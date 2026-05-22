Remove-Item setup.ps1 -Force -ErrorAction SilentlyContinue
npx -y create-vite@latest temp-app --template react-ts
Get-ChildItem -Path temp-app -Force | Move-Item -Destination . -Force
Remove-Item -Path temp-app -Recurse -Force
npm install
npm install -D tailwindcss@3 postcss autoprefixer
npx tailwindcss init -p
npm install framer-motion clsx tailwind-merge lucide-react
