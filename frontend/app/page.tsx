"use client";

import { StatsCard } from "@/components/dashboard/StatsCard";

import { GlassCard } from "@/components/shared/GlassCard";
import { AnimatedCounter } from "@/components/shared/AnimatedCounter";
import { useModelInfo } from "@/lib/hooks/useModelInfo";
import { Cpu, HardDrive, Clock, Zap, Database, Gauge, ArrowRight, Layers, GitBranch, Brain } from "lucide-react";
import Link from "next/link";
import { motion } from "framer-motion";

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.08 },
  },
};

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0, transition: { duration: 0.5, ease: [0.25, 0.1, 0.25, 1] } },
};

export default function Dashboard() {
  const { data: modelData, isLoading } = useModelInfo();
  const model = modelData?.data;
  const trainablePercent = model?.parameter_stats?.trainable_percent;

  return (
    <motion.div
      className="space-y-8"
      variants={container}
      initial="hidden"
      animate="show"
    >
      {/* Hero Section */}
      <motion.div variants={item} className="relative overflow-hidden rounded-2xl p-8 md:p-12" style={{ background: "var(--gradient-hero)" }}>
        <div className="absolute inset-0 opacity-30">
          <div className="absolute top-10 left-10 w-72 h-72 rounded-full blur-3xl animate-float" style={{ background: "var(--accent-indigo)", opacity: 0.15 }} />
          <div className="absolute bottom-10 right-10 w-96 h-96 rounded-full blur-3xl animate-float" style={{ background: "var(--accent-purple)", opacity: 0.1, animationDelay: "1.5s" }} />
        </div>

        <div className="relative z-10">
          <motion.div
            className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium border mb-4"
            style={{ borderColor: "var(--accent-indigo)", color: "var(--accent-indigo)", background: "color-mix(in srgb, var(--accent-indigo) 10%, transparent)" }}
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2 }}
          >
            <Zap className="w-3 h-3" />
            Parameter-Efficient Fine-Tuning
          </motion.div>

          <h1 className="text-4xl md:text-5xl font-bold text-[var(--text-primary)] tracking-tight">
            PEFT{" "}
            <span className="bg-clip-text text-transparent" style={{ backgroundImage: "var(--gradient-primary)" }}>
              Showcase
            </span>
          </h1>
          <p className="text-lg text-[var(--text-secondary)] mt-3 max-w-2xl">
            LoRA Fine-Tuned CV Adapter for Llama 3 8B — domain-specific resume and career
            document generation on consumer GPUs.
          </p>

          <div className="flex items-center gap-6 mt-6">
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 rounded-full" style={{ background: "var(--accent-green)" }} />
              <span className="text-sm text-[var(--text-secondary)]">
                <AnimatedCounter value={99.9} decimals={1} suffix="%" /> parameter reduction
              </span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 rounded-full" style={{ background: "var(--accent-purple)" }} />
              <span className="text-sm text-[var(--text-secondary)]">
                <AnimatedCounter value={75} suffix="%" /> memory saved
              </span>
            </div>
          </div>
        </div>
      </motion.div>

      {/* Stats Grid */}
      <motion.div variants={item} className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <StatsCard
          label="Trainable Parameters"
          value={trainablePercent != null ? `${trainablePercent.toFixed(3)}%` : "0.085%"}
          delta="-99.9% vs full FT"
          icon={<Cpu className="w-7 h-7" />}
          trend="down"
          loading={isLoading}
        />
        <StatsCard
          label="GPU Memory Saved"
          value="~75%"
          delta="6 GB vs 24 GB full FT"
          icon={<HardDrive className="w-7 h-7" />}
          trend="down"
          loading={isLoading}
        />
        <StatsCard
          label="LoRA Rank (r)"
          value={model?.adapter_config?.r || 16}
          delta="Effective scaling: 2.0x"
          icon={<Gauge className="w-7 h-7" />}
          loading={isLoading}
        />
        <StatsCard
          label="Total Parameters"
          value={`${((model?.parameter_stats?.total_params || 8030000000) / 1e9).toFixed(1)}B`}
          delta="8B Parameter Model"
          icon={<Database className="w-7 h-7" />}
          loading={isLoading}
        />
        <StatsCard
          label="Quantization"
          value="4-bit NF4"
          delta="BFloat16 Compute"
          icon={<Zap className="w-7 h-7" />}
          loading={isLoading}
        />
        <StatsCard
          label="Training Time"
          value="~2.4h"
          delta="Single Consumer GPU"
          icon={<Clock className="w-7 h-7" />}
          loading={isLoading}
        />
      </motion.div>

      {/* Info Cards */}
      <motion.div variants={item} className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <GlassCard>
          <div className="flex items-start gap-3 mb-4">
            <div className="p-2 rounded-lg" style={{ background: "color-mix(in srgb, var(--accent-indigo) 15%, transparent)" }}>
              <Brain className="w-5 h-5" style={{ color: "var(--accent-indigo)" }} />
            </div>
            <h2 className="text-xl font-bold text-[var(--text-primary)] pt-1">What is QLoRA?</h2>
          </div>
          <p className="text-[var(--text-secondary)] leading-relaxed text-sm mb-3">
            This adapter uses LoRA (Low-Rank Adaptation) to fine-tune Llama 3 8B
            for CV and resume domain tasks. Instead of updating all 8B weights,
            small trainable matrices are injected into 7 transformer modules
            while the base model stays frozen.
          </p>
          <p className="text-[var(--text-secondary)] leading-relaxed text-sm">
            The result is a ~96MB adapter specialized for professional document
            generation, career advice, and job application optimization.
          </p>
        </GlassCard>

        <GlassCard>
          <div className="flex items-start gap-3 mb-4">
            <div className="p-2 rounded-lg" style={{ background: "color-mix(in srgb, var(--accent-green) 15%, transparent)" }}>
              <GitBranch className="w-5 h-5" style={{ color: "var(--accent-green)" }} />
            </div>
            <h2 className="text-xl font-bold text-[var(--text-primary)] pt-1">Target Modules</h2>
          </div>
          <div className="space-y-2">
            {(model?.adapter_config?.target_modules || [
              "q_proj", "k_proj", "v_proj", "o_proj",
              "gate_proj", "up_proj", "down_proj",
            ]).map((mod: string, i: number) => (
              <motion.div
                key={mod}
                className="flex items-center gap-3 p-2.5 rounded-lg border border-[var(--border)]"
                style={{ background: "var(--bg-secondary)" }}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.4 + i * 0.1 }}
              >
                <div className="w-2 h-2 rounded-full" style={{ background: "var(--accent-indigo)" }} />
                <span className="font-mono text-sm text-[var(--text-primary)]">{mod}</span>
                <span className="text-xs text-[var(--text-muted)] ml-auto">
                  {["q_proj", "k_proj", "v_proj", "o_proj"].includes(mod) ? "Attention" : "Feed-Forward"}
                </span>
              </motion.div>
            ))}
          </div>
        </GlassCard>
      </motion.div>

      {/* Navigation Cards */}
      <motion.div variants={item} className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {[
          {
            href: "/metrics",
            title: "Training Metrics",
            desc: "Loss curves, learning rates, and gradient norms from W&B",
            icon: <Layers className="w-5 h-5" />,
            gradient: "linear-gradient(135deg, var(--accent-blue), var(--accent-indigo))",
          },
          {
            href: "/playground",
            title: "Inference Playground",
            desc: "Compare base vs fine-tuned model responses side-by-side",
            icon: <Zap className="w-5 h-5" />,
            gradient: "linear-gradient(135deg, var(--accent-purple), var(--accent-indigo))",
          },
          {
            href: "/architecture",
            title: "Architecture",
            desc: "Interactive QLoRA architecture breakdown and tech specs",
            icon: <GitBranch className="w-5 h-5" />,
            gradient: "linear-gradient(135deg, var(--accent-green), var(--accent-blue))",
          },
        ].map((card) => (
          <Link key={card.href} href={card.href}>
            <motion.div
              className="relative rounded-xl p-6 text-white overflow-hidden group cursor-pointer"
              style={{ background: card.gradient }}
              whileHover={{ y: -4, scale: 1.02 }}
              transition={{ type: "spring", stiffness: 300, damping: 20 }}
            >
              <div className="absolute inset-0 bg-white opacity-0 group-hover:opacity-10 transition-opacity duration-300" />
              <div className="relative z-10">
                <div className="flex items-center justify-between mb-3">
                  {card.icon}
                  <ArrowRight className="w-4 h-4 opacity-0 group-hover:opacity-100 group-hover:translate-x-1 transition-all" />
                </div>
                <h3 className="text-lg font-bold mb-1">{card.title}</h3>
                <p className="text-sm opacity-80">{card.desc}</p>
              </div>
            </motion.div>
          </Link>
        ))}
      </motion.div>

      {/* Model Info */}
      {model && (
        <motion.div variants={item}>
          <GlassCard gradient>
            <h2 className="text-sm font-bold text-[var(--text-primary)] mb-4 uppercase tracking-wider">Model Configuration</h2>
            <dl className="grid grid-cols-2 md:grid-cols-4 gap-6 text-sm">
              {[
                { label: "Base Model", value: model.base_model || "NousResearch/Meta-Llama-3-8B-Instruct" },
                { label: "LoRA Alpha", value: model.adapter_config?.lora_alpha || 32 },
                { label: "Dropout", value: model.adapter_config?.lora_dropout || 0.05 },
                { label: "Downloads", value: (model.downloads || 0).toLocaleString() },
              ].map((field) => (
                <div key={field.label}>
                  <dt className="text-[var(--text-muted)] font-medium text-xs uppercase tracking-wider">{field.label}</dt>
                  <dd className="text-[var(--text-primary)] font-mono mt-1">{field.value}</dd>
                </div>
              ))}
            </dl>
          </GlassCard>
        </motion.div>
      )}
    </motion.div>
  );
}
