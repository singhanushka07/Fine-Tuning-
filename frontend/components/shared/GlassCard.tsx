"use client";

import { motion, HTMLMotionProps } from "framer-motion";
import { ReactNode } from "react";

interface GlassCardProps extends Omit<HTMLMotionProps<"div">, "children"> {
  children: ReactNode;
  className?: string;
  hover?: boolean;
  gradient?: boolean;
  padding?: string;
}

export function GlassCard({
  children,
  className = "",
  hover = true,
  gradient = false,
  padding = "p-6",
  ...motionProps
}: GlassCardProps) {
  return (
    <motion.div
      className={`
        rounded-xl border
        ${gradient ? "bg-[image:var(--gradient-card)]" : ""}
        bg-[var(--bg-card)] border-[var(--border)]
        shadow-[var(--shadow-sm)]
        backdrop-blur-[var(--glass-blur)]
        ${hover ? "hover:shadow-[var(--shadow-md)] hover:border-[var(--border-hover)]" : ""}
        transition-all duration-300
        ${padding}
        ${className}
      `}
      whileHover={hover ? { y: -2, scale: 1.005 } : undefined}
      transition={{ type: "spring", stiffness: 300, damping: 30 }}
      {...motionProps}
    >
      {children}
    </motion.div>
  );
}
