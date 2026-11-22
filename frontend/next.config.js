/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    if (process.env.NODE_ENV === "development") {
      return [
        {
          source: "/api/:path*",
          destination: "http://localhost:8002/api/:path*",
        },
        {
          source: "/health",
          destination: "http://localhost:8002/health",
        },
      ];
    }
    return [];
  },
};

module.exports = nextConfig;
