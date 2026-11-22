"use client";

import { useState } from "react";
import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
} from "recharts";
import { motion } from "framer-motion";

const sectionVariants = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: "easeOut" } },
};

export default function ArchitecturePage() {
  const [activeStep, setActiveStep] = useState(0);

  const architectureSteps = [
    {
      title: "Standard Transformer Block",
      description:
        "Full 8B parameter model (NousResearch/Meta-Llama-3-8B-Instruct) loaded normally - requires 16GB GPU VRAM",
      image: (
        <svg viewBox="0 0 400 200" className="w-full h-32">
          <rect x="50" y="30" width="300" height="140" fill="var(--bg-secondary)" stroke="var(--border)" strokeWidth="2" />
          <text x="200" y="75" textAnchor="middle" fill="var(--text-primary)" className="text-sm font-bold">
            All Weights
          </text>
          <text x="200" y="110" textAnchor="middle" fill="var(--text-secondary)" className="text-xs">
            8B Parameters (Frozen)
          </text>
        </svg>
      ),
    },
    {
      title: "4-Bit Quantization (NF4)",
      description:
        "Reduce precision from 32-bit to 4-bit using NF4 quantization - drops memory to 4GB",
      image: (
        <svg viewBox="0 0 400 200" className="w-full h-32">
          <g>
            {[0, 1, 2, 3].map((i) => (
              <rect
                key={i}
                x={50 + i * 80}
                y="30"
                width="70"
                height="140"
                fill={[
                  "var(--accent-purple)",
                  "var(--accent-indigo)",
                  "var(--bg-secondary)",
                  "var(--bg-primary)",
                ][i]}
                stroke="var(--border)"
                strokeWidth="2"
                opacity={1 - i * 0.15}
              />
            ))}
          </g>
          <text x="200" y="190" textAnchor="middle" fill="var(--text-secondary)" className="text-xs">
            4-bit NF4 Quantization
          </text>
        </svg>
      ),
    },
    {
      title: "LoRA Adapters",
      description:
        "Add small trainable LoRA adapter matrices to 7 modules (attention + feed-forward) - only 0.085% of parameters",
      image: (
        <svg viewBox="0 0 400 200" className="w-full h-32">
          <rect
            x="50"
            y="30"
            width="300"
            height="140"
            fill="var(--bg-secondary)"
            stroke="var(--border)"
            strokeWidth="2"
            opacity="0.5"
          />
          <rect
            x="80"
            y="60"
            width="240"
            height="80"
            fill="none"
            stroke="var(--accent-green)"
            strokeWidth="3"
            strokeDasharray="5,5"
          />
          <text x="200" y="105" textAnchor="middle" fill="var(--accent-green)" className="text-sm font-bold">
            LoRA Adapters (Trainable)
          </text>
        </svg>
      ),
    },
  ];

  const parameterDistribution = [
    { name: "Base Model (Frozen)", value: 8023184256, fill: "var(--text-muted)" },
    { name: "LoRA Adapters", value: 6815744, fill: "var(--accent-green)" },
  ];

  const memoryComparison = [
    { name: "Full Fine-Tuning", value: 24, fill: "var(--accent-red)" },
    { name: "QLoRA", value: 6, fill: "var(--accent-green)" },
  ];

  return (
    <div className="space-y-8">
      <motion.div
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, amount: 0.3 }}
        variants={sectionVariants}
      >
        <h1 className="text-4xl font-bold" style={{ color: "var(--text-primary)" }}>
          Architecture
        </h1>
        <p className="text-lg mt-2" style={{ color: "var(--text-secondary)" }}>
          Deep dive into the QLoRA architecture and design decisions
        </p>
      </motion.div>

      <motion.div
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, amount: 0.2 }}
        variants={sectionVariants}
        className="rounded-lg p-8"
        style={{
          backgroundColor: "var(--bg-card)",
          border: "1px solid var(--border)",
          boxShadow: "var(--shadow-sm)",
        }}
      >
        <h2 className="text-2xl font-bold mb-6" style={{ color: "var(--text-primary)" }}>
          QLoRA Architecture Breakdown
        </h2>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-8">
          {architectureSteps.map((step, index) => (
            <motion.button
              key={index}
              onClick={() => setActiveStep(index)}
              whileHover={{ scale: 1.02 }}
              className="p-4 rounded-lg transition-all text-left"
              style={{
                border: `2px solid ${activeStep === index ? "var(--accent-blue)" : "var(--border)"}`,
                backgroundColor: activeStep === index ? "var(--bg-secondary)" : "var(--bg-card)",
              }}
            >
              <div className="text-sm font-medium" style={{ color: "var(--text-primary)" }}>
                {step.title}
              </div>
              <div className="text-xs mt-1" style={{ color: "var(--text-secondary)" }}>
                Step {index + 1}
              </div>
            </motion.button>
          ))}
        </div>

        <motion.div
          key={activeStep}
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -10 }}
          className="space-y-4"
        >
          <div
            className="rounded-lg p-6"
            style={{ backgroundColor: "var(--bg-secondary)" }}
          >
            {architectureSteps[activeStep].image}
          </div>
          <p className="leading-relaxed" style={{ color: "var(--text-secondary)" }}>
            {architectureSteps[activeStep].description}
          </p>
        </motion.div>
      </motion.div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <motion.div
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, amount: 0.2 }}
          variants={sectionVariants}
          className="rounded-lg p-8"
          style={{
            backgroundColor: "var(--bg-card)",
            border: "1px solid var(--border)",
            boxShadow: "var(--shadow-sm)",
          }}
        >
          <h3 className="text-xl font-bold mb-6" style={{ color: "var(--text-primary)" }}>
            Parameter Distribution
          </h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={parameterDistribution}
                cx="50%"
                cy="50%"
                labelLine={true}
                label={({ name, percent }) =>
                  `${name} (${(percent * 100).toFixed(2)}%)`
                }
                outerRadius={80}
                fill="#8884d8"
                dataKey="value"
              >
                {parameterDistribution.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.fill} />
                ))}
              </Pie>
              <Tooltip
                formatter={(value: any) => {
                  if (value > 1e9) return (value / 1e9).toFixed(2) + "B";
                  if (value > 1e6) return (value / 1e6).toFixed(2) + "M";
                  return value.toLocaleString();
                }}
                contentStyle={{
                  backgroundColor: "var(--bg-card)",
                  border: "1px solid var(--border)",
                  borderRadius: "0.5rem",
                  color: "var(--text-primary)",
                }}
              />
            </PieChart>
          </ResponsiveContainer>
        </motion.div>

        <motion.div
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, amount: 0.2 }}
          variants={sectionVariants}
          className="rounded-lg p-8"
          style={{
            backgroundColor: "var(--bg-card)",
            border: "1px solid var(--border)",
            boxShadow: "var(--shadow-sm)",
          }}
        >
          <h3 className="text-xl font-bold mb-6" style={{ color: "var(--text-primary)" }}>
            GPU Memory Comparison
          </h3>
          <div className="space-y-4">
            {memoryComparison.map((method, idx) => (
              <div key={idx} className="space-y-2">
                <div className="flex justify-between items-center">
                  <span className="text-sm font-medium" style={{ color: "var(--text-secondary)" }}>
                    {method.name}
                  </span>
                  <span className="text-lg font-bold" style={{ color: "var(--text-primary)" }}>
                    {method.value}GB
                  </span>
                </div>
                <div
                  className="w-full rounded-full h-3 overflow-hidden"
                  style={{ backgroundColor: "var(--bg-secondary)" }}
                >
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${(method.value / 24) * 100}%` }}
                    transition={{ duration: 1, delay: idx * 0.2 }}
                    style={{ backgroundColor: method.fill }}
                    className="h-full rounded-full"
                  />
                </div>
              </div>
            ))}
          </div>
          <p className="text-sm font-medium mt-4 flex items-center gap-2" style={{ color: "var(--accent-green)" }}>
            <span>&#10003;</span>
            <span>75% Memory Reduction</span>
          </p>
        </motion.div>
      </div>

      <motion.div
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, amount: 0.2 }}
        variants={sectionVariants}
        className="rounded-lg p-8"
        style={{
          backgroundColor: "var(--bg-card)",
          border: "1px solid var(--border)",
          boxShadow: "var(--shadow-sm)",
        }}
      >
        <h2 className="text-xl font-bold mb-6" style={{ color: "var(--text-primary)" }}>
          Key Components
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="space-y-4">
            <div className="border-l-4 pl-4" style={{ borderColor: "var(--accent-purple)" }}>
              <h3 className="font-bold" style={{ color: "var(--text-primary)" }}>
                4-Bit Quantization
              </h3>
              <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
                NF4 format reduces weight precision from 32 to 4 bits, cutting
                memory requirements by 75% with minimal accuracy loss.
              </p>
            </div>
            <div className="border-l-4 pl-4" style={{ borderColor: "var(--accent-green)" }}>
              <h3 className="font-bold" style={{ color: "var(--text-primary)" }}>
                LoRA Adapters
              </h3>
              <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
                Low-rank matrices (A and B) added to 7 modules: attention projections
                (q, k, v, o) and feed-forward layers (gate, up, down). Only these are trained.
              </p>
            </div>
            <div className="border-l-4 pl-4" style={{ borderColor: "var(--accent-blue)" }}>
              <h3 className="font-bold" style={{ color: "var(--text-primary)" }}>
                Rank = 16
              </h3>
              <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
                Each adapter has rank 16, balancing expressiveness with
                parameter efficiency. Alpha=32 provides 2x scaling.
              </p>
            </div>
          </div>

          <div className="space-y-4">
            <div className="border-l-4 pl-4" style={{ borderColor: "var(--accent-amber)" }}>
              <h3 className="font-bold" style={{ color: "var(--text-primary)" }}>
                Frozen Base
              </h3>
              <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
                Base model weights remain frozen, preserving foundation model
                knowledge while enabling domain-specific adaptation.
              </p>
            </div>
            <div className="border-l-4 pl-4" style={{ borderColor: "var(--accent-red)" }}>
              <h3 className="font-bold" style={{ color: "var(--text-primary)" }}>
                BFloat16 Compute
              </h3>
              <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
                Adapter training uses BFloat16 for numerical stability and
                memory efficiency, avoiding overflow issues.
              </p>
            </div>
            <div className="border-l-4 pl-4" style={{ borderColor: "var(--accent-indigo)" }}>
              <h3 className="font-bold" style={{ color: "var(--text-primary)" }}>
                Target Modules
              </h3>
              <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
                LoRA applied to q_proj, k_proj, v_proj, o_proj (attention) and
                gate_proj, up_proj, down_proj (feed-forward) — 7 modules total.
              </p>
            </div>
          </div>
        </div>
      </motion.div>

      <motion.div
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, amount: 0.2 }}
        variants={sectionVariants}
        className="rounded-lg p-8"
        style={{
          background: "linear-gradient(to right, var(--accent-blue), var(--accent-indigo))",
          opacity: 0.95,
          border: "1px solid var(--border)",
        }}
      >
        <h2 className="text-xl font-bold mb-4 text-white">
          Why QLoRA is Revolutionary
        </h2>
        <ul className="space-y-3 text-sm text-white/90">
          <li className="flex gap-2">
            <span className="flex-shrink-0 font-bold">1.</span>
            <span>
              <strong>Democratized Fine-Tuning:</strong> Enterprise LLM
              customization now possible on consumer GPUs, reducing costs from
              $10k+ to $100-500 per run
            </span>
          </li>
          <li className="flex gap-2">
            <span className="flex-shrink-0 font-bold">2.</span>
            <span>
              <strong>Maintained Quality:</strong> Empirically achieves ~99% of
              full fine-tuning performance while using 75% less memory
            </span>
          </li>
          <li className="flex gap-2">
            <span className="flex-shrink-0 font-bold">3.</span>
            <span>
              <strong>Preserved Knowledge:</strong> Frozen base model prevents
              catastrophic forgetting and maintains general capabilities
            </span>
          </li>
          <li className="flex gap-2">
            <span className="flex-shrink-0 font-bold">4.</span>
            <span>
              <strong>Fast Experimentation:</strong> Rapid iteration on
              hyperparameters and datasets without long training cycles
            </span>
          </li>
        </ul>
      </motion.div>

      <motion.div
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, amount: 0.2 }}
        variants={sectionVariants}
        className="rounded-lg p-8"
        style={{
          backgroundColor: "var(--bg-card)",
          border: "1px solid var(--border)",
          boxShadow: "var(--shadow-sm)",
        }}
      >
        <h2 className="text-xl font-bold mb-6" style={{ color: "var(--text-primary)" }}>
          Technical Specifications
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div>
            <h3 className="font-semibold text-sm mb-3" style={{ color: "var(--text-primary)" }}>
              Model Config
            </h3>
            <dl className="space-y-2 text-sm">
              <div className="flex justify-between">
                <dt style={{ color: "var(--text-secondary)" }}>Base Model</dt>
                <dd className="font-mono" style={{ color: "var(--text-primary)" }}>Llama 3 8B Instruct</dd>
              </div>
              <div className="flex justify-between">
                <dt style={{ color: "var(--text-secondary)" }}>Quantization</dt>
                <dd className="font-mono" style={{ color: "var(--text-primary)" }}>NF4 4-bit</dd>
              </div>
              <div className="flex justify-between">
                <dt style={{ color: "var(--text-secondary)" }}>Compute Dtype</dt>
                <dd className="font-mono" style={{ color: "var(--text-primary)" }}>BFloat16</dd>
              </div>
            </dl>
          </div>

          <div>
            <h3 className="font-semibold text-sm mb-3" style={{ color: "var(--text-primary)" }}>
              LoRA Config
            </h3>
            <dl className="space-y-2 text-sm">
              <div className="flex justify-between">
                <dt style={{ color: "var(--text-secondary)" }}>Rank (r)</dt>
                <dd className="font-mono" style={{ color: "var(--text-primary)" }}>16</dd>
              </div>
              <div className="flex justify-between">
                <dt style={{ color: "var(--text-secondary)" }}>Alpha</dt>
                <dd className="font-mono" style={{ color: "var(--text-primary)" }}>32</dd>
              </div>
              <div className="flex justify-between">
                <dt style={{ color: "var(--text-secondary)" }}>Dropout</dt>
                <dd className="font-mono" style={{ color: "var(--text-primary)" }}>0.05</dd>
              </div>
            </dl>
          </div>

          <div>
            <h3 className="font-semibold text-sm mb-3" style={{ color: "var(--text-primary)" }}>
              Performance
            </h3>
            <dl className="space-y-2 text-sm">
              <div className="flex justify-between">
                <dt style={{ color: "var(--text-secondary)" }}>Training Time</dt>
                <dd className="font-mono" style={{ color: "var(--text-primary)" }}>~2.4 hours</dd>
              </div>
              <div className="flex justify-between">
                <dt style={{ color: "var(--text-secondary)" }}>GPU Memory</dt>
                <dd className="font-mono" style={{ color: "var(--text-primary)" }}>6.2 GB</dd>
              </div>
              <div className="flex justify-between">
                <dt style={{ color: "var(--text-secondary)" }}>Inference</dt>
                <dd className="font-mono" style={{ color: "var(--text-primary)" }}>~1 sec/token</dd>
              </div>
            </dl>
          </div>
        </div>
      </motion.div>
    </div>
  );
}
