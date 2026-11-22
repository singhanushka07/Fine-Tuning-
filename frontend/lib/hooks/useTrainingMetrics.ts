import { useQuery } from "@tanstack/react-query";
import { fetchTrainingMetrics } from "../api";

export function useTrainingMetrics() {
  return useQuery({
    queryKey: ["trainingMetrics"],
    queryFn: fetchTrainingMetrics,
    staleTime: 10 * 60 * 1000,
    gcTime: 15 * 60 * 1000,
  });
}
