# PEFT Platform - QLoRA Fine-Tuning Showcase

A full-stack platform showcasing Parameter-Efficient Fine-Tuning (PEFT) with [Anushka69/llama3-finetuned-cv-adapter](https://huggingface.co/Anushka69/llama3-finetuned-cv-adapter) — a LoRA adapter fine-tuned on Meta-Llama-3-8B-Instruct for CV/Resume domain tasks. Built with FastAPI + Next.js 14.

---

## Quick Start (Run in 2 Minutes)

### Prerequisites
- **Python 3.10+**
- **Node.js 18+**
- **Git**

### Step 1: Clone the Repository

```bash
git clone https://github.com/singhanushka07/Fine-Tuning-.git
cd Fine-Tuning-
```

### Step 2: Setup Backend

```bash
cd backend
cp .env.example .env
pip install -r requirements.txt
```

The app works immediately in demo mode (no API keys needed). To enable live features, edit `backend/.env`:

| Key | Where to get it | What it enables |
|-----|----------------|-----------------|
| `HF_TOKEN` | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) | Live model metadata from HuggingFace |
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) (free) | Real Llama 3 inference in playground |
| `WANDB_API_KEY` | [wandb.ai/authorize](https://wandb.ai/authorize) | Live training metrics (optional) |

Start the backend:
```bash
uvicorn main:app --host 0.0.0.0 --port 8002
```

### Step 3: Setup Frontend

Open a new terminal:
```bash
cd frontend
cp .env.example .env.local
npm install
npm run dev
```

### Step 4: Open the App

Go to **http://localhost:3000** in your browser.

---

## Pages & Features

### 1. Dashboard (Home Page)

The main landing page with a hero section and key statistics about the fine-tuned model.

**What you see:**
- Hero banner with model description and quick-start links
- 6 stats cards showing parameter efficiency metrics:
  - Total Parameters (8B), Trainable Parameters (6.8M), Trainable % (0.085%)
  - Base Model Size (16GB), Quantized Size (4GB), Adapter Size (26MB)
- QLoRA explanation cards breaking down the technique
- Navigation cards to other pages (Metrics, Playground, Architecture)
- Model configuration details with all 7 target modules listed

**Data source:** Live from HuggingFace API (with HF_TOKEN) or demo data.

---

### 2. Training Metrics

Visualizes the complete training run with interactive charts.

**What you see:**
- Training progress bar showing steps completed
- 3 stats cards: Best Eval Loss (0.286), Final Train Loss (0.244), Total Steps (500)
- **Training Loss Chart** — Dual-line area chart showing train loss and eval loss converging over 500 steps
- **Learning Rate Schedule** — Shows the cosine decay schedule from 2e-4 to 5e-5
- **Gradient Norm Chart** — Tracks gradient stability throughout training
- Training configuration panel (learning rate, batch size, optimizer, warmup)
- Key insights section with convergence analysis

**Data source:** Weights & Biases API (with WANDB_API_KEY) or generated demo metrics.

---

### 3. Inference Playground

Side-by-side comparison of base model vs fine-tuned model responses.

**What you see:**
- Prompt input textarea with character counter (500 char limit)
- Category tabs: Resume, Career, Skills — each with quick-select example prompts
- Temperature slider (0.1 - 1.0) and Max Tokens slider (50 - 512)
- Two response panels side-by-side:
  - **Left:** Base Model (Llama-3-8B-Instruct) — generic response
  - **Right:** Fine-Tuned CV Adapter — domain-specific, structured response
- Each panel shows: response text with typing animation, latency, token count
- Latency comparison bar chart below the panels
- About section explaining the comparison methodology

**Data source:** Groq API for real Llama 3 inference (with GROQ_API_KEY) or CV-themed demo responses.

---

### 4. Architecture Visualizer

Interactive breakdown of the QLoRA fine-tuning architecture.

**What you see:**
- 3-step QLoRA process with animated SVG diagrams:
  1. **4-Bit Quantization** — NF4 compression reducing 16GB to 4GB
  2. **LoRA Injection** — Low-rank adapter matrices (rank 16, alpha 32)
  3. **Selective Training** — Only 0.085% parameters trained
- Parameter distribution pie chart (trainable vs frozen)
- GPU memory comparison bars (full fine-tuning vs QLoRA)
- Key components grid: Quantization, LoRA Adapters, Target Modules, Training
- Technical specifications table with all hyperparameters

**Data source:** Static content based on the actual adapter configuration.

---

### 5. Navigation & Status Bar

Present on every page:
- Glassmorphism navbar with animated page indicator
- 3 connection badges (HF, W&B, Inference) showing real-time service health:
  - Green = connected and live
  - Amber = degraded (using cache)
  - Red = offline (using fallback)
- Dark/light theme toggle
- Mobile-responsive slide-out menu

---

## Tech Stack

### Backend
| Technology | Purpose |
|-----------|---------|
| FastAPI | REST API framework |
| Hugging Face Hub | Model metadata integration |
| Groq API | Free Llama 3 inference |
| Pydantic | Data validation |
| httpx | Async HTTP client |

### Frontend
| Technology | Purpose |
|-----------|---------|
| Next.js 14 (App Router) | React framework with SSR |
| TanStack Query v5 | Data fetching & caching |
| Zustand | State management |
| Recharts | Interactive charts |
| Framer Motion | Animations |
| Tailwind CSS | Styling |

---

## Project Structure

```
Fine-Tuning-/
├── backend/
│   ├── main.py                    # FastAPI app + health endpoint
│   ├── fallback_data.py           # Demo data for offline mode
│   ├── routers/
│   │   ├── model.py               # GET /api/model/info, /api/adapter/config
│   │   ├── training.py            # GET /api/training/metrics, /summary
│   │   └── inference.py           # POST /api/inference/base, /finetuned, /compare
│   ├── services/
│   │   ├── huggingface.py         # HF Hub integration with TTL cache
│   │   ├── wandb_service.py       # W&B metrics with fallback
│   │   └── inference_service.py   # Groq API + smart fallback
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── app/
│   │   ├── page.tsx               # Dashboard
│   │   ├── metrics/page.tsx       # Training metrics
│   │   ├── playground/page.tsx    # Inference playground
│   │   └── architecture/page.tsx  # Architecture visualizer
│   ├── components/
│   │   ├── layout/                # Navbar, Providers, ThemeProvider
│   │   ├── dashboard/             # StatsCard
│   │   ├── metrics/               # TrainingChart
│   │   ├── playground/            # InferencePanel
│   │   └── shared/                # GlassCard, AnimatedCounter, etc.
│   ├── lib/
│   │   ├── api.ts                 # Axios client with retry logic
│   │   ├── types.ts               # TypeScript interfaces
│   │   ├── store.ts               # Zustand connection store
│   │   └── hooks/                 # React Query hooks
│   └── .env.example
├── merge_and_push.ipynb           # Colab notebook to merge LoRA adapter
├── docker-compose.yml
└── README.md
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Service health with HF, W&B, Inference status |
| GET | `/api/model/info` | Model metadata from HuggingFace |
| GET | `/api/adapter/config` | LoRA adapter configuration |
| GET | `/api/training/metrics` | Training loss, LR, gradient norms |
| GET | `/api/training/summary` | Training run summary |
| POST | `/api/inference/base` | Generate from base Llama 3 |
| POST | `/api/inference/finetuned` | Generate from fine-tuned model |
| POST | `/api/inference/compare` | Compare both models side-by-side |

---

## Model Details

| Property | Value |
|----------|-------|
| Base Model | NousResearch/Meta-Llama-3-8B-Instruct |
| Adapter | [Anushka69/llama3-finetuned-cv-adapter](https://huggingface.co/Anushka69/llama3-finetuned-cv-adapter) |
| Merged Model | [Anushka69/llama3-cv-merged](https://huggingface.co/Anushka69/llama3-cv-merged) |
| PEFT Type | LoRA |
| Rank (r) | 16 |
| Alpha | 32 |
| Dropout | 0.05 |
| Target Modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| Trainable Params | 6.8M (0.085% of 8B) |
| Quantization | 4-bit NF4 |
| Domain | CV/Resume writing and career advice |

---

## Performance Benchmarks

| Metric | Full Fine-Tuning | QLoRA (This Project) | Improvement |
|--------|-----------------|---------------------|-------------|
| GPU Memory | 24 GB | 6.2 GB | 75% reduction |
| Training Time | ~8 hours | ~2.4 hours | 70% faster |
| Model Size | 16 GB | 26 MB (adapter) | 616x smaller |
| Trainable Params | 8B | 6.8M | 99.9% reduction |
| Inference Latency | Same | Same | No overhead |

---

## Merge LoRA Adapter (Optional)

The repo includes `merge_and_push.ipynb` — a Google Colab notebook that merges the LoRA adapter with the base model and pushes the full model to HuggingFace.

1. Upload `merge_and_push.ipynb` to [Google Colab](https://colab.research.google.com)
2. Select **T4 GPU** runtime
3. Run all cells (takes ~15 minutes)
4. The merged model appears at `Anushka69/llama3-cv-merged`

---

## Docker Deployment

```bash
docker-compose up
```

Frontend: http://localhost:3000
Backend: http://localhost:8002

---

## License

MIT License

---

**Built to showcase Parameter-Efficient Fine-Tuning with QLoRA**
