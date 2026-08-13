# Soeuk Bondol — Portfolio

Personal portfolio of Soeuk Bondol, Data Scientist based in Phnom Penh, Cambodia.

Built with Astro and Tailwind CSS. Deployed via GitHub Pages.

---

## Stack

- [Astro](https://astro.build) — static site framework
- [Tailwind CSS](https://tailwindcss.com) — utility-first styling
- Inter, Plus Jakarta Sans, JetBrains Mono — typography (self-hosted via Fontsource)

## Project Structure

```
/
├── public/
│   ├── asciinema/          # self-hosted asciinema-player (css + js)
│   ├── recordings/         # portfolio.cast — terminal showcase recording
│   ├── 404.html            # redirects wrong URLs to /portfolio/
│   └── favicon.svg
├── scripts/
│   └── gen-terminal-cast.py  # regenerates public/recordings/portfolio.cast
├── src/
│   ├── components/
│   │   ├── Nav.astro
│   │   ├── Hero.astro
│   │   ├── Terminal.astro   # asciinema terminal showcase (like pi.dev)
│   │   ├── Projects.astro
│   │   ├── Stack.astro
│   │   ├── Contact.astro
│   │   └── Footer.astro
│   ├── layouts/
│   │   └── Base.astro
│   ├── pages/
│   │   └── index.astro
│   └── styles/
│       └── global.css
├── .github/
│   └── workflows/
│       └── deploy.yml
├── astro.config.mjs
├── tailwind.config.mjs
└── package.json
```

## Terminal showcase

The "Terminal" section plays a scripted terminal session (autoplay, looping) with
[asciinema-player](https://github.com/asciinema/asciinema-player) — same idea as
the pi.dev landing page. The player is self-hosted under `public/asciinema/` and
the recording lives at `public/recordings/portfolio.cast` (`.cast` = JSON Lines:
ANSI output + timestamps).

To edit the demo (commands, timing, content), change
`scripts/gen-terminal-cast.py` and regenerate:

```bash
python3 scripts/gen-terminal-cast.py
```

The theme is baked into the cast header so the terminal always matches the
site's accent palette.

## Commands

| Command           | Action                             |
| :---------------- | :--------------------------------- |
| `npm install`     | Install dependencies               |
| `npm run dev`     | Start dev server at localhost:4321 |
| `npm run build`   | Build production site to ./dist/   |
| `npm run preview` | Preview production build locally   |

## Contact

- Gmail: soeukbondolcc@gmail.com
- GitHub: [github.com/SoeukBondol-ai](https://github.com/SoeukBondol-ai)