# CHANNEL FORMAT SPEC — The Curious Cast (@TheCuriousCastOg)
**Version 1.2 — LOCKED Oct 31, 2026. Any agent on any machine MUST follow this exact format.**
**RENDER ENGINE: HyperFrames ONLY (Remotion retired Oct 31, user directive).**
**File ki copy har machine pe honi chahiye. Naya agent = ye file padho, phir video banao.**

---

## 1. CHANNEL IDENTITY
- **Channel:** The Curious Cast (youtube.com/@TheCuriousCastOg)
- **Type:** Hinglish tech explainers (AI, hardware, security, India-tech)
- **Format:** YouTube Shorts + Instagram Reels, **1080×1920 @ 30fps, 90–140s**
- **Voice:** Gemini TTS, voice **"Kore"** (gemini-2.5-flash-preview-tts, responseModalities AUDIO)
- **Delivery:** Full-quality MP4 → `C:\Users\rahus\Downloads\` (ya jis machine ka Downloads folder ho)

## 2. SCRIPT FORMULA (MANDATORY — viewer-first, approved)
1. **Hook (scene 1):** "TUM/AAP" se start — kabhi "companies/OpenAI/X" se nahi. Relatable anchor (tumhara phone, ChatGPT). 1 curiosity punch.
2. **Analogy (scene 2-3):** Desi, physical (corridor/sadak, spinning coin, restaurant recipe). "Aise samjho..." anchor 3-5x per script.
3. **Reveal (scene 4):** Bada number/fact — awe delivery.
4. **Twist (scene 5):** "Lekin ek DHOKE ki baat" — myth-buster, deadpan.
5. **Payoff (scene 6):** **ONE hero number only** (3 numbers kabhi ek saath nahi). Count-up 1.2-1.6s, tabular-nums.
6. **Uses/claim (scene 7):** India connect jab ho sake. "India bhi khel raha hai" pride beat.
7. **Outro (scene 8):** STANDARD OUTRO (section 7).
- **Pacing:** ~19 spoken words per scene (max 26). TTS ≈ 2.2 words/sec. 8 scenes ≈ 155 words max.
- **Numbers Hindi mein bolein:** "taintalis" not "43", "satais" not "27".

## 3. VISUAL STANDARD (HyperFrames — MANDATORY)
- **Engine:** HyperFrames (`npx hyperframes init <project>`), GSAP 3.14.2, `data-motion-blur="on"` on root.
- **Safe band:** y250–1440 (top 220px + bottom ~480px UI-free).
- **Frame 0 = THUMBNAIL:** designed, kabhi black/logo-only nahi. Hero text visible from t=0 (punch-settle scale 1.15→1).
- **Fonts:** Display = **Archivo Black**; Body = **Inter**; Mono/labels = **Space Mono**; Hindi fallback = `@font-face { font-family: "NirmalaLocal"; src: local("Nirmala UI"); }` — **HAR scene file mein** @font-face required.
- **Palette:** ground #06090a-family dark; accent PER-MOOD (amber heist, green machine, blue-violet quantum...); danger #ef4444. **NO linear gradients on dark** (H.264 banding) — radial ya solid.
- **Film grain:** static SVG fractalNoise texture, opacity 0.12, z-index 50, har scene mein (deterministic — CSS animation NAHI).
- **Entrances VARIED (banned: same fade+slide har scene):** per-word blur-in (blur 6px→0, 0.13s, stagger 0.067s), grey→ink words, whip-in (x:220+blur), punch-settle scale, evidence slide-left. Exits 40-50% shorter.
- **Banned tells:** 3-cards-in-a-row (vertical stagger list use karo), dark void + floating UI, glow/particles on titles, HUD readouts, everything centered.
- **Transitions:** scene seams pe **SOFT CLICK SFX** (`sfx-click.wav`, data-volume 0.45 — whoosh RETIRED). 2-4 real transitions-with-cause per film (dip-cut, colour flood, whip, blur swap).
- **3D — ONLY WHERE NEEDED (user rule Oct 31: "jaha zarurat pde waha use krna hai"):** 3D har video mein default NAHI. Jab topic visual depth demand kare (GPU rack, quantum, coin physics, product showcase) tabhi Three.js scene. Warna 2D + GSAP hi standard. Three.js pattern: `<script type="importmap">` + deterministic `renderAt(t)` + `window.addEventListener("hf-seek", e => renderAt(e.detail.time))` + `window.__hf.buildReady["<key>"] = Promise.resolve()`. Library: `C:\Users\rahus\hyperframes-3d-lib\lib\compositions\` (20 blocks). Optional 3D brand intro available (demo s0 particle-sphere) — sirf jab channel branding demand kare, default OFF.
- **Aurora bg blocks** for non-footage scenes: compositions/aurora-vert.html mount at root (DOM-first, track 0).

## 4. CAPTIONS STANDARD — **OFF (user decision Oct 31)**
- **NO burned-in bottom captions** — user ne band kiya ("niche me jo caption dikhta hai wo bnd kro"). Karaoke pill captions AB add nahi karne. Captions host/track hi mat banao. (YouTube ke auto-captions apne aap aate hain — vo theek hai.)

## 5. AUDIO STANDARD
- **VO:** Gemini Kore, per-segment emotional delivery cue prompt (BASE + "Delivery: ..."). 429 → rotate keys + 20-120s backoff + skip-existing resume. `silenceremove` trim (start -45dB/0.05, end -45dB/0.15 via areverse).
- **BGM:** mood-specific HAR video (kabhi repeat nahi): somber/satire/academia/carbon/glitch/ocean/anthem/heist/machine/quantum... — numpy-synth 110-130s, data-volume 0.14-0.16.
- **DUCKING (MANDATORY):** BGM pe `data-automation` volume lane — 1.0 between VOs, **0.5 under each VO window** (points: [s-0.3=1, s+0.1=0.5, e-0.1=0.5, e+0.3=1], t clip-relative).
- **SFX:** slam (hook stamp, 0.85-0.9 vol), soft click (transitions, 0.45 vol). Event-only, kabhi constant nahi.

## 6. BUILD PIPELINE (exact steps)
1. `npx hyperframes init <project>` → assets copy (aurora-vert, shaders, sfx, footage)
2. VO gen script (Gemini, key-rotation, skip-existing) → background run
3. BGM gen (numpy, new mood)
4. 8 scene files s1-s8.html (`<template>`, inline GSAP `window.__timelines["sN"]`)
5. index.html: scenes + captions host + audio (VO/BGM/ducking/SFX) + `window.__timelines["main"]` empty timeline + root `__timelines` registration (index root timeline registration REQUIRED for lint)
6. Build script (python): exact VO durations se retime + captions generate
7. **`npx hyperframes check --json`** — MUST be: lint 0, runtime 0, layout 0 (fix until clean)
8. `npx hyperframes snapshot --review` — frames rich (not tiny/blank)
9. `npm run render` → copy to Downloads (2 files: YT + `-IG-reel.mp4` same video)
10. SEO package → `gyaansetu-growth/content/<slug>-seo.md`

## 7. ⭐ STANDARD OUTRO (HAR VIDEO MEIN — MANDATORY)
- **VO last segment mein (brand se pehle):** "Aur haan — video PASAND aayi toh LIKE kar do, aur aisi stories ke liye SUBSCRIBE bhi. The Curious Cast—"
- **Visual end-card (s8/sN last scene):** brand lockup "THE CURIOUS CAST—" (gradient text, scale 1.3→1, blur 10px→0, power4.out, lands DEAD STILL) + **SUBSCRIBE button pill (red #ef4444, "SUBSCRIBE" text) + LIKE (👍) pill** — dono brand ke neeche, 0.35s stagger pop-in, phir hold till end. Abrupt loop ending (no fade-out — "- " se cut for Shorts loop).
- **Pinned comment (har video):** video ka viewer-question + "👇"

## 8. SEO TEMPLATE
- **Title:** Hinglish caps punch + emoji + "| The Curious Cast" (e.g. "Tumhara ChatGPT — 43% POWER PAANI ho rahi hai! 🖥️ | The Curious Cast")
- **Description:** hook line → "→" bullet points (5-7 facts) → one-line claim → source line → channel line + follow CTA → 💬 viewer question → 10-15 hashtags (#TechNewsHindi #Hinglish #CuriousCast + topic tags)
- **2 alternate titles** for A/B. Tags: 10-15 comma-separated Hinglish+English mix.
- **IG Reel version:** same MP4; caption = 3 hook lines + summary + "full video YouTube pe" + 20 hashtags.

## 9. NEW CHANNELS
- Har naye channel ke liye ALAG file banao isi folder mein: `channel-formats/<ChannelName>.md` (same template, alag identity/look/voice/structure).
- Agent ko bolna: "channel-formats/<name>.md follow karke video banao" — bas.
