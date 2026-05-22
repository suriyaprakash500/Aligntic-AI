import { motion } from 'framer-motion';
import { Send } from 'lucide-react';

export function Contact() {
  return (
    <main className="flex-1 px-8 py-20 max-w-2xl mx-auto w-full">
      <motion.h1 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-4xl md:text-6xl font-semibold tracking-tighter text-white mb-4 text-center"
      >
        Get in touch
      </motion.h1>
      <motion.p 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="text-white/50 text-center mb-12"
      >
        Ready to integrate AI into your workflow? Drop us a message.
      </motion.p>

      <motion.form 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="space-y-6 bg-[#0d0d0d] p-8 border border-white/10 rounded-3xl"
        onSubmit={(e) => e.preventDefault()}
      >
        <div className="space-y-2">
          <label className="text-xs font-medium text-white/50 uppercase tracking-wider">Name</label>
          <input type="text" className="w-full bg-[#151515] border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-white/30 transition-colors" placeholder="John Doe" />
        </div>
        <div className="space-y-2">
          <label className="text-xs font-medium text-white/50 uppercase tracking-wider">Email</label>
          <input type="email" className="w-full bg-[#151515] border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-white/30 transition-colors" placeholder="john@example.com" />
        </div>
        <div className="space-y-2">
          <label className="text-xs font-medium text-white/50 uppercase tracking-wider">Message</label>
          <textarea rows={4} className="w-full bg-[#151515] border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-white/30 transition-colors resize-none" placeholder="How can we help you?" />
        </div>
        <button type="submit" className="w-full flex items-center justify-center gap-2 bg-white text-black px-8 py-4 rounded-xl font-medium hover:bg-white/90 transition-transform active:scale-[0.98]">
          Send Message <Send className="w-4 h-4" />
        </button>
      </motion.form>
    </main>
  );
}
