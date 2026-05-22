import { motion } from 'framer-motion';
import { ArrowRight } from 'lucide-react';
import { Link } from 'react-router-dom';

export function Products() {
  return (
    <main className="flex-1 px-8 py-20 max-w-7xl mx-auto w-full">
      <motion.h1 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-4xl md:text-6xl font-semibold tracking-tighter text-white mb-6"
      >
        Our AI Products
      </motion.h1>
      <motion.p 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="text-white/50 text-lg max-w-2xl mb-16"
      >
        Enterprise-grade artificial intelligence solutions designed to scale with your business.
      </motion.p>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.2 }}
          className="group relative rounded-3xl overflow-hidden border border-white/10 bg-[#111] aspect-[4/3]"
        >
          <img src="/pulse_finance.jpg" alt="Pulse Finance" className="absolute inset-0 w-full h-full object-cover opacity-50 group-hover:opacity-70 transition-opacity duration-500 object-top" />
          <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent" />
          <div className="absolute bottom-0 left-0 p-8 w-full">
            <h3 className="text-2xl font-medium text-white mb-2">Pulse Finance</h3>
            <p className="text-white/60 mb-6 text-sm">Privacy-first Android app with automatic SMS extraction and AI-powered spending insights.</p>
            <Link to="/products/pulse-finance" className="flex items-center gap-2 text-sm text-white font-medium group-hover:gap-3 transition-all">
              View Case Study <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </motion.div>
        
        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.3 }}
          className="group relative rounded-3xl overflow-hidden border border-white/10 bg-[#111] aspect-[4/3]"
        >
          <img src="/newsume_ai.jpg" alt="Newsume AI" className="absolute inset-0 w-full h-full object-cover opacity-50 group-hover:opacity-70 transition-opacity duration-500 object-top" />
          <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent" />
          <div className="absolute bottom-0 left-0 p-8 w-full">
            <h3 className="text-2xl font-medium text-white mb-2">Newsume AI</h3>
            <p className="text-white/60 mb-6 text-sm">An AI that reads your resume and delivers daily personalized tech news with career impact cards.</p>
            <Link to="/products/newsume-ai" className="flex items-center gap-2 text-sm text-white font-medium group-hover:gap-3 transition-all">
              View Case Study <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </motion.div>
      </div>
    </main>
  );
}
