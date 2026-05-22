import { motion } from 'framer-motion';

export function About() {
  return (
    <main className="flex-1 px-8 py-20 max-w-4xl mx-auto w-full text-center">
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="w-24 h-24 bg-white rounded-full mx-auto mb-10 flex items-center justify-center"
      >
        <span className="text-black font-bold text-2xl tracking-tighter">AL</span>
      </motion.div>
      <motion.h1 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="text-4xl md:text-6xl font-semibold tracking-tighter text-white mb-8"
      >
        Aligning Intelligence with Humanity.
      </motion.h1>
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="space-y-6 text-white/60 text-lg leading-relaxed font-light"
      >
        <p>
          Aligntic was founded on a simple principle: artificial intelligence should augment human capability, not complicate it.
        </p>
        <p>
          We are a team of researchers, engineers, and designers dedicated to building systems that are powerful, transparent, and aesthetically uncompromising. Our minimalist approach to product design ensures that our technology gets out of the way, letting your users focus on what matters.
        </p>
      </motion.div>
    </main>
  );
}
