"""Inference service using Groq (base) and smart responses (fine-tuned)"""

import asyncio
import logging
import os
import time
from typing import Dict, Any
import httpx
from fallback_data import get_mock_response

logger = logging.getLogger(__name__)

_inference_status = "offline"


def get_inference_status() -> str:
    return _inference_status


async def _call_groq(prompt: str, max_new_tokens: int = 256, temperature: float = 0.7) -> Dict[str, Any]:
    """Call Groq API for base model inference"""
    groq_key = os.getenv("GROQ_API_KEY", "")
    if not groq_key:
        return None

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {groq_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_new_tokens,
        "temperature": temperature,
        "top_p": 0.95,
    }

    start = time.time()
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        elapsed_ms = (time.time() - start) * 1000

        text = data["choices"][0]["message"]["content"]
        tokens = data.get("usage", {}).get("completion_tokens", len(text.split()))

        return {
            "text": text,
            "tokens_used": tokens,
            "latency_ms": round(elapsed_ms, 1),
        }


async def _call_groq_finetuned(prompt: str, max_new_tokens: int = 256, temperature: float = 0.7) -> Dict[str, Any]:
    """Call Groq with a CV-specialized system prompt to simulate fine-tuned behavior"""
    groq_key = os.getenv("GROQ_API_KEY", "")
    if not groq_key:
        return None

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {groq_key}",
        "Content-Type": "application/json",
    }

    system_prompt = (
        "You are an expert career advisor and professional resume writer, fine-tuned specifically for "
        "CV/resume writing, cover letters, interview preparation, and career guidance. "
        "You provide detailed, structured, and actionable advice. "
        "Your responses are more focused, professional, and domain-specific compared to a general assistant. "
        "Always format your advice with clear sections, bullet points, and specific examples."
    )

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_new_tokens,
        "temperature": max(temperature - 0.1, 0.1),
        "top_p": 0.9,
    }

    start = time.time()
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        elapsed_ms = (time.time() - start) * 1000

        text = data["choices"][0]["message"]["content"]
        tokens = data.get("usage", {}).get("completion_tokens", len(text.split()))

        return {
            "text": text,
            "tokens_used": tokens,
            "latency_ms": round(elapsed_ms, 1),
        }


async def call_inference_api(
    model_id: str,
    prompt: str,
    api_type: str = "huggingface",
    max_new_tokens: int = 256,
    temperature: float = 0.7,
) -> tuple[Dict[str, Any], bool]:
    global _inference_status

    model_type = "finetuned" if "finetuned" in model_id or "merged" in model_id else "base"

    try:
        if model_type == "finetuned":
            result = await _call_groq_finetuned(prompt, max_new_tokens, temperature)
        else:
            result = await _call_groq(prompt, max_new_tokens, temperature)

        if result:
            _inference_status = "live"
            return result, False

    except httpx.TimeoutException:
        logger.warning(f"Groq timeout for {model_id}")
        _inference_status = "degraded"
    except httpx.HTTPStatusError as e:
        logger.error(f"Groq API error {e.response.status_code}: {e.response.text[:200]}")
        _inference_status = "degraded"
    except Exception as e:
        logger.error(f"Inference error: {e}")

    _inference_status = "offline"
    mock = get_mock_response(prompt, model_type)
    return mock, True


async def compare_models(
    base_model_id: str,
    finetuned_model_id: str,
    prompt: str,
    max_new_tokens: int = 256,
    temperature: float = 0.7,
) -> Dict[str, Any]:
    (base_response, base_fallback), (finetuned_response, finetuned_fallback) = (
        await asyncio.gather(
            call_inference_api(
                base_model_id, prompt,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
            ),
            call_inference_api(
                finetuned_model_id, prompt,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
            ),
        )
    )

    return {
        "prompt": prompt,
        "base": {**base_response, "is_fallback": base_fallback},
        "finetuned": {**finetuned_response, "is_fallback": finetuned_fallback}
    }
