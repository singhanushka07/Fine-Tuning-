export interface ApiResponse<T> {
  data: T;
  fallback: boolean;
  cached: boolean;
  timestamp?: string;
}

export interface ServiceStatus {
  status: "live" | "degraded" | "down";
  latency_ms: number | null;
  error: string | null;
  last_checked: string;
}

export interface HealthResponse {
  status: "ok" | "degraded" | "down";
  timestamp: string;
  services: {
    huggingface: ServiceStatus;
    wandb: ServiceStatus;
    inference: ServiceStatus;
  };
}

export interface AdapterConfig {
  r: number;
  lora_alpha: number;
  target_modules: string[];
  lora_dropout: number;
  bias: string;
  task_type: string;
  peft_type?: string;
}

export interface QuantizationConfig {
  load_in_4bit: boolean;
  bnb_4bit_quant_type: string;
  bnb_4bit_compute_dtype: string;
  bnb_4bit_use_double_quant: boolean;
}

export interface TrainingStats {
  total_params: number;
  trainable_params: number;
  trainable_percent: number;
  base_model_size_gb: number;
  quantized_size_gb: number;
  adapter_size_mb: number;
}

export interface ModelInfo {
  model_id: string;
  base_model: string;
  description: string;
  downloads: number;
  likes: number;
  tags: string[];
  adapter_config: AdapterConfig;
  quantization_config: QuantizationConfig;
  training_config: Record<string, any>;
  parameter_stats: TrainingStats;
}

export interface MetricPoint {
  step: number;
  epoch?: number;
  train_loss?: number;
  eval_loss?: number;
  learning_rate?: number;
  grad_norm?: number;
  value?: number;
}

export interface TrainingMetricsData {
  run_id: string;
  run_name: string;
  summary: {
    best_eval_loss: number;
    final_train_loss: number;
    total_steps: number;
  };
  metrics: MetricPoint[];
}

export interface InferenceResult {
  text: string;
  tokens_used: number;
  latency_ms: number;
  model_id?: string;
  finish_reason?: "cached" | "stop" | "length";
}

export interface InferenceResponse {
  base: InferenceResult & { is_fallback: boolean };
  finetuned: InferenceResult & { is_fallback: boolean };
  prompt: string;
}

export interface ConnectionState {
  huggingface: "live" | "degraded" | "down";
  wandb: "live" | "degraded" | "down";
  inference: "live" | "degraded" | "down";
}
