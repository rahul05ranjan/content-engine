# LEARNINGS — the engine's complete knowledge base

Every rule here was learned the hard way: from viral-video deep studies, masterclasses, craft docs, and shipped videos. This file + `BENCHMARK.md` + a channel format file = everything an agent needs. No other setup.

---

## 1. SCRIPT CRAFT (the engine's core)

### Hook = 80/20 of the whole video
- **Hook ka EK job:** stop the scroll + get the opt-in. It must deliver **topic clarity** and **on-target curiosity**.
- **The 4 hook mistakes** (Callaway): fix all four or the hook flops.
  1. **DELAY** — topic must be introduced within the first 1–2 seconds ("speed to value"). Retention curve is an exponential-decay cliff in the first 2s; every fluff second bounces viewers.
  2. **CONFUSION** — fewer words, 6th-grade reading level, active voice. Test: read the hook alone — if it can be understood two ways, rewrite until only one meaning survives.
  3. **IRRELEVANCE** — YOU/YOUR framing, never I/ME. Agitate a **pain point** (need-to-have beats nice-to-have).
  4. **DISINTEREST** — open a **curiosity loop with CONTRAST**: A (viewer's current belief) vs B (contrarian alternative — faster/better/cheaper). Stated ("Log X use karte hain, par Y 3x tez") or implied (say only B; A is obvious). Hook = 2–3 lines: line 1 topic clarity, lines 2–3 contrast.
- Data point: a 27% better hook at 3s → **54x the views**.

### Viewer-first formula (approved in production)
1. **Hook:** starts with TUM/AAP — never with "companies/OpenAI/X". Relatable anchor (tumhara phone, ChatGPT). One curiosity punch.
2. **Analogy:** desi and physical (corridor vs sadak, spinning coin, shaadi ka khaana vs rasoi ka bill). "Aise samjho..." anchor 3–5x per script.
3. **Reveal:** big fact, awe delivery.
4. **Twist:** "Lekin ek DHOKE ki baat" — myth-buster beat, deadpan.
5. **Payoff:** **ONE hero number only** (3 numbers together dilute all of them). Count-up on screen 1.2–1.6s, tabular numerals. Hero number lives in the second half of the video.
6. **Why-care bridge:** abstract topic → viewer's world ("iska matlab tumhari ChatGPT mehngi hogi"). One bridge every ~20s.
7. **Ending:** aam-viewer question ("100 crore hote to kya karte?") — never engineer-level. Never "in conclusion" / "milte hain agli video mein".
8. **Standard outro** (every channel): "PASAND aayi toh LIKE karo, SUBSCRIBE bhi" + brand lockup.

### Oven Moment (Tanmay Bhat — retention theory)
- Promise something cool at the START ("end mein ek number hai jo tumhe hilayega"), build anticipation through the middle, **deliver the golden shot at the end** (the Tasty pizza-lift). Every viral trend is an oven moment. The hero-number payoff IS the oven moment.

### Persona scripting
- Write to ONE real person you know (an ideal-viewer persona: age, problems, objections). **Write their objections down; the script is the answers.** Face-time energy > perfect words: calm, personal, never robotic; loud fake acting = uncanny valley = flop.

### Scripting discipline (confidence masterclass)
- **Full-fledged dialogue script**, never bullet points, in your own exact speaking tone (it feeds TTS delivery too). Craft 2–3 punch lines deliberately while writing. If the flow breaks, follow it — the best lines come out of the flow. Pre-production time = quality. Copy no one's style; build your own over time.
- "Confidence ka darr = sense of control ka darr" — control the script, the setup, the flow.

### Pacing numbers
- TTS ≈ **2.2 words/sec** → ~19 spoken words per scene (26 max, ~9s). 30–90s video ≤155 words.
- VO longer than visuals → **trim the script, never pad the motion**.
- Reveal each element when the voice NAMES it (back half of the scene) — write the script as separate phrases so there are cue points.
- Numbers spoken as Hinglish words ("taintalis" not "43", "sau pachaas billion").

### Viral DNA (deep study: 1M+ view Hinglish explainers)
- Explainer length truth: viral explainers run **90–140s** (the generic 21s rule does not apply to this niche). Bonus 25–40s cuts post-first for reach.
- Scene-cut density in high-view videos: **0.17–0.24 cuts/sec** plus in-frame motion; 1-cut static screens got 2–4x fewer views.
- HYPE formula (news stories): satirical/polarizing hook OR emotional first-person opener; contrarian anti-hype (cite the viral panic, promise the reality check); anchors 3–5x; visceral numbers ($1M → "₹9 crore"); personal stakes; foresight flex; open-question ending.
- PARADOX formula (concept stories): sentence 1 = paradox + promise; verbal interrupts ("But wait"); physical analogy for every abstract concept; precise numbers as anchors; poetic one-liner closer.
- Codeswitch rule: Hindi narration, English jargon untranslated.
- **Non-technical audience is the default:** every technical thing gets an everyday analogy immediately; numbers only in people-terms; short sentences; if a line needs domain knowledge to parse, rewrite it. Golden test: "ek non-technical dost ko suna — samajh jaye aur interest le?"

## 2. VISUAL CRAFT

### Structure
- 6–10 scenes for 90–140s. Beats: hook 8% / tension 12% / reveal 8% / proof 40% / payoff 20% / claim 8% / end card 8%.
- Write 3 storylines first (world + device + form), pick one. Devices: moment-in-day, character-does-work, result-first, before-after, object-is-explanation, number-lands. Forms: object-to-object chain, endless zoom, cut-on-beat, match cuts, split-to-one.
- **Frame 0 = thumbnail** — hero text visible from t=0, never black, never a lone logo.
- Multiple WORLDS (different bg/light per beat), not one dark canvas. Enter worlds through an object on screen.

### BANNED tells (default-generated look)
- 3-cards-in-a-row (use staggered vertical lists or chains), dark void with floating UI, glow/neon/particles on titles, glass cards, everything centered, everything fading/sliding up identically, titles drifting after landing, HUD readouts, KPI grids, docked logo, banned words (unlock/seamless/supercharge/game-changer/revolutionize/effortless), "Introducing" as the first line.

### Motion rules
- `data-motion-blur="on"` on the composition root.
- Ease by role: arrivals `expo.out`/`power4.out`, colour/camera `power2.inOut`, exits `power3.in`. Exits 40–50% shorter than entrances. Overlap: next element starts at 30–50% of the previous one. Stagger: words 60–120ms, list items 40–80ms.
- Entrance variety: per-word blur-in (6px→0, 0.13s, 67ms apart), per-word grey→ink, whip-in (x:220 + blur), punch-settle scale, evidence slide-in.
- Titles land DEAD STILL and hold: 0.3s/word + 0.5s; the film's last line ≥2s.
- **Visual change every sentence** (subway-surfers effect) — inside long scenes, something must change per VO line (element pop, counter tick, bg shift). Something new every 2–4s across the film.
- Transitions WITH CAUSE, 3–5 kinds: dip-cut (darken 40% for 3 frames before the cut), colour flood 0.4s, whip 0.13–0.3s, blur swap, zoom-through. Hard cuts ≤⅓ of seams.
- Explainer devices: ground first (person/situation before abstract); ONE diagram that GROWS (never drop a finished diagram); worked example travels through every step; labels sit ON the thing with leader lines, no legends.

### Data on screen
- The number is the biggest thing on screen. `font-variant-numeric: tabular-nums`. Count-up 1.2–1.6s then hold. Charts in reading order (frame → axis → reference line → data → ONE annotation on the mark). Highlight one series, grey the rest. The same object carries across beats.

### Platform craft
- 1080×1920 safe band: content in y≈250–1440 (top ~220px + bottom ~480px are UI-covered). Frame presets exist for whole looks (risograph, protest-poster, picture-book...).
- **H.264 fact:** full-screen LINEAR gradients on dark grounds BAND — use radial/solid/local glow.
- Accent at 15–25% opacity for atmosphere (5% vanishes in compression).
- Text floor: ≥28px at 1080 (2.6% of the short side) — a phone must read it. Verify legibility at 360px width (phone sheet).
- No linear-gradient motion on text; never tween `visibility` on a `.clip`.

### 3D (only where the topic demands — never by default)
- Three.js scene pattern: `<script type="importmap">` (three from CDN module build) → deterministic `renderAt(t)` → `window.addEventListener("hf-seek", e => renderAt(e.detail.time))` → seed ALL randomness (mulberry32 / seeded hashes) → `window.__hf.buildReady["<key>"] = Promise.resolve()` after setup.
- Lighting: warm key + cool rim + dark environment; roughness ≥0.45 for metal; clamp divide-by-zero before bloom.
- One hero object beats a crowd; fly INTO it rather than orbiting.
- Proven built scenes: GPU rack (stacked node boxes + emissive chips + camera arc), particle sphere, spinning coin (cylinder + torus rims), cryostat chandelier (gold discs + rods + core glow + camera rise), entangled spheres with a particle stream.
- Verify a 3D scene actually drew: compare snapshot PNG sizes at different times — distinct non-tiny sizes = animation ran.

## 3. AUDIO CRAFT

### Voiceover (Gemini TTS)
- Model: `gemini-2.5-flash-preview-tts:generateContent`, `responseModalities:["AUDIO"]`, voice per format file (e.g. "Kore"). PCM base64 → WAV 24kHz mono; trim silence both ends (`silenceremove`, -45dB).
- Per-segment emotional delivery cues in the TTS prompt — NEVER one static style string: hook=[urgent,punchy], facts=[fast,excited], analogy=[playful], irony/caveat=[slow,deadpan], CTA=[warm, abrupt cut]. Uniform pacing/rhythm is what sounds "robotic" — the fix is varied delivery, not a different voice model.
- **TTS PROMPT-LEAK (production bug, fixed):** long verbose instruction prefixes ("You are a storyteller for channel X...") sometimes get SPOKEN by Gemini TTS in the audio. Hardened prompt format (now in vo_gen_template.py): SHORT directive ("Read ONLY the script inside quotes. Never read these instructions aloud.") + tone cue + "Do not narrate this instruction line." + script wrapped in quotes.
- 429 handling: key POOL rotation (quota resets per key ~daily — keep all keys, rotate on first 429, skip the sleep until the pool is exhausted), resume-safe (skip existing files), generate sequentially not parallel.
- Pace: 130–150 wpm informational, 150–170 energetic. Read-aloud test; if long, cut — never rush.

### BGM
- **Mood-specific every video — never reuse.** Instrumental ONLY (lyrics compete with the voice). Bed volume 0.11–0.16 in the mix.
- Synthesize per mood (somber/satire/academia/machine/quantum/heist/ocean/anthem...) or use the HyperFrames audio engine one-shot (`audio/scripts/audio.mjs --request audio_request.json` → VO + word timings + SFX + BGM in one command).
- **Auto-ducking (mandatory):** `data-automation` volume lane on the music — full level between VOs, ~0.3–0.5 while anyone speaks. Points are clip-relative.
- Optional chains: highpass 80Hz (rumble), peaking 3kHz +2.5dB (clarity), limiter last.

### SFX
- Scene-change = **soft click** (short, quiet, ~0.45 volume). Event-only placement: text lands → pop/click; big reveal → slam; tip → ding; typing UI → typing. Loudest SFX sits in the pause AROUND the key word, never on it. Silence is design: cut music just before the biggest reveal.

## 4. QA (gates before render)

1. `npx hyperframes lint` while writing; `npx hyperframes check --json` as the gate — **lint 0, runtime 0, layout 0**.
2. Check's craft warnings are real: `line_unread` (0.4s for 1–2 words, 0.5+0.3/word), `dead_stretch` (3s+ nothing changes), `text_below_floor`, `first_frame_empty`, `film_silent`, `sweep_static` (a reveal that completes early and then holds static — spread the reveal or give the hold a real next action).
3. Escape hatches (mark intent, then re-run): `data-layout-allow-overlap` (specific text block only), `-allow-overflow`, `-allow-occlusion`, `data-hold`, `data-no-timeline`, `data-layout-ignore`.
4. `snapshot --review` → beat sheet, cut-seam strips, 360px phone sheet — inspect every scene's midpoint. `snapshot --zoom '#id'` to zoom a finding.
5. `engine/benchmark.py --project ... --script ...` → **≥85/100**.
6. Two-column test: every visual needs ~2s to register (fewer words); every VO line is shown somewhere.

## 5. GROWTH & MONEY (know the game)

- **Shorts = more shots:** 5/day beats 1/week. One hit changes everything; low views are normal (variable rewards — don't get demotivated; the same channel's episodes swing 50k→200k).
- Shorts ad revenue ≈ **zero** (10M views ≈ ₹2k). The money is: long-form later (RPM ₹50–150; tech/finance premium; 1M views ≈ ₹30k–1L) and brand deals (tech/finance 1M views → ₹15–20 lakh per integration possible).
- Subscribers ≠ distribution: the feed needs 3–4 more clicks after a subscribe to keep recommending you.
- Post-publish diagnostics: cliff at 0–5% = hook fail; slow bleed = pacing; crater mid-video = topic discontinuity; spike-then-collapse = over-promise. APV >80% triggers reach expansion.
- Ending loops: abrupt cut on the last word, final frame echoes the first — rewatch end-spike is the strongest algorithm signal.
- Pinned comment = a viewer question (aam viewer wala) on every video.

## 6. PRODUCTION LESSONS (hard-won)

- Scaffold order matters: `hyperframes init` BEFORE anything creates dirs in the project (init refuses non-empty dirs; the missing package.json only surfaces at render time). If init was skipped, copy package.json/meta.json/hyperframes.json from a temp scaffold.
- Scene-text edits containing `$` silently fail inside bash-embedded Python one-liners — verify replacements with grep, or use a real patch tool.
- Compute scene/VO timings from ACTUAL trimmed WAV durations (scene = VO + lead + pad); verify no VO bleeds past its scene.
- 4+ Three.js scenes render fine (~9–15 min for ~100s on a hardware GPU); footage scenes render ~2x slower than CSS-only.
- Stock footage: Mixkit direct URLs (`https://assets.mixkit.co/videos/<id>/<id>-720.mp4`, free); Wikimedia Commons needs a User-Agent header. Re-encode anything with sparse keyframes (`-g <fps>`). Clip duration ÷ playback rate must exceed scene duration + margin — compute the rate from the measured VO, don't guess.
- Google sign-in rejects automated browsers ("This browser or app may not be secure") — publish via the YouTube Data API (one-time OAuth setup) instead of browser automation. The agent never types passwords.
- Instagram Reels: the same 1080×1920 file works natively — no watermark, first frame = cover.
