#!/usr/bin/env python3
"""
Generate public/recordings/portfolio.cast — the terminal showcase for the
portfolio site (rendered with asciinema-player, same idea as pi.dev).

Regenerate with:
    python3 scripts/gen-terminal-cast.py

The .cast format (v2) is JSON Lines:
    {"version":2,"width":W,"height":H,"timestamp":T,"env":{...}}
    [time, "o", "output"]        # 'o' = output printed to the terminal

Terminal colors map to the site theme via the player's custom theme:
    30 black #0d1117   31 red #f87171    32 green #4ade80   33 amber #f0b429
    34 blue  #4d9de0   35 vio  #a78bfa   36 cyan  #38d9f5   37 white #f0f4ff
    90 muted #8899bb   97 bright white #ffffff
"""

import json
import time

WIDTH, HEIGHT = 80, 24
OUT = "public/recordings/portfolio.cast"

t = 0.0
events = []


def emit(text: str, delay: float = 0.0):
    """Append an output event at current time `t`, then advance time."""
    global t
    events.append([round(t, 3), "o", text])
    t += delay


# ── ANSI helpers ──────────────────────────────────────────────────────────
RESET = "\x1b[0m"
BOLD = "\x1b[1m"
DIM = "\x1b[2m"
CLEAR_LINE = "\x1b[K"  # erase from cursor to end of line

GREEN = "\x1b[32m"
AMBER = "\x1b[33m"
BLUE = "\x1b[34m"
VIOLET = "\x1b[35m"
CYAN = "\x1b[36m"
WHITE = "\x1b[37m"
MUTED = "\x1b[90m"
RED = "\x1b[31m"
BWHITE = "\x1b[97m"


def c(code: str, text: str) -> str:
    return f"{code}{text}{RESET}"


# ── Typing helpers ────────────────────────────────────────────────────────
def type_cmd(cmd: str, cps: float = 24.0, pre: str = ""):
    """Type a command at the shell prompt, character by character, then press Enter."""
    emit(c(GREEN, "➜") + " " + c(CYAN, "~") + " " + pre, 0.35)
    for ch in cmd:
        emit(ch, 1.0 / cps)
    emit("\r\n", 0.25)


def run(delay: float = 0.55):
    """Pause after a command is submitted while it 'runs'."""
    emit("", delay)


def out(text: str, delay: float = 0.04):
    emit(text + "\r\n", delay)


def blank(delay: float = 0.12):
    emit("\r\n", delay)


