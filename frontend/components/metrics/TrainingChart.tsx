"use client";

import {
  AreaChart,
  Area,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import { MetricPoint } from "@/lib/types";
import { motion } from "framer-motion";

interface TrainingChartProps {
  data: MetricPoint[];
  title: string;
  lines: {
    key: string;
    color: string;
    name: string;
  }[];
  yAxisLabel?: string;
  areaFill?: boolean;
}

export function TrainingChart({
  data,
  title,
  lines,
  yAxisLabel,
  areaFill = false,
}: TrainingChartProps) {
  const Chart = areaFill ? AreaChart : LineChart;

  return (
    <motion.div
      className="rounded-xl border border-[var(--border)] p-6 backdrop-blur-md"
      style={{ background: "var(--bg-card)" }}
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-50px" }}
      transition={{ duration: 0.5 }}
    >
      <h3 className="text-lg font-bold text-[var(--text-primary)] mb-4">{title}</h3>
      <ResponsiveContainer width="100%" height={300}>
        <Chart data={data}>
          <defs>
            {lines.map((line) => (
              <linearGradient key={`grad-${line.key}`} id={`grad-${line.key}`} x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor={line.color} stopOpacity={0.3} />
                <stop offset="95%" stopColor={line.color} stopOpacity={0} />
              </linearGradient>
            ))}
          </defs>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--chart-grid)" opacity={0.5} />
          <XAxis
            dataKey="step"
            stroke="var(--chart-text)"
            style={{ fontSize: "11px" }}
            tickLine={false}
            axisLine={false}
          />
          <YAxis
            stroke="var(--chart-text)"
            style={{ fontSize: "11px" }}
            tickLine={false}
            axisLine={false}
            label={yAxisLabel ? { value: yAxisLabel, angle: -90, position: "insideLeft", style: { fill: "var(--chart-text)", fontSize: "11px" } } : undefined}
          />
          <Tooltip
            contentStyle={{
              backgroundColor: "var(--chart-tooltip-bg)",
              border: "1px solid var(--chart-tooltip-border)",
              borderRadius: "8px",
              boxShadow: "var(--shadow-md)",
              color: "var(--text-primary)",
            }}
            formatter={(value: any) =>
              typeof value === "number" ? value.toFixed(4) : value
            }
            labelStyle={{ color: "var(--text-secondary)" }}
          />
          <Legend
            wrapperStyle={{ color: "var(--text-secondary)", fontSize: "12px" }}
          />
          {lines.map((line) =>
            areaFill ? (
              <Area
                key={line.key}
                type="monotone"
                dataKey={line.key}
                stroke={line.color}
                fill={`url(#grad-${line.key})`}
                name={line.name}
                dot={false}
                isAnimationActive={true}
                strokeWidth={2}
                animationDuration={1500}
              />
            ) : (
              <Line
                key={line.key}
                type="monotone"
                dataKey={line.key}
                stroke={line.color}
                name={line.name}
                dot={false}
                isAnimationActive={true}
                strokeWidth={2}
                animationDuration={1500}
              />
            )
          )}
        </Chart>
      </ResponsiveContainer>
    </motion.div>
  );
}
