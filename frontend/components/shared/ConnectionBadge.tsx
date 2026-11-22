"use client";

interface ConnectionBadgeProps {
  status: "live" | "degraded" | "down";
  label: string;
}

export function ConnectionBadge({ status, label }: ConnectionBadgeProps) {
  const dotColor = {
    live: "var(--accent-green)",
    degraded: "var(--accent-amber)",
    down: "var(--accent-red)",
  };

  return (
    <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium border border-[var(--border)] bg-[var(--bg-card)]">
      <div className="relative flex items-center justify-center">
        <div
          className="w-1.5 h-1.5 rounded-full"
          style={{ background: dotColor[status] }}
        />
        {status === "live" && (
          <div
            className="absolute w-1.5 h-1.5 rounded-full animate-ping"
            style={{ background: dotColor[status], opacity: 0.5 }}
          />
        )}
      </div>
      <span className="text-[var(--text-muted)]">{label}</span>
    </div>
  );
}
