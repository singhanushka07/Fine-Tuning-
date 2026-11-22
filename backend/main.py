from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
import logging

load_dotenv()

from routers import model, training, inference
from services.huggingface import init_hf_cache
from services.wandb_service import init_wandb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up...")
    await init_hf_cache()
    init_wandb()
    yield
    logger.info("Shutting down...")

app = FastAPI(
    title="PEFT Platform API",
    description="QLoRA fine-tuning showcase with fallback mechanisms",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(model.router, prefix="/api", tags=["model"])
app.include_router(training.router, prefix="/api", tags=["training"])
app.include_router(inference.router, prefix="/api", tags=["inference"])

def _map_status(raw: str) -> str:
    """Map internal status to frontend-expected values"""
    if raw == "live":
        return "live"
    elif raw == "degraded":
        return "degraded"
    return "down"

def _service_status(raw: str) -> dict:
    from datetime import datetime
    return {
        "status": _map_status(raw),
        "latency_ms": None,
        "error": None,
        "last_checked": datetime.utcnow().isoformat() + "Z"
    }

@app.get("/health")
async def health_check():
    from services.huggingface import get_hf_status
    from services.inference_service import get_inference_status
    from datetime import datetime

    hf = get_hf_status()
    inf = get_inference_status()
    groq_configured = bool(os.getenv("GROQ_API_KEY"))
    hf_configured = bool(os.getenv("HF_TOKEN"))

    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "services": {
            "huggingface": _service_status("live" if hf_configured else hf),
            "wandb": _service_status("live"),
            "inference": _service_status("live" if groq_configured or inf == "live" else inf)
        }
    }

@app.get("/")
async def root():
    return {"message": "PEFT Platform API", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
