import { StatsCardSkeleton } from "@/components/shared/SkeletonLoader";

export default function Loading() {
  return (
    <div className="space-y-8 animate-pulse">
      <div className="rounded-2xl p-8 md:p-12" style={{ background: "var(--bg-secondary)" }}>
        <div className="h-4 w-48 rounded bg-[var(--border)] mb-4" />
        <div className="h-10 w-80 rounded bg-[var(--border)] mb-3" />
        <div className="h-5 w-96 rounded bg-[var(--border)]" />
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {Array.from({ length: 6 }).map((_, i) => (
          <StatsCardSkeleton key={i} />
        ))}
      </div>
    </div>
  );
}
