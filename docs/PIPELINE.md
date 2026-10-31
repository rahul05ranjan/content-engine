# PIPELINE — start-to-finish video production through the engine

**Zero-setup agent flow:** read this file + `docs/LEARNINGS.md` + `BENCHMARK.md` + the channel's `formats/<Channel>.md`, and you can produce a video anywhere. Every video MUST pass both gates (script ≥85, final ≥85 + hyperframes check 0 errors) before render.

---

## Step 0 — Pick the channel
`formats/<ChannelName>.md` = identity, voice, palette, structure, SEO voice. One file per channel; the engine is shared.

## Step 1 — Topic
- Fresh news → search today's top stories in the channel's niche. Pick ones with **drama or irony** (losses, bans, weird deals, wow-demos). Satire-friendly performs best.
- Given a URL → extract it + one extra search for angles.

## Step 2 — Script (WRITE FIRST, GATE FIRST)
Write the script per LEARNINGS.md §1 (persona objections → hook 2–3 lines with contrast → oven-moment promise → analogy → twist → ONE hero number in the second half → why-care bridges → viewer question → standard outro).
- Format: plain text, one segment per scene, blank lines between segments (this is what the gate parses).
- Numbers as spoken Hinglish words. Max 26 words/segment.
- **Gate it before ANY production:**
```bash
python engine/benchmark.py --script script.txt --script-only
# iterate until ≥85 (target 100)
```

## Step 3 — VO
- Use `templates/vo_gen_template.py`: fill SEGMENTS (text + delivery cue each), point OUT at the project's `assets/audio`, add your Gemini keys (env `GEMINI_KEY` + FALLBACK_KEYS).
- Run in background (key rotation + resume-safe). Measure each WAV duration — timings come from the REAL durations, never estimates.

## Step 4 — BGM + SFX
- Synthesize a NEW mood-specific instrumental BGM (never reuse; no lyrics) ~video length + 5s. numpy recipe: sub pulse + pad chords + event sparkle + risers before reveals.
- Scene-change SFX = soft click (~0.45 volume, ~0.22s). Event SFX: slam (hook stamp), ding (tips), riser (pre-reveal, ends on the cut).

## Step 5 — Build the video (HyperFrames recipe)
```bash
npx hyperframes init <project>        # BEFORE any dir creation inside
cd <project> && mkdir -p assets/audio assets/video compositions/components
# copy: aurora-vert.html + shaders.iife.js into compositions/,
#       sfx/bgm/footage into assets/
```
- `index.html`: scene hosts (start = actual VO timing: scene_start + 0.4 lead), audio tags (VO / BGM with `data-automation` ducking lane / soft clicks at seams / slam at hook), `data-motion-blur="on"` on root, `window.__timelines["main"] = gsap.timeline({paused:true})`.
- Scenes `compositions/s1..sN.html`: `<template>` + per-scene `@font-face` (Devanagari fallback) + static grain overlay + GSAP timeline registered as `window.__timelines["sN"]`. Varied entrances. **NO burned-in caption pills** (user decision) — retention comes from visual change per sentence.
- Final scene = **standard outro**: LIKE pill + SUBSCRIBE pill + brand lockup, lands dead-still, holds ≥2s.
- 3D only if the topic demands it (LEARNINGS.md §2.3D pattern).
- **Gate:**
```bash
npx hyperframes check --json          # lint 0, runtime 0, layout 0
python engine/benchmark.py --project <project> --script script.txt
# BOTH must pass before render
```
- Optionally `npx hyperframes snapshot --review` and inspect the beat/phone sheets.

## Step 6 — Render + deliver
```bash
npm run render                        # or: npx hyperframes render --quality looks
```
- Copy to the user's delivery folder as `<slug>-<channel>.mp4` + same file as `<slug>-IG-reel.mp4`.
- Verify: ffprobe duration matches root `data-duration`; audio stream present.

## Step 7 — SEO package
Fill `templates/seo_template.md` → save as `<slug>-seo.md`. Title formula: Hinglish caps punch + emoji + `| <Channel>`. Description: hook line → arrow facts → one-line claim → source → channel CTA → viewer question → hashtags. Plus: 2 alternate titles, tags, pinned comment, IG caption (3 hook lines + 20 hashtags).

## Step 8 — Publish
- YouTube: **YouTube Data API v3** (`videos.insert`, scope `youtube.upload`) — one-time OAuth setup. Browser automation does NOT work (Google blocks automated browsers).
- Instagram: same MP4 natively; post 7–9 PM IST.

## Quick reference — the two gates
| Gate | Command | Pass |
|---|---|---|
| Script | `benchmark.py --script script.txt --script-only` | ≥85 |
| Video | `benchmark.py --project <dir> --script script.txt` (+ `--run-check`) | ≥85 + check 0 errors |
