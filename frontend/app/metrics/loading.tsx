import { StatsCardSkeleton, ChartSkeleton } from "@/components/shared/SkeletonLoader";

export default function MetricsLoading() {
  return (
    <div className="space-y-8">
      <div className="space-y-2">
        <div className="h-8 w-64 rounded bg-[var(--border)]" />
        <div className="h-5 w-96 rounded bg-[var(--border)]" />
      </div>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {Array.from({ length: 3 }).map((_, i) => (
          <StatsCardSkeleton key={i} />
        ))}
      </div>
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <ChartSkeleton />
        <ChartSkeleton />
      </div>
    </div>
  );
}
