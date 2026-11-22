"use client";

interface SkeletonProps {
  variant?: "text" | "card" | "chart" | "circle";
  className?: string;
  width?: string;
  height?: string;
}

export function Skeleton({
  variant = "text",
  className = "",
  width,
  height,
}: SkeletonProps) {
  const base = "relative overflow-hidden rounded bg-[var(--border)]";

  const variants = {
    text: "h-4 w-full rounded",
    card: "h-40 w-full rounded-xl",
    chart: "h-64 w-full rounded-xl",
    circle: "h-10 w-10 rounded-full",
  };

  return (
    <div
      className={`${base} ${variants[variant]} ${className}`}
      style={{ width, height }}
    >
      <div className="absolute inset-0 animate-shimmer bg-[image:var(--gradient-shimmer)]" />
    </div>
  );
}

export function StatsCardSkeleton() {
  return (
    <div className="rounded-xl border bg-[var(--bg-card)] border-[var(--border)] p-6 space-y-3">
      <Skeleton variant="text" className="h-3 w-24" />
      <Skeleton variant="text" className="h-8 w-32" />
      <Skeleton variant="text" className="h-3 w-40" />
    </div>
  );
}

export function ChartSkeleton() {
  return (
    <div className="rounded-xl border bg-[var(--bg-card)] border-[var(--border)] p-6 space-y-4">
      <Skeleton variant="text" className="h-5 w-40" />
      <Skeleton variant="chart" />
    </div>
  );
}
