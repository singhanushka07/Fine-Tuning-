"""Inference endpoints for base and fine-tuned models"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import os
from services.inference_service import call_inference_api, compare_models

router = APIRouter()

class InferenceRequest(BaseModel):
    prompt: str
    max_new_tokens: Optional[int] = 256
    temperature: Optional[float] = 0.7

@router.post("/inference/base")
async def infer_base_model(request: InferenceRequest) -> Dict[str, Any]:
    """Generate from base model"""
    if len(request.prompt) > 500:
        raise HTTPException(status_code=422, detail="Prompt exceeds 500 character limit")

    base_model_id = os.getenv("HF_BASE_MODEL_ID", "NousResearch/Meta-Llama-3-8B-Instruct")
    response, is_fallback = await call_inference_api(
        base_model_id, request.prompt,
        max_new_tokens=request.max_new_tokens,
        temperature=request.temperature,
    )

    return {
        "data": {
            **response,
            "model_id": base_model_id,
            "finish_reason": "cached" if is_fallback else "stop"
        },
        "fallback": is_fallback,
        "cached": is_fallback
    }

@router.post("/inference/finetuned")
async def infer_finetuned_model(request: InferenceRequest) -> Dict[str, Any]:
    """Generate from fine-tuned model"""
    if len(request.prompt) > 500:
        raise HTTPException(status_code=422, detail="Prompt exceeds 500 character limit")

    finetuned_model_id = os.getenv("HF_FINETUNED_MODEL_ID", "Anushka69/llama3-cv-merged")
    response, is_fallback = await call_inference_api(
        finetuned_model_id, request.prompt,
        max_new_tokens=request.max_new_tokens,
        temperature=request.temperature,
    )

    return {
        "data": {
            **response,
            "model_id": finetuned_model_id,
            "finish_reason": "cached" if is_fallback else "stop"
        },
        "fallback": is_fallback,
        "cached": is_fallback
    }

@router.post("/inference/compare")
async def compare_inference(request: InferenceRequest) -> Dict[str, Any]:
    """Compare base vs fine-tuned responses"""
    if len(request.prompt) > 500:
        raise HTTPException(status_code=422, detail="Prompt exceeds 500 character limit")

    base_model_id = os.getenv("HF_BASE_MODEL_ID", "NousResearch/Meta-Llama-3-8B-Instruct")
    finetuned_model_id = os.getenv("HF_FINETUNED_MODEL_ID", "Anushka69/llama3-cv-merged")

    comparison = await compare_models(
        base_model_id, finetuned_model_id, request.prompt,
        max_new_tokens=request.max_new_tokens,
        temperature=request.temperature,
    )

    return {
        "data": comparison,
        "fallback": comparison["base"].get("is_fallback", False) or comparison["finetuned"].get("is_fallback", False),
        "cached": False
    }
