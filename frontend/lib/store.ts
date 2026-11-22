import { create } from "zustand";
import { ConnectionState } from "./types";

interface ConnectionStore extends ConnectionState {
  setHFStatus: (status: ConnectionState["huggingface"]) => void;
  setWandBStatus: (status: ConnectionState["wandb"]) => void;
  setInferenceStatus: (status: ConnectionState["inference"]) => void;
  updateAllStatuses: (statuses: ConnectionState) => void;
}

export const useConnectionStore = create<ConnectionStore>((set) => ({
  huggingface: "down",
  wandb: "down",
  inference: "down",

  setHFStatus: (status) => set({ huggingface: status }),
  setWandBStatus: (status) => set({ wandb: status }),
  setInferenceStatus: (status) => set({ inference: status }),
  updateAllStatuses: (statuses) => set(statuses),
}));
