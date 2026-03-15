/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        bg:      '#0a0a0b',
        surface: '#111113',
        border:  '#1e1e22',
        green:   '#00ff88',
        blue:    '#4488ff',
        orange:  '#ff6b35',
        muted:   '#555560',
        dim:     '#1a1a1e',
      },
      fontFamily: {
        mono: ['JetBrains Mono', 'monospace'],
        display: ['Syne', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
