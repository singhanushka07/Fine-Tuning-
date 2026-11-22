"use client";

import { motion } from "framer-motion";
import { useTrainingMetrics } from "@/lib/hooks/useTrainingMetrics";
import { TrainingChart } from "@/components/metrics/TrainingChart";

import { StatsCard } from "@/components/dashboard/StatsCard";
import { GlassCard } from "@/components/shared/GlassCard";
import { ChartSkeleton, Skeleton } from "@/components/shared/SkeletonLoader";
import {
  TrendingDown,
  Activity,
  BarChart3,
  Settings2,
  Lightbulb,
  CheckCircle2,
} from "lucide-react";

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { staggerChildren: 0.1 },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: "easeOut" } },
};

export default function MetricsPage() {
  const { data: metricsData, isLoading } = useTrainingMetrics();
  const metrics = metricsData?.data;


  const totalSteps = metrics?.summary?.total_steps ?? 0;
  const progressPercent = Math.min((totalSteps / 500) * 100, 100);

  if (isLoading) {
    return (
      <div className="space-y-8">
        {/* Header skeleton */}
        <div className="space-y-3">
          <Skeleton variant="text" className="h-10 w-72" />
          <Skeleton variant="text" className="h-5 w-96" />
        </div>

        {/* Progress bar skeleton */}
        <div className="space-y-2">
          <Skeleton variant="text" className="h-4 w-48" />
          <Skeleton variant="text" className="h-3 w-full" />
        </div>

        {/* Stats skeleton */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {[1, 2, 3].map((i) => (
            <Skeleton key={i} variant="card" />
          ))}
        </div>

        {/* Charts skeleton */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <ChartSkeleton />
          <ChartSkeleton />
        </div>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <ChartSkeleton />
          <Skeleton variant="card" className="h-[340px]" />
        </div>
      </div>
    );
  }

  return (
    <motion.div
      className="space-y-8"
      variants={containerVariants}
      initial="hidden"
      animate="visible"
    >
      {/* Page header */}
      <motion.div variants={itemVariants}>
        <h1
          className="text-4xl font-bold"
          style={{ color: "var(--text-primary)" }}
        >
          Training Metrics
        </h1>
        <p
          className="text-lg mt-2"
          style={{ color: "var(--text-secondary)" }}
        >
          Training progress and performance tracking from Weights &amp; Biases
        </p>
      </motion.div>

      {/* Epoch progress bar */}
      <motion.div
        variants={itemVariants}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-50px" }}
      >
        <GlassCard hover={false} padding="p-5">
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center gap-2">
              <Activity
                className="w-5 h-5"
                style={{ color: "var(--accent-blue)" }}
              />
              <span
                className="text-sm font-semibold"
                style={{ color: "var(--text-primary)" }}
              >
                Training Progress
              </span>
            </div>
            <span
              className="text-sm font-mono font-medium"
              style={{ color: "var(--text-secondary)" }}
            >
              {totalSteps} / 500 steps ({progressPercent.toFixed(0)}%)
            </span>
          </div>
          <div
            className="w-full h-3 rounded-full overflow-hidden"
            style={{ background: "var(--bg-secondary)" }}
          >
            <motion.div
              className="h-full rounded-full"
              style={{
                background: `linear-gradient(90deg, var(--accent-blue), var(--accent-indigo))`,
              }}
              initial={{ width: 0 }}
              animate={{ width: `${progressPercent}%` }}
              transition={{ duration: 1.2, ease: "easeOut", delay: 0.3 }}
            />
          </div>
          <p
            className="text-xs mt-2"
            style={{ color: "var(--text-muted)" }}
          >
            {(totalSteps / 100).toFixed(1)} epochs completed
          </p>
        </GlassCard>
      </motion.div>

      {/* Stats cards */}
      {metrics?.summary && (
        <motion.div
          className="grid grid-cols-1 md:grid-cols-3 gap-6"
          variants={itemVariants}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-50px" }}
        >
          <StatsCard
            label="Best Eval Loss"
            value={metrics.summary.best_eval_loss.toFixed(4)}
            icon={<TrendingDown className="w-8 h-8" />}
            trend="down"
          />
          <StatsCard
            label="Final Train Loss"
            value={metrics.summary.final_train_loss.toFixed(4)}
            icon={<TrendingDown className="w-8 h-8" />}
            trend="down"
          />
          <StatsCard
            label="Total Steps"
            value={metrics.summary.total_steps}
            delta={`${(metrics.summary.total_steps / 100).toFixed(1)} epochs`}
            icon={<BarChart3 className="w-8 h-8" />}
          />
        </motion.div>
      )}

      {/* Charts row 1 */}
      <motion.div
        className="grid grid-cols-1 lg:grid-cols-2 gap-6"
        variants={itemVariants}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-50px" }}
      >
        <TrainingChart
          data={metrics?.metrics || []}
          title="Training Loss"
          lines={[
            { key: "train_loss", color: "#3b82f6", name: "Train Loss" },
            { key: "eval_loss", color: "#ef4444", name: "Eval Loss" },
          ]}
          yAxisLabel="Loss"
          areaFill={true}
        />

        <TrainingChart
          data={metrics?.metrics || []}
          title="Learning Rate Schedule"
          lines={[
            { key: "learning_rate", color: "#10b981", name: "Learning Rate" },
          ]}
          yAxisLabel="LR"
        />
      </motion.div>

      {/* Charts row 2 + Training Configuration */}
      <motion.div
        className="grid grid-cols-1 lg:grid-cols-2 gap-6"
        variants={itemVariants}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-50px" }}
      >
        <TrainingChart
          data={metrics?.metrics || []}
          title="Gradient Norm"
          lines={[{ key: "grad_norm", color: "#f59e0b", name: "Grad Norm" }]}
          yAxisLabel="Norm"
        />

        <GlassCard hover={true} gradient={false}>
          <div className="flex items-center gap-2 mb-4">
            <Settings2
              className="w-5 h-5"
              style={{ color: "var(--accent-indigo)" }}
            />
            <h3
              className="text-lg font-bold"
              style={{ color: "var(--text-primary)" }}
            >
              Training Configuration
            </h3>
          </div>
          <dl className="space-y-4 text-sm">
            <div className="flex justify-between">
              <dt style={{ color: "var(--text-secondary)" }}>Learning Rate</dt>
              <dd
                className="font-mono"
                style={{ color: "var(--text-primary)" }}
              >
                2e-4 &rarr; 1e-5
              </dd>
            </div>
            <div className="flex justify-between">
              <dt style={{ color: "var(--text-secondary)" }}>Warmup Steps</dt>
              <dd
                className="font-mono"
                style={{ color: "var(--text-primary)" }}
              >
                50
              </dd>
            </div>
            <div className="flex justify-between">
              <dt style={{ color: "var(--text-secondary)" }}>Batch Size</dt>
              <dd
                className="font-mono"
                style={{ color: "var(--text-primary)" }}
              >
                4 (Grad Accum: 4)
              </dd>
            </div>
            <div className="flex justify-between">
              <dt style={{ color: "var(--text-secondary)" }}>Optimizer</dt>
              <dd
                className="font-mono"
                style={{ color: "var(--text-primary)" }}
              >
                AdamW
              </dd>
            </div>
            <div
              className="flex justify-between border-t pt-4"
              style={{ borderColor: "var(--border)" }}
            >
              <dt
                className="font-semibold"
                style={{ color: "var(--text-secondary)" }}
              >
                Convergence
              </dt>
              <dd className="font-mono font-semibold flex items-center gap-1.5">
                <CheckCircle2
                  className="w-4 h-4"
                  style={{ color: "var(--accent-green)" }}
                />
                <span style={{ color: "var(--accent-green)" }}>Stable</span>
              </dd>
            </div>
          </dl>
        </GlassCard>
      </motion.div>

      {/* Key Insights */}
      <motion.div
        variants={itemVariants}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-50px" }}
      >
        <div
          className="rounded-xl border p-6"
          style={{
            background:
              "linear-gradient(135deg, var(--bg-card), var(--bg-secondary))",
            borderColor: "var(--border)",
            boxShadow: "var(--shadow-sm)",
          }}
        >
          <div className="flex items-center gap-2 mb-3">
            <Lightbulb
              className="w-5 h-5"
              style={{ color: "var(--accent-blue)" }}
            />
            <h3
              className="text-lg font-bold"
              style={{ color: "var(--text-primary)" }}
            >
              Key Insights
            </h3>
          </div>
          <ul className="space-y-3 text-sm">
            {[
              "Eval loss converged smoothly after 300 steps, indicating good generalization",
              "Learning rate schedule applied optimal warmup and cosine decay",
              "Gradient norms stayed stable throughout training, no gradient explosion/vanishing",
              "Training completed in ~2.4 hours on single 24GB GPU with 4-bit quantization",
            ].map((insight, idx) => (
              <motion.li
                key={idx}
                className="flex items-start gap-2"
                initial={{ opacity: 0, x: -10 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ delay: idx * 0.1, duration: 0.3 }}
              >
                <CheckCircle2
                  className="w-4 h-4 mt-0.5 flex-shrink-0"
                  style={{ color: "var(--accent-green)" }}
                />
                <span style={{ color: "var(--text-secondary)" }}>
                  {insight}
                </span>
              </motion.li>
            ))}
          </ul>
        </div>
      </motion.div>
    </motion.div>
  );
}
