import { motion } from 'framer-motion';
import { ArrowRight, Sparkles } from 'lucide-react';
import { Link } from 'react-router-dom';

export function Home() {
  return (
    <main className="flex-1 flex flex-col items-center justify-center px-4 py-20 text-center relative overflow-hidden">
      {/* Background Glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-white/[0.02] rounded-full blur-[120px] pointer-events-none" />

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
        className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-white/10 bg-white/5 text-xs font-medium text-white/80 mb-8 z-10"
      >
        <Sparkles className="w-3 h-3" />
        The future of AI is here
      </motion.div>

      <motion.h1 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
        className="text-5xl md:text-7xl lg:text-8xl font-semibold tracking-tighter text-white max-w-4xl z-10"
      >
        Intelligence, <br /> beautifully aligned.
      </motion.h1>

      <motion.p 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
        className="mt-8 text-lg md:text-xl text-white/50 max-w-2xl font-light leading-relaxed z-10"
      >
        We build premium AI products and services that seamlessly integrate into your ecosystem. Minimalist design, maximal impact.
      </motion.p>

      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.3, ease: [0.16, 1, 0.3, 1] }}
        className="mt-12 flex flex-col sm:flex-row items-center gap-4 z-10"
      >
        <Link to="/products" className="w-full sm:w-auto flex items-center justify-center gap-2 bg-white text-black px-8 py-4 rounded-full font-medium hover:bg-white/90 transition-transform hover:scale-105 active:scale-95">
          View Products <ArrowRight className="w-4 h-4" />
        </Link>
        <Link to="/services" className="w-full sm:w-auto flex items-center justify-center gap-2 border border-white/10 bg-white/5 text-white px-8 py-4 rounded-full font-medium hover:bg-white/10 transition-colors">
          Our Services
        </Link>
      </motion.div>
    </main>
  );
}
