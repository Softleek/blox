/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  eslint: {
    ignoreDuringBuilds: true,
  },
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "**", // Allow all HTTPS domains
        pathname: "/**",
      },
      {
        protocol: "http",
        hostname: "**", // Allow all HTTP domains (including local dev)
        pathname: "/**",
      },
    ],
    domains: ["*"], // Allow all domains
    unoptimized: true, // Allows images without Next.js optimization
  },
  async rewrites() {
    return [
      {
        source: "/:path*",
        destination: "/:path*",
      },
    ];
  },
};

export default nextConfig;
