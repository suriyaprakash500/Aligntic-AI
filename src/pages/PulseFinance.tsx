import { motion } from 'framer-motion';
import { CheckCircle2, ShieldCheck, BrainCircuit } from 'lucide-react';
import { Link } from 'react-router-dom';

const features = [
  "Automatic SMS Parsing (HDFC, ICICI, SBI, Axis, Kotak, PhonePe, GPay, Paytm)",
  "Real-time transaction capture via BroadcastReceiver",
  "Smart auto-categorization with confidence scoring",
  "Manual review & category correction with learning",
  "Subscription detection & bill reminders",
  "Spending visualization — monthly charts & breakdowns",
  "Biometric App Lock (Fingerprint / Face ID)",
  "Semantic search across transactions",
  "Privacy-first — all data stays on device"
];

const aiFeatures = [
  "Personality classification (Saver / Balanced / Impulsive)",
  "Behavioral insights with severity levels",
  "Personalized actionable tips",
  "Monthly spending summary",
  "Detailed category breakdown",
  "Offline fallback when AI unavailable"
];

export function PulseFinance() {
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
          <img src="/pulse_finance.jpg" alt="Pulse Finance App" className="w-full rounded-3xl border border-white/10 shadow-2xl object-cover aspect-[9/19]" />
        </motion.div>

        <motion.div 
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.1 }}
          className="space-y-8"
        >
          <div>
            <h1 className="text-4xl md:text-5xl font-semibold tracking-tighter text-white mb-4">Pulse Finance</h1>
            <p className="text-white/60 text-lg leading-relaxed font-light">
              A privacy-first Android app that automatically extracts financial transactions from SMS, detects spending patterns, and delivers AI-powered insights.
            </p>
          </div>

          <div className="space-y-6">
            <h3 className="text-xl font-medium text-white flex items-center gap-2">
              <ShieldCheck className="w-5 h-5 text-cyan-400" /> Core Features
            </h3>
            <ul className="space-y-3">
              {features.map((feature, i) => (
                <li key={i} className="flex items-start gap-3 text-white/70 text-sm leading-relaxed">
                  <CheckCircle2 className="w-5 h-5 text-green-500 shrink-0" />
                  <span>{feature}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="space-y-6 pt-6 border-t border-white/10">
            <h3 className="text-xl font-medium text-white flex items-center gap-2">
              <BrainCircuit className="w-5 h-5 text-purple-400" /> AI Spending Coach
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
