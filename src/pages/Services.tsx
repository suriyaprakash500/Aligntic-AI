import { motion } from 'framer-motion';
import { Cpu, Brain, Network, Workflow, LineChart, Layers, MessageSquare } from 'lucide-react';

const services = [
  {
    icon: <Brain className="w-6 h-6 text-purple-400" />,
    title: "Custom LLM Fine-tuning",
    description: "We adapt large language models to your specific domain data, ensuring high accuracy and perfect tone alignment for your enterprise."
  },
  {
    icon: <Network className="w-6 h-6 text-blue-400" />,
    title: "AI Integration Architecture",
    description: "Seamlessly integrate predictive and generative AI into your existing software stack without disrupting current operations."
  },
  {
    icon: <Cpu className="w-6 h-6 text-green-400" />,
    title: "Edge Deployment Optimization",
    description: "Compress and optimize models to run efficiently on edge devices, reducing latency and cloud compute costs."
  },
  {
    icon: <Workflow className="w-6 h-6 text-orange-400" />,
    title: "AI Automation Workflows",
    description: "Automate repetitive business operations using intelligent AI agents and robust end-to-end workflows."
  },
  {
    icon: <LineChart className="w-6 h-6 text-cyan-400" />,
    title: "AI-Powered Analytics & Forecasting",
    description: "Use advanced ML models to predict business trends, uncover hidden insights, and optimize your operations."
  },
  {
    icon: <Layers className="w-6 h-6 text-yellow-400" />,
    title: "Multimodal AI Solutions",
    description: "Combine text, image, audio, and video AI systems to create comprehensive, next-generation user experiences."
  },
  {
    icon: <MessageSquare className="w-6 h-6 text-pink-400" />,
    title: "Conversational AI Platforms",
    description: "Deploy intelligent, context-aware virtual assistants that handle complex customer interactions with human-like understanding."
  }
];

export function Services() {
  return (
    <main className="flex-1 px-8 py-20 max-w-7xl mx-auto w-full">
      <motion.h1 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-4xl md:text-6xl font-semibold tracking-tighter text-white mb-6"
      >
        AI Consulting & Services
      </motion.h1>
      <motion.p 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="text-white/50 text-lg max-w-2xl mb-16"
      >
        Partner with our world-class engineering team to build bespoke AI solutions.
      </motion.p>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {services.map((s, i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 + (i * 0.1) }}
            className="p-8 rounded-3xl border border-white/10 bg-[#0d0d0d] hover:bg-[#151515] transition-colors"
          >
            <div className="w-12 h-12 bg-white/5 rounded-2xl flex items-center justify-center mb-6 border border-white/10">
              {s.icon}
            </div>
            <h3 className="text-xl font-medium text-white mb-3">{s.title}</h3>
            <p className="text-sm text-white/50 leading-relaxed">{s.description}</p>
          </motion.div>
        ))}
      </div>
    </main>
  );
}
