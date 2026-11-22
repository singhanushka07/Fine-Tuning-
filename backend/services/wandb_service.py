"""Weights & Biases integration with fallback"""

import logging
import os
from typing import Optional, Dict, Any, List
from fallback_data import MOCK_TRAINING_METRICS, generate_training_metrics_extended

logger = logging.getLogger(__name__)

_wandb_status = "offline"
_cached_metrics: Optional[List[Dict[str, Any]]] = None

def init_wandb():
    """Initialize W&B connection"""
    logger.info("Initializing W&B service...")

def get_wandb_status() -> str:
    """Get W&B service status"""
    return _wandb_status

async def fetch_training_metrics() -> tuple[List[Dict[str, Any]], bool]:
    """
    Fetch training metrics from W&B with fallback
    Returns: (metrics_list, is_fallback)
    """
    global _wandb_status, _cached_metrics

    wandb_api_key = os.getenv("WANDB_API_KEY", "")
    wandb_run_path = os.getenv("WANDB_RUN_PATH", "")

    if not wandb_api_key or not wandb_run_path:
        logger.warning("W&B credentials not set, using fallback metrics")
        _wandb_status = "offline"
        return generate_training_metrics_extended(), True

    try:
        import wandb

        api = wandb.Api(overrides={"project": wandb_run_path.split("/")[1]})
        run = api.run(wandb_run_path)

        metrics_list = []
        history = run.history()

        for row in history:
            if "train_loss" in row and "eval_loss" in row:
                metrics_list.append({
                    "step": int(row.get("_step", 0)),
                    "epoch": int(row.get("epoch", 0)),
                    "train_loss": float(row.get("train_loss", 0)),
                    "eval_loss": float(row.get("eval_loss", 0)),
                    "learning_rate": float(row.get("learning_rate", 0)),
                    "grad_norm": float(row.get("grad_norm", 0))
                })

        _cached_metrics = metrics_list
        _wandb_status = "live"
        logger.info(f"Fetched {len(metrics_list)} metrics from W&B")
        return metrics_list, False

    except ImportError:
        logger.warning("wandb package not installed")
        _wandb_status = "offline"
    except Exception as e:
        logger.error(f"W&B error: {e}")
        _wandb_status = "degraded"

    if _cached_metrics:
        logger.info("Using cached W&B metrics")
        return _cached_metrics, True

    logger.info("Using static fallback W&B metrics")
    _cached_metrics = generate_training_metrics_extended()
    return _cached_metrics, True

async def get_run_summary() -> Dict[str, Any]:
    """Get run summary from W&B"""
    metrics, is_fallback = await fetch_training_metrics()

    if metrics:
        final_metrics = metrics[-1] if metrics else {}
        return {
            "best_eval_loss": min(m.get("eval_loss", float('inf')) for m in metrics) if metrics else 0.77,
            "final_train_loss": final_metrics.get("train_loss", 0),
            "total_steps": len(metrics),
            "is_fallback": is_fallback
        }

    return {
        "best_eval_loss": 0.77,
        "final_train_loss": 0.86,
        "total_steps": 500,
        "is_fallback": True
    }
