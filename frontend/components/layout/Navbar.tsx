"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Zap, Sun, Moon, Menu, X } from "lucide-react";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ConnectionStatus } from "./ConnectionStatus";
import { useTheme } from "./ThemeProvider";

const NAV_LINKS = [
  { href: "/", label: "Dashboard" },
  { href: "/metrics", label: "Training" },
  { href: "/playground", label: "Playground" },
  { href: "/architecture", label: "Architecture" },
];

export function Navbar() {
  const pathname = usePathname();
  const { isDark, toggleTheme } = useTheme();
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <>
      <nav className="sticky top-0 z-50 glass border-b border-[var(--border)]">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-8">
              <Link href="/" className="flex items-center gap-2 font-bold text-lg group">
                <div className="relative">
                  <Zap className="w-5 h-5 text-[var(--accent-indigo)] transition-transform group-hover:scale-110" />
                  <div className="absolute inset-0 bg-[var(--accent-indigo)] opacity-20 blur-md rounded-full" />
                </div>
                <span className="text-[var(--text-primary)]">PEFT Platform</span>
              </Link>

              <div className="hidden md:flex gap-1 relative">
                {NAV_LINKS.map((link) => {
                  const isActive = pathname === link.href;
                  return (
                    <Link
                      key={link.href}
                      href={link.href}
                      className={`relative px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                        isActive
                          ? "text-[var(--accent-indigo)]"
                          : "text-[var(--text-secondary)] hover:text-[var(--text-primary)] hover:bg-[var(--border)]"
                      }`}
                    >
                      {link.label}
                      {isActive && (
                        <motion.div
                          layoutId="nav-indicator"
                          className="absolute inset-0 rounded-lg"
                          style={{ background: "var(--accent-indigo)", opacity: 0.1 }}
                          transition={{ type: "spring", stiffness: 400, damping: 30 }}
                        />
                      )}
                    </Link>
                  );
                })}
              </div>
            </div>

            <div className="flex gap-3 items-center">
              <div className="hidden sm:block">
                <ConnectionStatus />
              </div>

              <motion.button
                onClick={toggleTheme}
                className="p-2 rounded-lg text-[var(--text-secondary)] hover:text-[var(--text-primary)] hover:bg-[var(--border)] transition-colors"
                whileTap={{ scale: 0.9 }}
                aria-label="Toggle theme"
              >
                <AnimatePresence mode="wait">
                  {isDark ? (
                    <motion.div
                      key="sun"
                      initial={{ rotate: -90, opacity: 0 }}
                      animate={{ rotate: 0, opacity: 1 }}
                      exit={{ rotate: 90, opacity: 0 }}
                      transition={{ duration: 0.2 }}
                    >
                      <Sun className="w-5 h-5" />
                    </motion.div>
                  ) : (
                    <motion.div
                      key="moon"
                      initial={{ rotate: 90, opacity: 0 }}
                      animate={{ rotate: 0, opacity: 1 }}
                      exit={{ rotate: -90, opacity: 0 }}
                      transition={{ duration: 0.2 }}
                    >
                      <Moon className="w-5 h-5" />
                    </motion.div>
                  )}
                </AnimatePresence>
              </motion.button>

              <button
                onClick={() => setMobileOpen(true)}
                className="md:hidden p-2 rounded-lg text-[var(--text-secondary)] hover:bg-[var(--border)]"
                aria-label="Open menu"
              >
                <Menu className="w-5 h-5" />
              </button>
            </div>
          </div>
        </div>
      </nav>

      <AnimatePresence>
        {mobileOpen && (
          <>
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="fixed inset-0 z-50 bg-black/50 backdrop-blur-sm md:hidden"
              onClick={() => setMobileOpen(false)}
            />
            <motion.div
              initial={{ x: "100%" }}
              animate={{ x: 0 }}
              exit={{ x: "100%" }}
              transition={{ type: "spring", damping: 25, stiffness: 300 }}
              className="fixed right-0 top-0 bottom-0 z-50 w-72 glass border-l border-[var(--border)] p-6 md:hidden"
              style={{ background: "var(--bg-card-solid)" }}
            >
              <div className="flex items-center justify-between mb-8">
                <span className="font-bold text-[var(--text-primary)]">Menu</span>
                <button
                  onClick={() => setMobileOpen(false)}
                  className="p-2 rounded-lg hover:bg-[var(--border)]"
                >
                  <X className="w-5 h-5 text-[var(--text-secondary)]" />
                </button>
              </div>

              <div className="space-y-2">
                {NAV_LINKS.map((link) => {
                  const isActive = pathname === link.href;
                  return (
                    <Link
                      key={link.href}
                      href={link.href}
                      onClick={() => setMobileOpen(false)}
                      className={`block px-4 py-3 rounded-lg text-sm font-medium transition-colors ${
                        isActive
                          ? "text-[var(--accent-indigo)]"
                          : "text-[var(--text-secondary)] hover:bg-[var(--border)]"
                      }`}
                      style={isActive ? { background: "color-mix(in srgb, var(--accent-indigo) 10%, transparent)" } : undefined}
                    >
                      {link.label}
                    </Link>
                  );
                })}
              </div>

              <div className="mt-8 pt-8 border-t border-[var(--border)]">
                <ConnectionStatus />
              </div>
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </>
  );
}
