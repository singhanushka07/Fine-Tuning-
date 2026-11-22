# PEFT Platform - Quick Start Guide

Get the PEFT showcase platform running in 5 minutes.

## Option 1: Docker Compose (Easiest)

### Prerequisites
- Docker & Docker Compose installed
- (Optional) HuggingFace API token
- (Optional) Weights & Biases API key

### Steps

1. **Clone/Setup**
```bash
cd Fine-Tunning
```

2. **Create environment file**
```bash
cat > .env << EOF
HF_TOKEN=your_token_here_or_leave_empty
HF_MODEL_ID=Anushka69/llama3-finetuned-cv-adapter
WANDB_API_KEY=your_key_here_or_leave_empty
WANDB_RUN_PATH=workspace/project/run_id
EOF
```

3. **Start everything**
```bash
docker-compose up
```

4. **Open in browser**
- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

That's it! The platform runs with fallback data if API credentials are missing.

---

## Option 2: Manual Setup (More Control)

### Backend

```bash
cd backend

# Setup Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your credentials

# Run
uvicorn main:app --reload
```

Backend will be at `http://localhost:8000`

### Frontend (New Terminal)

```bash
cd frontend

# Install dependencies
npm install

# Create environment file
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

# Run
npm run dev
```

Frontend will be at `http://localhost:3000`

---

## Testing Fallback Mode

The platform works **even without any credentials**. Try:

### Test 1: No API Keys
Just run without setting `HF_TOKEN` or `WANDB_API_KEY`:

```bash
# Backend will use fallback data
uvicorn main:app --reload

# Frontend shows:
# ✅ Dashboard with hardcoded stats
# ✅ Training charts with demo metrics
# ✅ Inference playground with cached responses
# ✅ Architecture visualizer (fully static)
```

Look for the **yellow "Fallback Data" banner** - it shows what's cached.

### Test 2: Partial Credentials
Set only `HF_TOKEN`:
- ✅ Real model metadata from HuggingFace
- ⚠️ W&B metrics use fallback demo data
- ✅ Inference uses HF API

---

## Platform Overview

### 📊 Dashboard (`/`)
- Hero overview with key metrics
- Trainable parameters: 0.085%
- GPU memory saved: 70%
- LoRA adapter configuration
- Quick links to other pages

### 📈 Training Metrics (`/metrics`)
- Loss curves (training & validation)
- Learning rate schedule
- Gradient norms over steps
- Training configuration summary
- Performance insights

### 🎮 Inference Playground (`/playground`)
- Enter any prompt (up to 500 chars)
- Submit prompt to compare models
- Side-by-side responses
- Latency & token count comparison
- Quick example prompts

### 🏗️ Architecture (`/architecture`)
- QLoRA architecture breakdown
- Parameter distribution pie chart
- GPU memory comparison
- Technical specifications
- Why QLoRA is effective

---

## Key Features

### ✨ Always Works
Even if HuggingFace Hub and W&B are down:
- Responses include `fallback: true` flag
- UI shows yellow banner
- All pages remain functional with demo data

### 🔄 Smart Caching
- HF model metadata: 30-min cache TTL
- Training metrics: In-memory cache
- Inference: Fallback Q&A pairs
- Auto-retry with exponential backoff

### 📡 Service Status Bar
Top-right corner shows three badges:
- 🟢 Green = Live
- 🟡 Yellow = Degraded (cached)
- 🔴 Red = Offline

Polls every 30 seconds.

---

## Example Prompts to Try

```
"What is QLoRA and how does it reduce memory?"
"Explain parameter-efficient fine-tuning"
"How does LoRA work in transformer models?"
"What are the benefits of 4-bit quantization?"
"Compare full fine-tuning vs QLoRA"
```

---

## Troubleshooting

### Port Already in Use
```bash
# Change ports in docker-compose.yml or use:
# Backend
uvicorn main:app --reload --port 8001

# Frontend
npm run dev -- -p 3001
```

### CORS Errors
- Frontend at `localhost:3000` → Backend at `localhost:8000` ✅
- Or use `NEXT_PUBLIC_API_URL` env var

### Modules Not Found
```bash
# Frontend
cd frontend && npm install

# Backend
cd backend && pip install -r requirements.txt
```

### W&B Not Loading
- Optional - platform works without it
- Check `WANDB_API_KEY` and `WANDB_RUN_PATH` in `.env`
- Falls back to demo metrics if missing

---

## What to Show

Perfect for demonstrations:

1. **Dashboard** - Shows efficiency metrics, scroll through cards
2. **Metrics** - Hover over charts, show convergence
3. **Playground** - Submit prompts, compare responses side-by-side
4. **Architecture** - Click through QLoRA breakdown, show memory savings
5. **Connection Status** - Disconnect backend, watch badges turn red, then yellow (cached)

---

## Next Steps

### Deploy to Production
- **Frontend**: Push to GitHub, deploy to Vercel
- **Backend**: Deploy to Railway
- See `README.md` for detailed instructions

### Customize
- Edit `fallback_data.py` for different demo metrics
- Update colors in components using Tailwind config
- Add your own model metadata to model card

### Extend
- Connect to real Llama 3 8B inference
- Load actual fine-tuned model weights
- Add more comparison metrics
- Integrate with your training pipeline

---

## Support

**Health Check:**
```bash
curl http://localhost:8000/health
```

Should return:
```json
{
  "status": "ok",
  "services": {
    "huggingface": { "status": "live|degraded|down" },
    "wandb": { "status": "live|degraded|down" },
    "inference": { "status": "live|degraded|down" }
  }
}
```

**API Docs:**
Visit http://localhost:8000/docs for interactive Swagger UI

---

**Start now:** `docker-compose up` 🚀
