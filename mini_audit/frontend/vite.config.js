import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'


const NGROK_HOST = 'tamala-overwarmed-gaynell.ngrok-free.dev'

export default defineConfig({
  plugins: [react()],
  server: {

    allowedHosts: [NGROK_HOST],
    

  }
})
