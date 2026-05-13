# Mining Hardware Video — Production Benchmark Spec

## Overview

This spec defines a production-ready benchmark for mining hardware promotional videos. Three duration variants are required: **15s (social cut)**, **30s (standard ad)**, and **60s (deep-dive)**. Each variant must pass per-shot acceptance criteria defined below.

**Reward:** 15 RTC (base, 15s only) / 25 RTC (extended, all three variants). Pool cap: 200 RTC across all submissions.

## Shot List — 60s Variant (Reference)

All shorter variants are subsets of this. Shots are numbered for cross-referencing.

| Shot | Description | Duration | Key Visual Elements | Voiceover (VO) |
|------|-------------|----------|---------------------|----------------|
| S1 | Open — ASIC miner in dark room, power LED flickers on | 0:00–0:05 | Close-up of hash board, green LEDs, subtle glow | "Every hash starts with a single cycle." |
| S2 | Wide rack shot — multiple miners running, fans spinning | 0:05–0:12 | 3–5 units in frame, airflow visible, blue/white LEDs | "This is RustChain mining hardware. Built for density." |
| S3 | Hash rate display overlay — 120 TH/s, power draw 3250W | 0:12–0:18 | Screen capture or HUD overlay on S2 footage | "120 terahash. 3250 watts. Industry-leading efficiency." |
| S4 | Thermal camera view — heat distribution across chips | 0:18–0:23 | IR footage, hot spots < 75°C, even spread | "Advanced thermal design keeps junction temps under control." |
| S5 | Close-up — immersion cooling tank, mineral oil bubbling | 0:23–0:30 | Transparent tank, submerged boards, bubble streams | "Optional immersion cooling for zero-fan operation." |
| S6 | Dashboard UI — RustChain pool stats, real-time earnings | 0:30–0:38 | Web dashboard, BTC/RTC balance, worker status | "Monitor everything from one dashboard. Real-time." |
| S7 | Split screen — left: old GPU rig, right: RustChain ASIC | 0:38–0:45 | Side-by-side comparison, power meter readings | "Compare: 8 GPUs vs one ASIC. Same hash rate. 1/3 the power." |
| S8 | Unboxing shot — unit removed from packaging, size reference | 0:45–0:52 | Hand holding miner, banana or ruler for scale | "Ships worldwide. Plug and mine in under 10 minutes." |
| S9 | CTA — logo + URL + QR code | 0:52–0:60 | RustChain logo, rustchain.io, scan-to-buy QR | "RustChain. Mine smarter. Visit rustchain.io." |

## Duration Variants

### 15s (Social Cut) — 15 RTC
- **Shots used:** S1 (2s), S3 (3s), S6 (4s), S9 (6s)
- **No voiceover** — text overlays only
- **Captions:** "120 TH/s · 3250W · Real-time dashboard" → fade to CTA
- **Aspect ratio:** 9:16 vertical (TikTok/Reels/Shorts)
- **Max text:** 3 lines on screen at any time

### 30s (Standard Ad) — 20 RTC
- **Shots used:** S1 (3s), S2 (4s), S3 (4s), S5 (5s), S7 (6s), S9 (8s)
- **Voiceover:** Full script from S1, S2, S3, S5, S7, S9
- **Captions:** Key metrics overlaid on S3 and S7
- **Aspect ratio:** 16:9 landscape
- **Audio:** VO + ambient machine hum (low, -18dB)

### 60s (Deep-Dive) — 25 RTC
- **All 9 shots** as specified above
- **Full voiceover**
- **Captions on S3, S4, S6, S7**
- **Aspect ratio:** 16:9 landscape
- **Audio:** VO + ambient + subtle transition whoosh

## Asset Constraints

### Video Assets
- **Resolution:** Minimum 1920×1080 (all variants). 4K preferred for 60s.
- **Frame rate:** 30fps or 60fps (consistent within variant)
- **Codec:** H.264 or H.265, bitrate ≥ 15 Mbps (1080p)
- **No watermarks, no third-party logos** (except RustChain branding)
- **Stock footage allowed** for S4 (thermal) and S5 (immersion) only — must be royalty-free with proof of license

### Audio Assets
- **Voiceover:** Male or female, neutral English accent, no music background
- **Sample rate:** 48 kHz, 16-bit, mono
- **Level:** -12dB to -6dB peak, no clipping
- **Background music:** Optional for 60s only — instrumental, no lyrics, royalty-free, -20dB relative to VO

### Text/Captions
- **Font:** Montserrat (free Google Font) or system sans-serif fallback
- **Size:** Minimum 48px for 16:9, 64px for 9:16
- **Color:** White with 20% black drop shadow
- **Duration:** Minimum 2s per caption, maximum 4s
- **Position:** Bottom third (16:9) or center-lower (9:16)

## Pass/Fail Acceptance Criteria

Each shot must pass all applicable checks:

| Criterion | Pass | Fail |
|-----------|------|------|
| **Resolution** | ≥ 1920×1080, no scaling artifacts | Sub-1080p, stretched, or pixelated |
| **Duration** | Within ±0.5s of spec | Off by > 0.5s |
| **VO sync** | Lip-sync not applicable (no talent), but VO aligns with shot content | VO describes something not on screen |
| **Captions** | Correct text, readable, no typos | Missing, illegible, or wrong metrics |
| **Branding** | RustChain logo present in final shot, correct color (#FF6B35 orange) | Wrong logo, wrong color, or missing |
| **Audio levels** | VO -12dB to -6dB, music -20dB relative | Clipping, silence, or music overpowers VO |
| **Format** | H.264/H.265, correct container (.mp4) | Wrong codec, wrong container, or corrupted file |
| **No watermarks** | Clean footage | Any third-party watermark visible |

**Hard fails:** Missing CTA shot, wrong aspect ratio, VO with background music in 15s/30s variants, any shot duration off by > 1s.

## Submission Format

Submit as a single ZIP containing:
- `rustchain_mining_15s.mp4`
- `rustchain_mining_30s.mp4`
- `rustchain_mining_60s.mp4`
- `rustchain_mining_assets.txt` — list of all assets used (stock footage URLs, font name, music track title)
- `rustchain_mining_credits.txt` — your name/handle for attribution

**No README, no extra files.** Just the deliverables.

## Notes

- 15s variant can be a straight cut from 60s — no need to re-render everything.
- If you don't have access to actual mining hardware, use high-quality product mockups or stock footage. The thermal shot (S4) is the hardest to source — a simulated thermal overlay on a static image is acceptable.
- The 200 RTC pool is shared across all submitters. First valid submission for each variant gets priority review. If multiple submissions pass, pool is split proportionally by variant count.

---

*Last updated: 2026-04-26. This spec replaces the original "make a video" bounty. All previous discussion is superseded.*