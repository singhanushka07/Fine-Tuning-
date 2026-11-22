import { useQuery } from "@tanstack/react-query";
import { fetchHealth } from "../api";
import { useConnectionStore } from "../store";
import { useEffect } from "react";

export function useHealth() {
  const updateAllStatuses = useConnectionStore((s) => s.updateAllStatuses);

  const { data, isLoading, isError } = useQuery({
    queryKey: ["health"],
    queryFn: fetchHealth,
    refetchInterval: 30000,
    staleTime: 5000,
  });

  useEffect(() => {
    if (data?.services) {
      updateAllStatuses({
        huggingface: data.services.huggingface.status,
        wandb: data.services.wandb.status,
        inference: data.services.inference.status,
      });
    }
  }, [data, updateAllStatuses]);

  return { data, isLoading, isError };
}
