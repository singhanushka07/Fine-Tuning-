"""Training metrics endpoints"""

from fastapi import APIRouter
from typing import Dict, Any, List
from services.wandb_service import fetch_training_metrics, get_run_summary

router = APIRouter()

@router.get("/training/metrics")
async def get_training_metrics() -> Dict[str, Any]:
    """Get W&B training metrics with fallback"""
    metrics, is_fallback = await fetch_training_metrics()

    summary_data = await get_run_summary()

    return {
        "data": {
            "run_id": "demo-run-qlora",
            "run_name": "llama3-8b-qlora",
            "summary": summary_data,
            "metrics": metrics
        },
        "fallback": is_fallback,
        "cached": not is_fallback
    }

@router.get("/training/summary")
async def get_training_summary() -> Dict[str, Any]:
    """Get training run summary"""
    summary = await get_run_summary()

    return {
        "data": summary,
        "fallback": summary.get("is_fallback", False),
        "cached": False
    }
