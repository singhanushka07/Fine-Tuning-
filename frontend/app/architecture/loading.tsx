import { Skeleton } from "@/components/shared/SkeletonLoader";

export default function ArchitectureLoading() {
  return (
    <div className="space-y-8">
      <div className="space-y-2">
        <div className="h-8 w-48 rounded bg-[var(--border)]" />
        <div className="h-5 w-80 rounded bg-[var(--border)]" />
      </div>
      <div className="rounded-xl border border-[var(--border)] p-8 space-y-6" style={{ background: "var(--bg-card)" }}>
        <Skeleton variant="text" className="h-6 w-64" />
        <div className="grid grid-cols-3 gap-4">
          {Array.from({ length: 3 }).map((_, i) => (
            <Skeleton key={i} variant="card" className="h-16" />
          ))}
        </div>
        <Skeleton variant="chart" />
      </div>
    </div>
  );
}
