"use client";

import { useHealth } from "@/lib/hooks/useHealth";
import { useConnectionStore } from "@/lib/store";
import { ConnectionBadge } from "../shared/ConnectionBadge";

export function ConnectionStatus() {
  const { huggingface, wandb, inference } = useConnectionStore();
  useHealth();

  return (
    <div className="flex gap-2 items-center flex-wrap">
      <ConnectionBadge status={huggingface} label="HF" />
      <ConnectionBadge status={wandb} label="W&B" />
      <ConnectionBadge status={inference} label="Inference" />
    </div>
  );
}
