import axios, { AxiosInstance } from "axios";
import {
  ApiResponse,
  HealthResponse,
  ModelInfo,
  TrainingMetricsData,
  InferenceResult,
  InferenceResponse,
} from "./types";

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://localhost:8002";

const api: AxiosInstance = axios.create({
  baseURL: `${API_BASE_URL}/api`,
  timeout: 10000,
});

// Retry logic with exponential backoff
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const config = error.config;

    if (!config || !error.response || error.response.status < 500) {
      return Promise.reject(error);
    }

    config.retryCount = config.retryCount || 0;
    if (config.retryCount >= 3) {
      return Promise.reject(error);
    }

    config.retryCount += 1;
    const delayMs = Math.pow(2, config.retryCount) * 1000;
    await new Promise((resolve) => setTimeout(resolve, delayMs));

    return api(config);
  }
);

export const fetchHealth = async (): Promise<HealthResponse | null> => {
  try {
    const baseUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8002";
    const response = await axios.get(`${baseUrl}/health`);
    return response.data;
  } catch (error) {
    console.error("Health check failed:", error);
    return null;
  }
};

export const fetchModelInfo = async (): Promise<
  ApiResponse<ModelInfo> | null
> => {
  try {
    const response = await api.get("/model/info");
    return response.data;
  } catch (error) {
    console.error("Failed to fetch model info:", error);
    return null;
  }
};

export const fetchAdapterConfig = async () => {
  try {
    const response = await api.get("/adapter/config");
    return response.data;
  } catch (error) {
    console.error("Failed to fetch adapter config:", error);
    return null;
  }
};

export const fetchTrainingMetrics = async (): Promise<
  ApiResponse<TrainingMetricsData> | null
> => {
  try {
    const response = await api.get("/training/metrics");
    return response.data;
  } catch (error) {
    console.error("Failed to fetch training metrics:", error);
    return null;
  }
};

export interface InferenceRequest {
  prompt: string;
  max_new_tokens?: number;
  temperature?: number;
}

export const inferBase = async (
  request: InferenceRequest
): Promise<ApiResponse<InferenceResult> | null> => {
  try {
    const response = await api.post("/inference/base", request);
    return response.data;
  } catch (error) {
    console.error("Failed to infer base model:", error);
    return null;
  }
};

export const inferFinetuned = async (
  request: InferenceRequest
): Promise<ApiResponse<InferenceResult> | null> => {
  try {
    const response = await api.post("/inference/finetuned", request);
    return response.data;
  } catch (error) {
    console.error("Failed to infer fine-tuned model:", error);
    return null;
  }
};

export const compareInference = async (
  request: InferenceRequest
): Promise<ApiResponse<InferenceResponse> | null> => {
  try {
    const response = await api.post("/inference/compare", request);
    return response.data;
  } catch (error) {
    console.error("Failed to compare inference:", error);
    return null;
  }
};

export default api;
