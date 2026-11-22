"use client";

import { ReactNode } from "react";
import { TrendingDown, TrendingUp } from "lucide-react";
import { motion } from "framer-motion";
import { Skeleton } from "@/components/shared/SkeletonLoader";

interface StatsCardProps {
  label: string;
  value: string | number;
  delta?: string;
  icon?: ReactNode;
  trend?: "up" | "down" | "neutral";
  loading?: boolean;
}

export function StatsCard({
  label,
  value,
  delta,
  icon,
  trend,
  loading,
}: StatsCardProps) {
  return (
    <motion.div
      className="rounded-xl border border-[var(--border)] p-6 backdrop-blur-md transition-all duration-300 hover:border-[var(--border-hover)] hover:shadow-[var(--shadow-md)] group"
      style={{ background: "var(--bg-card)" }}
      whileHover={{ y: -2 }}
      transition={{ type: "spring", stiffness: 300, damping: 30 }}
    >
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <p className="text-sm font-medium text-[var(--text-muted)]">{label}</p>
          {loading ? (
            <div className="mt-2 space-y-2">
              <Skeleton variant="text" className="h-8 w-28" />
              <Skeleton variant="text" className="h-3 w-36" />
            </div>
          ) : (
            <>
              <p className="text-3xl font-bold text-[var(--text-primary)] mt-2">
                {value}
              </p>
              {delta && (
                <p className="text-sm text-[var(--text-muted)] mt-2 flex items-center gap-1">
                  {trend === "down" && (
                    <TrendingDown className="w-4 h-4" style={{ color: "var(--accent-red)" }} />
                  )}
                  {trend === "up" && (
                    <TrendingUp className="w-4 h-4" style={{ color: "var(--accent-green)" }} />
                  )}
                  {delta}
                </p>
              )}
            </>
          )}
        </div>
        {icon && (
          <div
            className="transition-transform group-hover:scale-110"
            style={{ color: "var(--accent-indigo)" }}
          >
            {icon}
          </div>
        )}
      </div>
    </motion.div>
  );
}
