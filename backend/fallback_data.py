"""Static fallback data when APIs are unavailable"""

MOCK_MODEL_INFO = {
    "model_id": "Anushka69/llama3-finetuned-cv-adapter",
    "base_model": "NousResearch/Meta-Llama-3-8B-Instruct",
    "description": "CV/Resume domain fine-tuned Llama 3 8B using LoRA adapters for professional document generation and analysis",
    "downloads": 0,
    "likes": 0,
    "tags": ["llama3", "peft", "lora", "instruct", "fine-tuned", "safetensors", "cv", "resume"],
    "adapter_config": {
        "r": 16,
        "lora_alpha": 32,
        "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        "lora_dropout": 0.05,
        "bias": False,
        "task_type": "CAUSAL_LM",
        "peft_type": "LORA"
    },
    "quantization_config": {
        "load_in_4bit": True,
        "bnb_4bit_quant_type": "nf4",
        "bnb_4bit_compute_dtype": "bfloat16",
        "bnb_4bit_use_double_quant": True
    },
    "training_config": {
        "max_seq_length": 2048,
        "output_dir": "./results",
        "num_train_epochs": 3,
        "per_device_train_batch_size": 4,
        "gradient_accumulation_steps": 4,
        "learning_rate": 2e-4,
        "warmup_ratio": 0.03,
        "lr_scheduler_type": "constant",
        "save_strategy": "epoch"
    },
    "parameter_stats": {
        "total_params": 8030000000,
        "trainable_params": 6815744,
        "trainable_percent": 0.0848,
        "base_model_size_gb": 16,
        "quantized_size_gb": 4,
        "adapter_size_mb": 96
    }
}

MOCK_TRAINING_METRICS = [
    {"step": 0, "train_loss": 2.8342, "eval_loss": 2.7891, "learning_rate": 0.0002, "grad_norm": 1.2341},
    {"step": 50, "train_loss": 2.6234, "eval_loss": 2.5892, "learning_rate": 0.0002, "grad_norm": 1.0987},
    {"step": 100, "train_loss": 2.4567, "eval_loss": 2.3456, "learning_rate": 0.0002, "grad_norm": 0.9876},
    {"step": 150, "train_loss": 2.2891, "eval_loss": 2.1234, "learning_rate": 0.0002, "grad_norm": 0.8765},
    {"step": 200, "train_loss": 2.0456, "eval_loss": 1.9876, "learning_rate": 0.0002, "grad_norm": 0.7654},
    {"step": 250, "train_loss": 1.8234, "eval_loss": 1.7891, "learning_rate": 0.0002, "grad_norm": 0.6543},
    {"step": 300, "train_loss": 1.6789, "eval_loss": 1.5234, "learning_rate": 0.0002, "grad_norm": 0.5432},
    {"step": 350, "train_loss": 1.4567, "eval_loss": 1.3456, "learning_rate": 0.0001, "grad_norm": 0.4321},
    {"step": 400, "train_loss": 1.2891, "eval_loss": 1.1789, "learning_rate": 0.0001, "grad_norm": 0.3210},
    {"step": 450, "train_loss": 1.0234, "eval_loss": 0.9876, "learning_rate": 0.0001, "grad_norm": 0.2109},
    {"step": 500, "train_loss": 0.8567, "eval_loss": 0.7654, "learning_rate": 0.0001, "grad_norm": 0.1987},
]

MOCK_RESPONSES = {
    "base": {
        "text": "A resume is a document that summarizes your work experience, education, and skills. It is typically used when applying for jobs. A good resume should be clear and concise, highlighting your most relevant qualifications for the position you are seeking.",
        "tokens_used": 48,
        "latency_ms": 1243
    },
    "finetuned": {
        "text": "A professional CV should be strategically structured with a compelling summary statement, quantified achievements (e.g., 'increased revenue by 35%'), and ATS-optimized keywords matching the target role. Use reverse-chronological format for experience, include a skills matrix aligned to the job description, and keep formatting clean with consistent typography. Tailor each application: mirror the employer's language from the posting to maximize keyword match rates.",
        "tokens_used": 72,
        "latency_ms": 892
    }
}