# ── Demo content ──────────────────────────────────────────────────────────
def main():
    global t
    t = time.time()

    # header: version/geometry/env
    header = {
        "version": 2,
        "width": WIDTH,
        "height": HEIGHT,
        "timestamp": int(t),
        "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color", "COLORTERM": "truecolor"},
        # theme baked into the recording — mirrors the site palette so the
        # player renders with site colors via theme: "auto/asciinema"
        "theme": {
            "fg": "#f0f4ff",
            "bg": "#0d1117",
            "palette": ":".join(
                [
                    "#0d1117",  # 30 black
                    "#f87171",  # 31 red
                    "#4ade80",  # 32 green
                    "#f0b429",  # 33 amber (accent)
                    "#4d9de0",  # 34 blue
                    "#a78bfa",  # 35 violet
                    "#38d9f5",  # 36 cyan
                    "#f0f4ff",  # 37 white
                    "#8899bb",  # 90 muted
                    "#f87171",  # 91
                    "#4ade80",  # 92
                    "#f0b429",  # 93
                    "#4d9de0",  # 94
                    "#a78bfa",  # 95
                    "#38d9f5",  # 96
                    "#ffffff",  # 97 bright white
                ]
            ),
        },
    }
    print(json.dumps(header))
    events.append(header)

    # ── whoami ──
    type_cmd("whoami")
    run(0.5)
    out(c(WHITE, "soeuk-bondol") + c(MUTED, " — ") + c(AMBER, "Data Scientist") + c(MUTED, " @ ") + c(BLUE, "Phnom Penh, KH"))
    blank(0.4)

    # ── profile.json ──
    type_cmd("cat profile.json")
    run(0.5)
    out(c(MUTED, "{"))
    out(f"  {c(CYAN, '"name"')}: {c(GREEN, '"Soeuk Bondol"')},")
    out(f"  {c(CYAN, '"role"')}: {c(GREEN, '"Data Scientist"')},")
    out(f"  {c(CYAN, '"location"')}: {c(GREEN, '"Phnom Penh, Cambodia"')},")
    out(f"  {c(CYAN, '"focus"')}: [{c(GREEN, '"Machine Learning"')}, {c(GREEN, '"Computer Vision"')}, {c(GREEN, '"NLP"')}],")
    out(f"  {c(CYAN, '"stack"')}: [{c(GREEN, '"Python"')}, {c(GREEN, '"PyTorch"')}, {c(GREEN, '"FastAPI"')}, {c(GREEN, '"Docker"')}],")
    out(f"  {c(CYAN, '"status"')}: {c(AMBER, '"open to work"')}")
    out(c(MUTED, "}"))
    blank(0.4)

    # ── ls projects ──
    type_cmd("ls projects/")
    run(0.45)
    out(c(AMBER, "001_khmer-number-recognition/"))
    out(c(AMBER, "002_background-remover/"))
    out(c(AMBER, "003_grabbit/"))
    out(c(DIM + MUTED, "004_coming-soon/"))
    blank(0.4)

    # ── project readme ──
    type_cmd("cat projects/001_khmer-number-recognition/README.md | head -6")
    run(0.5)
    out(c(BOLD + WHITE, "# Khmer Number Recognition"), 0.1)
    blank(0.25)
    out(c(MUTED, "Deep learning model that reads handwritten Khmer numerals."))
    out(c(MUTED, "Custom CNN · data augmentation · ") + c(AMBER, "97.4% accuracy") + c(MUTED, "."))
    blank(0.25)
    out(c(VIOLET, "→ github.com/SoeukBondol-ai/khmer-number-recognition"))
    blank(0.4)

    # ── training run (animated progress bars) ──
    type_cmd("python train.py --model khmer_cnn --epochs 20")
    run(0.8)
    out(c(MUTED, "[2025-05-14 09:41:02]") + c(WHITE, " device:") + c(CYAN, "cuda:0") + c(WHITE, " batch:") + c(CYAN, "512") + c(WHITE, " lr:") + c(CYAN, "1e-3"), 0.15)

    def epoch_bar(epoch: int, pct: int, loss: str, acc: str, final: bool = False):
        filled = int(pct / 100 * 20)
        bar = "█" * filled + "░" * (20 - filled)
        color = GREEN if final else AMBER
        line = (
            f"{c(CYAN, f'Epoch {epoch:>2}/20')}  "
            f"{c(color, bar)} {pct:>3}%  "
            f"{c(MUTED, 'loss=')}{c(WHITE, loss)}  "
            f"{c(MUTED, 'val_acc=')}{c(GREEN if final else WHITE, acc)}"
        )
        return line

    # animate epochs 1..3 live with \r
    for e in range(1, 4):
        for p in range(0, 101, 4):
            emit("\r" + CLEAR_LINE + epoch_bar(e, p, "0.42", "0.941"), 0.03)
        emit("\r" + CLEAR_LINE + epoch_bar(e, 100, "0.42", "0.941") + "\r\n", 0.2)
    # a couple of quick static lines
    out(epoch_bar(7, 100, "0.0871", "0.958"))
    out(epoch_bar(14, 100, "0.0234", "0.966"))
    # final animated epoch
    for p in range(0, 101, 4):
        emit("\r" + CLEAR_LINE + epoch_bar(20, p, "0.0012", "0.974"), 0.03)
    emit("\r" + CLEAR_LINE + epoch_bar(20, 100, "0.0012", "0.974", final=True) + "\r\n", 0.25)
    out(c(GREEN, "✓") + c(MUTED, " Model saved → ") + c(CYAN, "models/khmer_cnn.pt"))
    blank(0.4)

    # ── contact API ──
    type_cmd("curl -s localhost:8000/api/contact | jq")
    run(0.9)
    out(c(MUTED, "{"))
    out(f"  {c(CYAN, '"email"')}: {c(GREEN, '"soeukbondolcc@gmail.com"')},")
    out(f"  {c(CYAN, '"github"')}: {c(GREEN, '"github.com/SoeukBondol-ai"')},")
    out(f"  {c(CYAN, '"socials"')}: [{c(GREEN, '"LinkedIn"')}, {c(GREEN, '"X"')}],")
    out(f"  {c(CYAN, '"response_time"')}: {c(AMBER, '"< 24h"')}")
    out(c(MUTED, "}"))
    blank(0.4)

    # ── exit ──
    type_cmd("exit")
    run(0.3)
    emit("", 1.0)

    with open(OUT, "w", encoding="utf-8") as f:
        for ev in events:
            f.write(json.dumps(ev, ensure_ascii=False) + "\n")
    print(f"wrote {OUT} ({len(events)} events, {t - events[1][0]:.1f}s of recording)")


if __name__ == "__main__":
    main()
