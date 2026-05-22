import { motion } from 'framer-motion';
import { CheckCircle2, ShieldCheck, BrainCircuit } from 'lucide-react';
import { Link } from 'react-router-dom';

const coreFeatures = [
  "Resume upload & parsing with AI skill extraction (Groq Llama 3.3)",
  "User-editable profile to add/remove extracted skills and certifications",
  "12 integrated news sources (Hacker News, DEV, freeCodeCamp, TechCrunch, etc.)",
  "Personalization controls (preferred/blocked topics, seniority levels)",
  "Customizable delivery schedule for digests and alerts"
];

const aiFeatures = [
  "Daily 2-minute digest summarizing key tech updates",
  "Career impact cards explaining why an article matters and next action",
  "AI skill-gap report comparing resume skills against industry trends",
  "Resume improvement suggestions tailored to career goals",
  "Smart bookmarking and learning-based profile refinement"
];

export function NewsumeAI() {
  return (
    <main className="flex-1 px-8 py-20 max-w-6xl mx-auto w-full">
      <Link to="/products" className="text-white/40 hover:text-white transition-colors text-sm mb-12 inline-block">
        &larr; Back to Products
      </Link>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-16 items-start">
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
        >
          <img src="/newsume_ai.jpg" alt="Newsume AI App" className="w-full rounded-3xl border border-white/10 shadow-2xl object-cover aspect-[9/19]" />
        </motion.div>

        <motion.div 
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.1 }}
          className="space-y-8"
        >
          <div>
            <h1 className="text-4xl md:text-5xl font-semibold tracking-tighter text-white mb-4">Newsume AI</h1>
            <p className="text-white/60 text-lg leading-relaxed font-light">
              An Android app and Python backend that reads your resume, extracts your skills and experience, and delivers daily personalized, career-relevant tech news with AI-powered career impact cards, skill-gap analysis, and a 2-minute daily digest.
            </p>
          </div>

          <div className="space-y-6">
            <h3 className="text-xl font-medium text-white flex items-center gap-2">
              <ShieldCheck className="w-5 h-5 text-cyan-400" /> Core Features
            </h3>
            <ul className="space-y-3">
              {coreFeatures.map((feature, i) => (
                <li key={i} className="flex items-start gap-3 text-white/70 text-sm leading-relaxed">
                  <CheckCircle2 className="w-5 h-5 text-green-500 shrink-0" />
                  <span>{feature}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="space-y-6 pt-6 border-t border-white/10">
            <h3 className="text-xl font-medium text-white flex items-center gap-2">
              <BrainCircuit className="w-5 h-5 text-purple-400" /> AI Insights & Personalization
            </h3>
            <ul className="space-y-3">
              {aiFeatures.map((feature, i) => (
                <li key={i} className="flex items-start gap-3 text-white/70 text-sm leading-relaxed">
                  <CheckCircle2 className="w-5 h-5 text-green-500 shrink-0" />
                  <span>{feature}</span>
                </li>
              ))}
            </ul>
          </div>
        </motion.div>
      </div>
    </main>
  );
}
