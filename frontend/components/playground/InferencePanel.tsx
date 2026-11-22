"use client";

import { InferenceResult } from "@/lib/types";
import { Loader2, Zap, AlertCircle, Copy, Check } from "lucide-react";
import { motion } from "framer-motion";
import { useState, useEffect } from "react";

interface InferencePanelProps {
  title: string;
  result?: InferenceResult;
  loading?: boolean;
  isFallback?: boolean;
  error?: string;
  accentColor?: string;
  typingSpeed?: number;
}

export function InferencePanel({
  title,
  result,
  loading,
  isFallback,
  error,
  accentColor = "var(--accent-blue)",
  typingSpeed = 15,
}: InferencePanelProps) {
  const [displayedText, setDisplayedText] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    if (!result?.text) {
      setDisplayedText("");
      setIsTyping(false);
      return;
    }

    setIsTyping(true);
    setDisplayedText("");
    let idx = 0;
    const text = result.text;
    const interval = setInterval(() => {
      idx++;
      setDisplayedText(text.slice(0, idx));
      if (idx >= text.length) {
        clearInterval(interval);
        setIsTyping(false);
      }
    }, typingSpeed);

    return () => clearInterval(interval);
  }, [result?.text, typingSpeed]);

  const handleCopy = async () => {
    if (!result?.text) return;
    await navigator.clipboard.writeText(result.text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <motion.div
      className="rounded-xl border border-[var(--border)] overflow-hidden backdrop-blur-md"
      style={{ background: "var(--bg-card)" }}
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
    >
      <div
        className="border-b border-[var(--border)] px-6 py-4"
        style={{
          background: `linear-gradient(135deg, color-mix(in srgb, ${accentColor} 10%, var(--bg-card)), var(--bg-card))`,
        }}
      >
        <div className="flex items-center justify-between">
          <h3 className="text-sm font-bold text-[var(--text-primary)]">{title}</h3>
          {isFallback && (
            <span
              className="text-xs px-2 py-0.5 rounded-full font-medium border"
              style={{
                color: "var(--accent-amber)",
                borderColor: "var(--accent-amber)",
                background: "color-mix(in srgb, var(--accent-amber) 10%, transparent)",
              }}
            >
              Demo
            </span>
          )}
        </div>
      </div>

      <div className="p-6 space-y-4">
        {loading && (
          <div className="flex items-center justify-center py-8">
            <div className="flex flex-col items-center gap-3">
              <div className="relative">
                <Loader2 className="w-6 h-6 animate-spin" style={{ color: accentColor }} />
                <div className="absolute inset-0 blur-md" style={{ color: accentColor, opacity: 0.3 }}>
                  <Loader2 className="w-6 h-6 animate-spin" />
                </div>
              </div>
              <p className="text-sm text-[var(--text-muted)]">Generating response...</p>
            </div>
          </div>
        )}

        {error && !loading && (
          <div
            className="flex items-start gap-3 p-4 rounded-lg border"
            style={{
              borderColor: "var(--accent-red)",
              background: "color-mix(in srgb, var(--accent-red) 10%, var(--bg-card))",
            }}
          >
            <AlertCircle className="w-5 h-5 flex-shrink-0 mt-0.5" style={{ color: "var(--accent-red)" }} />
            <div>
              <p className="font-medium text-sm text-[var(--text-primary)]">Error</p>
              <p className="text-xs text-[var(--text-secondary)]">{error}</p>
            </div>
          </div>
        )}

        {result && !loading && (
          <>
            <div className="relative rounded-lg border border-[var(--border)] p-4 min-h-[8rem]" style={{ background: "var(--bg-secondary)" }}>
              <p className="text-sm text-[var(--text-primary)] leading-relaxed whitespace-pre-wrap">
                {displayedText}
                {isTyping && (
                  <span className="inline-block w-0.5 h-4 ml-0.5 align-text-bottom animate-blink" style={{ background: accentColor }} />
                )}
              </p>
              {!isTyping && result.text && (
                <button
                  onClick={handleCopy}
                  className="absolute top-3 right-3 p-1.5 rounded-lg hover:bg-[var(--border)] transition-colors"
                  title="Copy response"
                >
                  {copied ? (
                    <Check className="w-3.5 h-3.5" style={{ color: "var(--accent-green)" }} />
                  ) : (
                    <Copy className="w-3.5 h-3.5 text-[var(--text-muted)]" />
                  )}
                </button>
              )}
            </div>

            <div className="grid grid-cols-3 gap-4 pt-4 border-t border-[var(--border)]">
              <div>
                <p className="text-xs text-[var(--text-muted)] font-medium">Latency</p>
                <p className="text-lg font-bold text-[var(--text-primary)] mt-1">
                  {result.latency_ms}
                  <span className="text-xs font-normal text-[var(--text-muted)] ml-1">ms</span>
                </p>
              </div>
              <div>
                <p className="text-xs text-[var(--text-muted)] font-medium">Tokens</p>
                <p className="text-lg font-bold text-[var(--text-primary)] mt-1">
                  {result.tokens_used}
                </p>
              </div>
              <div>
                <p className="text-xs text-[var(--text-muted)] font-medium">Status</p>
                <p className="text-lg font-bold mt-1 flex items-center gap-1" style={{ color: "var(--accent-green)" }}>
                  <Zap className="w-4 h-4" />
                  {isTyping ? "Streaming" : "Done"}
                </p>
              </div>
            </div>
          </>
        )}

        {!result && !loading && !error && (
          <div className="flex items-center justify-center py-8 text-[var(--text-muted)]">
            <p className="text-sm">Submit a prompt to see response here</p>
          </div>
        )}
      </div>
    </motion.div>
  );
}
