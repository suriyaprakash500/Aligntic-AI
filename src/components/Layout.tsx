import { Outlet, Link } from 'react-router-dom';

export function Layout() {
  return (
    <div className="min-h-screen bg-[#0a0a0a] text-[#ededed] flex flex-col font-sans selection:bg-white/20">
      <nav className="flex items-center justify-between px-8 py-6 border-b border-white/5">
        <Link to="/" className="text-xl font-medium tracking-tight text-white hover:opacity-80 transition-opacity">
          Aligntic
        </Link>
        <div className="hidden md:flex gap-8 text-sm text-white/60">
          <Link to="/products" className="hover:text-white transition-colors">Products</Link>
          <Link to="/services" className="hover:text-white transition-colors">Services</Link>
          <Link to="/about" className="hover:text-white transition-colors">About</Link>
        </div>
        <Link to="/contact" className="text-sm bg-white text-black px-4 py-2 rounded-full font-medium hover:bg-white/90 transition-colors">
          Contact Us
        </Link>
      </nav>

      <div className="flex-1 flex flex-col">
        <Outlet />
      </div>

      <footer className="py-8 text-center text-sm text-white/30 border-t border-white/5 mt-auto">
        © 2026 Aligntic. All rights reserved. Minimalist design, maximal impact.
      </footer>
    </div>
  );
}
