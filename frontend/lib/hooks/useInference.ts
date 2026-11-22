import { useMutation } from "@tanstack/react-query";
import { inferBase, inferFinetuned, InferenceRequest } from "../api";

export function useInference() {
  return useMutation({
    mutationFn: async (request: InferenceRequest) => {
      const [baseRes, finetunedRes] = await Promise.all([
        inferBase(request),
        inferFinetuned(request),
      ]);

      return {
        prompt: request.prompt,
        base: baseRes?.data,
        finetuned: finetunedRes?.data,
        baseIsFallback: baseRes?.fallback,
        finetunedIsFallback: finetunedRes?.fallback,
      };
    },
  });
}
