import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
  },
  site: 'https://soeukbondol-ai.github.io',
  base: '/portfolio',
  output: 'static',
});