MOCK_RESPONSE_PAIRS = [
    {
        "keywords": ["resume", "cv", "curriculum vitae"],
        "base": {"text": "A resume is a document that lists your work experience and education. You should include your name, contact info, work history, and education.", "tokens_used": 28, "latency_ms": 1243},
        "finetuned": {"text": "A professional CV should follow a strategic structure: start with a compelling summary (2-3 lines positioning your value proposition), then list experience in reverse-chronological order with quantified achievements (e.g., 'Reduced deployment time by 40%'). Include a skills matrix with both technical and soft skills, tailored to the job description. Use ATS-friendly formatting—avoid tables, graphics, and unusual fonts. End with certifications and relevant projects. Each bullet should follow the CAR format: Challenge, Action, Result.", "tokens_used": 92, "latency_ms": 876}
    },
    {
        "keywords": ["cover letter", "application"],
        "base": {"text": "A cover letter is a letter you send with your resume when applying for a job. It should explain why you want the job and why you're qualified.", "tokens_used": 30, "latency_ms": 1156},
        "finetuned": {"text": "An effective cover letter follows a proven structure: Opening paragraph hooks with a specific connection to the company (recent news, product, or mission alignment). The body maps your top 2-3 achievements directly to the job requirements using the STAR method. Quantify impact wherever possible. Close with a clear call to action and enthusiasm for the role. Keep it under 400 words. Address it to the hiring manager by name when possible—use LinkedIn to research. Avoid restating your resume; instead, tell the story behind your best achievements.", "tokens_used": 95, "latency_ms": 912}
    },
    {
        "keywords": ["interview", "prepare", "question"],
        "base": {"text": "To prepare for an interview, research the company and practice answering common questions. Dress professionally and arrive on time.", "tokens_used": 22, "latency_ms": 1089},
        "finetuned": {"text": "Interview preparation should be systematic: 1) Research the company's recent earnings, product launches, and culture via Glassdoor and LinkedIn. 2) Map your experience to the role using the STAR framework (Situation, Task, Action, Result) for 8-10 behavioral questions. 3) Prepare 3-5 insightful questions showing strategic thinking (e.g., 'What does success look like in the first 90 days?'). 4) Practice with mock interviews focusing on conciseness—aim for 90-second responses. 5) Prepare a 2-minute elevator pitch connecting your background to this specific role's requirements.", "tokens_used": 105, "latency_ms": 934}
    },
    {
        "keywords": ["skill", "skills", "technical"],
        "base": {"text": "Technical skills are abilities related to technology and specific tools. You should list relevant skills on your resume.", "tokens_used": 20, "latency_ms": 1198},
        "finetuned": {"text": "Skills presentation on a CV requires strategic categorization: group into Technical Skills (languages, frameworks, tools), Domain Expertise (industry-specific knowledge), and Leadership/Soft Skills. Rate proficiency honestly—use 'proficient', 'experienced', 'familiar' rather than arbitrary scales. Prioritize skills mentioned in the job posting. For tech roles, include specific versions and ecosystem tools (e.g., 'Python 3.11, FastAPI, PostgreSQL, Docker, AWS ECS'). Add a 'Currently Learning' section to show growth mindset. Link to portfolio projects that demonstrate each key skill in practice.", "tokens_used": 98, "latency_ms": 867}
    },
    {
        "keywords": ["fine-tuning", "fine tuning", "lora", "qlora", "peft", "adapter"],
        "base": {"text": "Fine-tuning is a technique where you take a pre-trained model and train it further on a specific dataset to adapt it for a particular task or domain.", "tokens_used": 32, "latency_ms": 1312},
        "finetuned": {"text": "This CV adapter was built using LoRA (Low-Rank Adaptation) on NousResearch/Meta-Llama-3-8B-Instruct. The adapter applies trainable low-rank matrices (r=16, alpha=32) to 7 target modules: q_proj, k_proj, v_proj, o_proj (attention) and gate_proj, up_proj, down_proj (feed-forward). Only 0.085% of parameters are trained while the base model stays frozen. The ~96MB adapter specializes the model for CV/resume domain tasks—professional document generation, career advice, and job application optimization—while preserving the base model's general capabilities.", "tokens_used": 112, "latency_ms": 845}
    },
    {
        "keywords": ["experience", "work history", "job"],
        "base": {"text": "Work experience should be listed on your resume in reverse order, starting with your most recent job.", "tokens_used": 18, "latency_ms": 1267},
        "finetuned": {"text": "Each work experience entry should lead with impact, not duties. Structure as: Role Title | Company | Dates, then 3-5 bullet points using action verbs (Led, Architected, Optimized, Delivered). Quantify everything: revenue impact, team size, percentage improvements, scale metrics. Example: 'Architected microservices migration serving 2M+ daily users, reducing p99 latency from 800ms to 120ms.' For career gaps, address proactively with freelance work, certifications, or relevant projects completed during that period.", "tokens_used": 88, "latency_ms": 876}
    }
]


def get_mock_response(prompt: str, model_type: str) -> dict:
    """Fuzzy-match the prompt against keyword pairs and return the appropriate mock response.

    Args:
        prompt: The user's input prompt.
        model_type: Either "base" or "finetuned".

    Returns:
        A dict with text, tokens_used, and latency_ms.
    """
    prompt_lower = prompt.lower()
    for pair in MOCK_RESPONSE_PAIRS:
        for keyword in pair["keywords"]:
            if keyword.lower() in prompt_lower:
                return pair[model_type]
    # No keyword matched -- fall back to generic MOCK_RESPONSES
    return MOCK_RESPONSES.get(model_type, MOCK_RESPONSES["base"])


MOCK_ADAPTER_CONFIG = {
    "r": 16,
    "lora_alpha": 32,
    "target_modules": [
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj"
    ],
    "lora_dropout": 0.05,
    "bias": False,
    "task_type": "CAUSAL_LM",
    "peft_type": "LORA",
    "init_lora_weights": True
}

def generate_training_metrics_extended(num_steps: int = 500) -> list:
    """Generate extended training metrics with more realistic progression"""
    import math
    metrics = []

    for step in range(0, num_steps, 10):
        progress = step / num_steps
        train_loss = 2.8 * math.exp(-2.5 * progress) + 0.2 * (1 - progress**0.5)
        eval_loss = 2.7 * math.exp(-2.3 * progress) + 0.25 * (1 - progress**0.5)
        lr = 0.0002 if step < 350 else 0.0001 if step < 450 else 0.00005
        grad_norm = 1.2 * math.exp(-2.0 * progress)

        metrics.append({
            "step": step,
            "epoch": step // 100,
            "train_loss": round(train_loss, 4),
            "eval_loss": round(eval_loss, 4),
            "learning_rate": lr,
            "grad_norm": round(grad_norm, 4)
        })

    return metrics
