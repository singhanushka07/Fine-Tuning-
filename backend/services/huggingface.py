"""Hugging Face Hub integration with caching and fallback"""

import logging
import os
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import httpx
from fallback_data import MOCK_MODEL_INFO

logger = logging.getLogger(__name__)

class HFCache:
    def __init__(self, ttl_seconds: int = 1800):
        self.data: Optional[Dict[str, Any]] = None
        self.timestamp: Optional[datetime] = None
        self.ttl = ttl_seconds
        self.status = "offline"

    def is_valid(self) -> bool:
        if not self.data or not self.timestamp:
            return False
        return datetime.now() - self.timestamp < timedelta(seconds=self.ttl)

    def set(self, data: Dict[str, Any]):
        self.data = data
        self.timestamp = datetime.now()
        self.status = "live"
        logger.info("HF cache updated")

    def get(self) -> Optional[Dict[str, Any]]:
        if self.is_valid():
            return self.data
        return None

_hf_cache = HFCache(ttl_seconds=int(os.getenv("HF_CACHE_TTL", 1800)))

async def init_hf_cache():
    """Initialize cache on startup by fetching model info"""
    logger.info("Initializing HF cache...")
    try:
        await fetch_model_info()
        logger.info(f"HF cache initialized, status: {_hf_cache.status}")
    except Exception as e:
        logger.warning(f"HF cache init failed: {e}")

def get_hf_status() -> str:
    """Get HF service status"""
    if _hf_cache.is_valid():
        return "live"
    return "offline"

async def fetch_model_info() -> tuple[Dict[str, Any], bool]:
    """
    Fetch model info from HF Hub with fallback to cache/static data
    Returns: (data, is_fallback)
    """
    hf_token = os.getenv("HF_TOKEN", "")
    hf_model_id = os.getenv("HF_MODEL_ID", "Anushka69/llama3-finetuned-cv-adapter")

    if not hf_token:
        logger.warning("HF_TOKEN not set, using fallback data")
        return MOCK_MODEL_INFO, True

    try:
        url = f"https://huggingface.co/api/models/{hf_model_id}"
        headers = {"Authorization": f"Bearer {hf_token}"}

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            enriched_data = {
                "model_id": data.get("id", hf_model_id),
                "base_model": data.get("base_model", "NousResearch/Meta-Llama-3-8B-Instruct"),
                "description": data.get("description", ""),
                "downloads": data.get("downloads", 0),
                "likes": data.get("likes", 0),
                "tags": data.get("tags", []),
                "adapter_config": MOCK_MODEL_INFO["adapter_config"],
                "quantization_config": MOCK_MODEL_INFO["quantization_config"],
                "training_config": MOCK_MODEL_INFO["training_config"],
                "parameter_stats": MOCK_MODEL_INFO["parameter_stats"]
            }

            _hf_cache.set(enriched_data)
            return enriched_data, False

    except httpx.TimeoutException:
        logger.error("HF Hub timeout")
        _hf_cache.status = "degraded"
    except httpx.RequestError as e:
        logger.error(f"HF Hub error: {e}")
        _hf_cache.status = "offline"
    except Exception as e:
        logger.error(f"Unexpected error fetching HF data: {e}")
        _hf_cache.status = "offline"

    cached = _hf_cache.get()
    if cached:
        logger.info("Using cached HF data")
        _hf_cache.status = "degraded"
        return cached, True

    logger.info("Using static fallback HF data")
    return MOCK_MODEL_INFO, True

async def fetch_adapter_config() -> tuple[Dict[str, Any], bool]:
    """Fetch LoRA adapter configuration"""
    model_info, is_fallback = await fetch_model_info()
    return model_info.get("adapter_config", MOCK_MODEL_INFO["adapter_config"]), is_fallback
