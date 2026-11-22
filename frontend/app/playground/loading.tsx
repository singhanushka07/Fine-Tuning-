import { Skeleton } from "@/components/shared/SkeletonLoader";

export default function PlaygroundLoading() {
  return (
    <div className="space-y-8">
      <div className="space-y-2">
        <div className="h-8 w-64 rounded bg-[var(--border)]" />
        <div className="h-5 w-96 rounded bg-[var(--border)]" />
      </div>
      <div className="rounded-xl border border-[var(--border)] p-6 space-y-4" style={{ background: "var(--bg-card)" }}>
        <Skeleton variant="text" className="h-4 w-24" />
        <Skeleton variant="card" className="h-28" />
        <div className="flex gap-2">
          {Array.from({ length: 3 }).map((_, i) => (
            <Skeleton key={i} variant="text" className="h-8 w-24 rounded-full" />
          ))}
        </div>
        <Skeleton variant="text" className="h-12 rounded-lg" />
      </div>
    </div>
  );
}
