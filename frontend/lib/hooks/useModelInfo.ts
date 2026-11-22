import { useQuery } from "@tanstack/react-query";
import { fetchModelInfo } from "../api";

export function useModelInfo() {
  return useQuery({
    queryKey: ["modelInfo"],
    queryFn: fetchModelInfo,
    staleTime: 5 * 60 * 1000,
    gcTime: 10 * 60 * 1000,
  });
}
