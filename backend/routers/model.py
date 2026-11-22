"""Model information endpoints"""

from datetime import datetime
from fastapi import APIRouter
from typing import Dict, Any
from services.huggingface import fetch_model_info, fetch_adapter_config

router = APIRouter()

@router.get("/model/info")
async def get_model_info() -> Dict[str, Any]:
    """Get model info from HuggingFace Hub with fallback"""
    data, is_fallback = await fetch_model_info()

    return {
        "data": data,
        "fallback": is_fallback,
        "cached": not is_fallback,
        "timestamp": datetime.utcnow().isoformat()
    }

@router.get("/adapter/config")
async def get_adapter_config() -> Dict[str, Any]:
    """Get LoRA adapter configuration"""
    config, is_fallback = await fetch_adapter_config()

    stats = {
        "trainable_params": config.get("trainable_params", 3407872),
        "total_params": config.get("total_params", 8030261248),
        "lora_rank": config.get("r", 16),
        "lora_alpha": config.get("lora_alpha", 32),
        "effective_scaling": (config.get("lora_alpha", 32) / config.get("r", 16)),
        "target_module_count": len(config.get("target_modules", []))
    }

    return {
        "data": {
            **config,
            "compute_stats": stats
        },
        "fallback": is_fallback,
        "cached": not is_fallback
    }
