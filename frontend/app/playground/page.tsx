"use client";

import { useState, useEffect, useRef } from "react";
import { motion } from "framer-motion";
import { useInference } from "@/lib/hooks/useInference";
import { InferencePanel } from "@/components/playground/InferencePanel";

import { GlassCard } from "@/components/shared/GlassCard";
import { Send, Sparkles, Zap } from "lucide-react";

const PROMPT_CATEGORIES = [
  {
    category: "Resume",
    prompts: [
      "How do I write a strong professional resume?",
      "What makes a great CV summary statement?",
    ],
  },
  {
    category: "Career",
    prompts: [
      "How should I prepare for a technical interview?",
      "How do I write an effective cover letter?",
    ],
  },
  {
    category: "Skills",
    prompts: [
      "How should I list technical skills on my CV?",
      "How do I describe work experience with impact?",
    ],
  },
];

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
    },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.4, ease: "easeOut" } },
};

export default function PlaygroundPage() {
  const [prompt, setPrompt] = useState("");
  const [temperature, setTemperature] = useState(0.7);
  const [maxTokens, setMaxTokens] = useState(256);
  const [activeCategory, setActiveCategory] = useState("Resume");
  const { mutate, data, isPending } = useInference();
  const formRef = useRef<HTMLFormElement>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (prompt.trim() && !isPending) {
      mutate({ prompt: prompt.trim() });
    }
  };

  const handleQuickPrompt = (text: string) => {
    setPrompt(text);
    mutate({ prompt: text });
  };

  // Ctrl+Enter keyboard shortcut to submit
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.ctrlKey && e.key === "Enter") {
        e.preventDefault();
        if (prompt.trim() && !isPending) {
          mutate({ prompt: prompt.trim() });
        }
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [prompt, isPending, mutate]);

  const activePrompts =
    PROMPT_CATEGORIES.find((c) => c.category === activeCategory)?.prompts ?? [];

  // Compute latency bar widths for comparison chart
  const maxLatency =
    data?.base && data?.finetuned
      ? Math.max(data.base.latency_ms, data.finetuned.latency_ms, 1)
      : 1;
  const baseLatencyPct =
    data?.base ? (data.base.latency_ms / maxLatency) * 100 : 0;
  const finetunedLatencyPct =
    data?.finetuned ? (data.finetuned.latency_ms / maxLatency) * 100 : 0;

  return (
    <motion.div
      variants={containerVariants}
      initial="hidden"
      animate="visible"
      style={{ display: "flex", flexDirection: "column", gap: "2rem" }}
    >
      {/* Header */}
      <motion.div variants={itemVariants}>
        <h1
          style={{
            fontSize: "2.25rem",
            fontWeight: 700,
            color: "var(--text-primary)",
            margin: 0,
          }}
        >
          Inference Playground
        </h1>
        <p
          style={{
            fontSize: "1.125rem",
            color: "var(--text-secondary)",
            marginTop: "0.5rem",
          }}
        >
          Compare base and fine-tuned model responses side-by-side
        </p>
      </motion.div>

      {/* Form */}
      <motion.form
        ref={formRef}
        onSubmit={handleSubmit}
        variants={itemVariants}
        style={{ display: "flex", flexDirection: "column", gap: "1rem" }}
      >
        {/* Textarea */}
        <div>
          <label
            style={{
              display: "block",
              fontSize: "0.875rem",
              fontWeight: 500,
              color: "var(--text-secondary)",
              marginBottom: "0.5rem",
            }}
          >
            Enter Prompt
          </label>
          <div style={{ position: "relative" }}>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Type your prompt here..."
              maxLength={500}
              rows={4}
              style={{
                width: "100%",
                padding: "0.75rem 1rem",
                backgroundColor: "var(--bg-input)",
                border: "1px solid var(--border)",
                borderRadius: "0.5rem",
                color: "var(--text-primary)",
                fontSize: "0.95rem",
                resize: "none",
                outline: "none",
                fontFamily: "inherit",
                boxSizing: "border-box",
                transition: "border-color 0.2s",
              }}
              onFocus={(e) =>
                (e.currentTarget.style.borderColor = "var(--accent-blue)")
              }
              onBlur={(e) =>
                (e.currentTarget.style.borderColor = "var(--border)")
              }
            />
            <div
              style={{
                position: "absolute",
                bottom: "0.5rem",
                right: "0.75rem",
                fontSize: "0.75rem",
                color: "var(--text-muted)",
              }}
            >
              {prompt.length}/500
            </div>
          </div>
        </div>

        {/* Category Tabs */}
        <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap" }}>
          {PROMPT_CATEGORIES.map(({ category }) => (
            <button
              key={category}
              type="button"
              onClick={() => setActiveCategory(category)}
              style={{
                padding: "0.375rem 0.875rem",
                fontSize: "0.8125rem",
                fontWeight: activeCategory === category ? 600 : 400,
                borderRadius: "9999px",
                border: "1px solid",
                borderColor:
                  activeCategory === category
                    ? "var(--accent-indigo)"
                    : "var(--border)",
                backgroundColor:
                  activeCategory === category
                    ? "var(--accent-indigo)"
                    : "var(--bg-secondary)",
                color:
                  activeCategory === category
                    ? "#ffffff"
                    : "var(--text-secondary)",
                cursor: "pointer",
                transition: "all 0.2s",
              }}
            >
              {category}
            </button>
          ))}
        </div>

        {/* Example Prompts */}
        <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap" }}>
          {activePrompts.map((examplePrompt) => (
            <button
              key={examplePrompt}
              type="button"
              onClick={() => handleQuickPrompt(examplePrompt)}
              style={{
                padding: "0.375rem 0.75rem",
                fontSize: "0.8125rem",
                backgroundColor: "var(--bg-secondary)",
                color: "var(--text-secondary)",
                borderRadius: "9999px",
                border: "1px solid var(--border)",
                cursor: "pointer",
                transition: "all 0.2s",
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.borderColor = "var(--border-hover)";
                e.currentTarget.style.color = "var(--text-primary)";
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.borderColor = "var(--border)";
                e.currentTarget.style.color = "var(--text-secondary)";
              }}
            >
              {examplePrompt.length > 40
                ? examplePrompt.substring(0, 40) + "..."
                : examplePrompt}
            </button>
          ))}
        </div>

        {/* Parameter Sliders Row */}
        <div
          style={{
            display: "flex",
            gap: "1.5rem",
            alignItems: "center",
            flexWrap: "wrap",
            padding: "0.75rem 1rem",
            backgroundColor: "var(--bg-secondary)",
            borderRadius: "0.5rem",
            border: "1px solid var(--border)",
          }}
        >
          {/* Temperature Slider */}
          <div style={{ flex: 1, minWidth: "180px" }}>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                marginBottom: "0.375rem",
              }}
            >
              <label
                style={{
                  fontSize: "0.8125rem",
                  fontWeight: 500,
                  color: "var(--text-secondary)",
                }}
              >
                Temperature
              </label>
              <span
                style={{
                  fontSize: "0.8125rem",
                  fontWeight: 600,
                  color: "var(--accent-blue)",
                  fontFamily: "monospace",
                }}
              >
                {temperature.toFixed(1)}
              </span>
            </div>
            <input
              type="range"
              min={0.1}
              max={1.0}
              step={0.1}
              value={temperature}
              onChange={(e) => setTemperature(parseFloat(e.target.value))}
              style={{
                width: "100%",
                accentColor: "var(--accent-blue)",
                cursor: "pointer",
              }}
            />
          </div>

          {/* Max Tokens Slider */}
          <div style={{ flex: 1, minWidth: "180px" }}>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                marginBottom: "0.375rem",
              }}
            >
              <label
                style={{
                  fontSize: "0.8125rem",
                  fontWeight: 500,
                  color: "var(--text-secondary)",
                }}
              >
                Max Tokens
              </label>
              <span
                style={{
                  fontSize: "0.8125rem",
                  fontWeight: 600,
                  color: "var(--accent-purple)",
                  fontFamily: "monospace",
                }}
              >
                {maxTokens}
              </span>
            </div>
            <input
              type="range"
              min={64}
              max={512}
              step={16}
              value={maxTokens}
              onChange={(e) => setMaxTokens(parseInt(e.target.value, 10))}
              style={{
                width: "100%",
                accentColor: "var(--accent-purple)",
                cursor: "pointer",
              }}
            />
          </div>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={!prompt.trim() || isPending}
          style={{
            width: "100%",
            padding: "0.75rem 1rem",
            backgroundColor:
              !prompt.trim() || isPending
                ? "var(--bg-secondary)"
                : "var(--accent-blue)",
            color:
              !prompt.trim() || isPending
                ? "var(--text-muted)"
                : "#ffffff",
            fontWeight: 600,
            fontSize: "0.95rem",
            borderRadius: "0.5rem",
            border: "none",
            cursor:
              !prompt.trim() || isPending ? "not-allowed" : "pointer",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            gap: "0.5rem",
            transition: "all 0.2s",
            fontFamily: "inherit",
            boxShadow: "var(--shadow-sm)",
          }}
        >
          <Send style={{ width: "1.25rem", height: "1.25rem" }} />
          {isPending ? "Generating..." : "Compare Models"}
          <span
            style={{
              fontSize: "0.75rem",
              opacity: 0.7,
              marginLeft: "0.25rem",
            }}
          >
            Ctrl+Enter
          </span>
        </button>
      </motion.form>

      {/* Results */}
      {(data || isPending) && (
        <motion.div variants={itemVariants}>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: "0.5rem",
              marginBottom: "0.5rem",
            }}
          >
            <Sparkles
              style={{
                width: "1.25rem",
                height: "1.25rem",
                color: "var(--accent-purple)",
              }}
            />
            <h2
              style={{
                fontSize: "1.125rem",
                fontWeight: 700,
                color: "var(--text-primary)",
                margin: 0,
              }}
            >
              Results
            </h2>
          </div>
          <p
            style={{
              fontSize: "0.875rem",
              color: "var(--text-secondary)",
              marginBottom: "1rem",
            }}
          >
            Prompt: {data?.prompt || prompt}
          </p>

          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fit, minmax(min(100%, 400px), 1fr))",
              gap: "1.5rem",
            }}
          >
            <InferencePanel
              title="Base Model (NousResearch/Llama-3-8B-Instruct)"
              result={data?.base}
              loading={isPending}
              accentColor="var(--accent-blue)"
              typingSpeed={20}
            />
            <InferencePanel
              title="Fine-Tuned CV Adapter (Anushka69/llama3-finetuned-cv-adapter)"
              result={data?.finetuned}
              loading={isPending}
              accentColor="var(--accent-purple)"
              typingSpeed={12}
            />
          </div>

          {/* Comparison Insights with animated bar chart */}
          {data?.base && data?.finetuned && (
            <div style={{ marginTop: "1.5rem" }}>
              <GlassCard>
                <div style={{ padding: "1.5rem" }}>
                  <div
                    style={{
                      display: "flex",
                      alignItems: "center",
                      gap: "0.5rem",
                      marginBottom: "1rem",
                    }}
                  >
                    <Zap
                      style={{
                        width: "1.125rem",
                        height: "1.125rem",
                        color: "var(--accent-indigo)",
                      }}
                    />
                    <h3
                      style={{
                        fontWeight: 700,
                        color: "var(--text-primary)",
                        margin: 0,
                        fontSize: "1rem",
                      }}
                    >
                      Comparison Insights
                    </h3>
                  </div>

                  {/* Latency Bar Chart */}
                  <div
                    style={{
                      display: "flex",
                      flexDirection: "column",
                      gap: "0.75rem",
                    }}
                  >
                    {/* Base latency bar */}
                    <div>
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          alignItems: "center",
                          marginBottom: "0.25rem",
                        }}
                      >
                        <span
                          style={{
                            fontSize: "0.8125rem",
                            color: "var(--text-secondary)",
                          }}
                        >
                          Base Model Latency
                        </span>
                        <span
                          style={{
                            fontSize: "0.8125rem",
                            fontFamily: "monospace",
                            fontWeight: 600,
                            color: "var(--accent-blue)",
                          }}
                        >
                          {data.base.latency_ms}ms
                        </span>
                      </div>
                      <div
                        style={{
                          width: "100%",
                          height: "0.5rem",
                          backgroundColor: "var(--bg-secondary)",
                          borderRadius: "9999px",
                          overflow: "hidden",
                        }}
                      >
                        <div
                          style={{
                            width: `${baseLatencyPct}%`,
                            height: "100%",
                            backgroundColor: "var(--accent-blue)",
                            borderRadius: "9999px",
                            transition: "width 0.8s ease-out",
                          }}
                        />
                      </div>
                    </div>

                    {/* Fine-tuned latency bar */}
                    <div>
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          alignItems: "center",
                          marginBottom: "0.25rem",
                        }}
                      >
                        <span
                          style={{
                            fontSize: "0.8125rem",
                            color: "var(--text-secondary)",
                          }}
                        >
                          Fine-Tuned Latency
                        </span>
                        <span
                          style={{
                            fontSize: "0.8125rem",
                            fontFamily: "monospace",
                            fontWeight: 600,
                            color: "var(--accent-purple)",
                          }}
                        >
                          {data.finetuned.latency_ms}ms
                        </span>
                      </div>
                      <div
                        style={{
                          width: "100%",
                          height: "0.5rem",
                          backgroundColor: "var(--bg-secondary)",
                          borderRadius: "9999px",
                          overflow: "hidden",
                        }}
                      >
                        <div
                          style={{
                            width: `${finetunedLatencyPct}%`,
                            height: "100%",
                            backgroundColor: "var(--accent-purple)",
                            borderRadius: "9999px",
                            transition: "width 0.8s ease-out",
                          }}
                        />
                      </div>
                    </div>

                    {/* Token difference */}
                    <div
                      style={{
                        display: "flex",
                        justifyContent: "space-between",
                        alignItems: "center",
                        paddingTop: "0.5rem",
                        borderTop: "1px solid var(--border)",
                      }}
                    >
                      <span
                        style={{
                          fontSize: "0.8125rem",
                          color: "var(--text-secondary)",
                        }}
                      >
                        Response Length Difference
                      </span>
                      <span
                        style={{
                          fontSize: "0.8125rem",
                          fontFamily: "monospace",
                          fontWeight: 600,
                          color: "var(--accent-indigo)",
                        }}
                      >
                        {Math.abs(
                          data.finetuned.tokens_used - data.base.tokens_used
                        )}{" "}
                        tokens
                      </span>
                    </div>
                  </div>
                </div>
              </GlassCard>
            </div>
          )}
        </motion.div>
      )}

      {/* About Fine-Tuning Info Card */}
      <motion.div
        variants={itemVariants}
        style={{
          background:
            "linear-gradient(135deg, var(--bg-secondary), var(--bg-card))",
          borderRadius: "0.5rem",
          border: "1px solid var(--border)",
          padding: "1.5rem",
          boxShadow: "var(--shadow-sm)",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: "0.5rem",
            marginBottom: "0.5rem",
          }}
        >
          <Sparkles
            style={{
              width: "1rem",
              height: "1rem",
              color: "var(--accent-purple)",
            }}
          />
          <h3
            style={{
              fontWeight: 700,
              color: "var(--text-primary)",
              margin: 0,
            }}
          >
            About Fine-Tuning
          </h3>
        </div>
        <p
          style={{
            fontSize: "0.875rem",
            color: "var(--text-secondary)",
            lineHeight: 1.7,
            margin: 0,
          }}
        >
          The fine-tuned model (Anushka69/llama3-finetuned-cv-adapter) has been
          adapted using LoRA on CV and resume domain data. Notice how it provides
          more targeted, professionally-oriented responses compared to the base
          model, with expertise in resume writing, career advice, and job applications.
        </p>
      </motion.div>
    </motion.div>
  );
}
