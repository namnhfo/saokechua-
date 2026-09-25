import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin", "vietnamese"],
  variable: "--font-inter",
});

export const metadata = {
  title: "Quản Lý Thu Chi - Tự Động Sao Kê",
  description: "Ứng dụng di động quản lý tài chính cá nhân và sao kê giao dịch thông minh.",
  manifest: "/manifest.json",
  appleWebApp: {
    capable: true,
    statusBarStyle: "black-translucent",
    title: "Thu Chi",
  },
  icons: {
    icon: "/icons/icon-192x192.png",
    apple: "/icons/apple-touch-icon.png",
  },
};

export const viewport = {
  themeColor: "#059669",
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
};

export default function RootLayout({ children }) {
  return (
    <html lang="vi" className={`${inter.variable} h-full antialiased`}>
      <head>
        <link rel="manifest" href="/manifest.json" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
        <meta name="apple-mobile-web-app-title" content="Thu Chi" />
      </head>
      <body className="min-h-full bg-slate-900 text-slate-100 flex justify-center font-sans antialiased selection:bg-emerald-500 selection:text-white">
        {/* Container chuẩn Mobile First: max-w-md, căn giữa trên PC màn hình rộng */}
        <div className="w-full max-w-md min-h-screen bg-slate-950 text-slate-100 shadow-2xl relative flex flex-col border-x border-slate-800/60">
          {children}
        </div>
      </body>
    </html>
  );
}
