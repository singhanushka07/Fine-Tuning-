"use client";

import { useState } from "react";
import { AlertCircle, X } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

interface FallbackBannerProps {
  show: boolean;
  message?: string;
}

export function FallbackBanner({
  show,
  message = "Using cached or demo data — external services are offline",
}: FallbackBannerProps) {
  const [dismissed, setDismissed] = useState(false);

  return (
    <AnimatePresence>
      {show && !dismissed && (
        <motion.div
          initial={{ opacity: 0, y: -10, height: 0 }}
          animate={{ opacity: 1, y: 0, height: "auto" }}
          exit={{ opacity: 0, y: -10, height: 0 }}
          className="rounded-xl p-4 flex items-start gap-3 border border-[var(--accent-amber)] overflow-hidden"
          style={{
            background: "color-mix(in srgb, var(--accent-amber) 10%, var(--bg-card))",
          }}
        >
          <AlertCircle className="w-5 h-5 flex-shrink-0 mt-0.5" style={{ color: "var(--accent-amber)" }} />
          <div className="flex-1">
            <h3 className="font-semibold text-sm text-[var(--text-primary)]">Demo Mode Active</h3>
            <p className="text-xs text-[var(--text-secondary)] mt-0.5">{message}</p>
          </div>
          <button
            onClick={() => setDismissed(true)}
            className="flex-shrink-0 p-1 rounded-lg hover:bg-[var(--border)] transition-colors"
          >
            <X className="w-4 h-4 text-[var(--text-muted)]" />
          </button>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
