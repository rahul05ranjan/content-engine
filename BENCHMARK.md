# The Benchmark — 100 points, render gate at 85

Every video is scored by `engine/benchmark.py` (automated) against these rules.
A video that scores below 85, or fails `hyperframes check`, does NOT get rendered.

## Phase A — SCRIPT (35 points)

| # | Rule | Pts | Source |
|---|---|---|---|
| A1 | **Topic clarity in first 2 seconds** — no fluff lines before the topic sentence ("speed to value") | 8 | Callaway mistake #1 (delay). Retention = exponential decay cliff in first 2s. |
| A2 | **Single interpretation** — the hook read alone cannot be understood two ways | 4 | Callaway mistake #2 (confusion). 6th-grade words, active voice. |
| A3 | **YOU/YOUR framing + pain point** in the hook — never I/ME | 6 | Callaway mistake #3 (irrelevance). Need-to-have beats nice-to-have. |
| A4 | **A-vs-B contrast** (stated or implied) within first 3 lines — viewer's current belief vs contrarian alternative | 6 | Callaway mistake #4 (disinterest). Contrast = curiosity loop opener. |
| A5 | **Oven moment** — explicit promise near the start, anticipation cues mid-way, golden-shot payoff at the end | 5 | Tanmay Bhat (Tasty pizza). Every viral trend is an oven moment. |
| A6 | **ONE hero number** — a single number gets the spotlight; supporting numbers stay background | 3 | User-approved formula (NVL72 v2). 3 numbers together dilute all. |
| A7 | **≤26 spoken words per scene** (~19 target; TTS ≈2.2 words/sec) | 3 | HyperFrames film.md pacing science. |

*(A1–A5 are scored by the script checklist in `benchmark.py --script`; the scorer checks word counts and YOU-framing automatically, contrast/oven-moment are flagged as self-review when not detected heuristically.)*

## Phase B — VISUAL (25 points)

| # | Rule | Pts | Source |
|---|---|---|---|
| B1 | **Frame 0 = designed thumbnail** — hero text/visual visible from t=0, never black | 5 | HyperFrames craft (`first_frame_empty`). Social players use frame 0. |
| B2 | **Film grain** texture present (static, deterministic) | 3 | Channel format v1.1. |
| B3 | **motion-blur on** (`data-motion-blur="on"` on root) | 3 | HyperFrames motion.md. |
| B4 | **6–10 scenes** in 90–140s | 3 | Explainer shape; beat density. |
| B5 | **Per-scene `@font-face` fallback** for Devanagari (NirmalaLocal) | 3 | HyperFrames format lint. |
| B6 | **No full-screen linear gradients on dark grounds** (H.264 banding) — radial/solid only | 3 | HyperFrames look.md video facts. |
| B7 | **Visual change every sentence** inside long scenes (element pop, tick, shift) — not only at beats | 5 | Retention science ("subway-surfers effect", 54x-view data). |

## Phase C — AUDIO (20 points)

| # | Rule | Pts | Source |
|---|---|---|---|
| C1 | **BGM auto-ducking** (`data-automation` volume lane: 1.0 between VOs, ~0.5 under VO) | 6 | HyperFrames mixing.md + user-approved NVL72 v2 mix. |
| C2 | **Soft click transitions** (`sfx-click` ≤0.5 volume); whoosh retired | 4 | User decision Oct 31 ("dhima click"). |
| C3 | **BGM bed volume ≤0.18** and instrumental-only (no lyrics) | 4 | Mixing rules; lyrics compete with voice. |
| C4 | **Mood-specific BGM, never reused** across videos | 3 | User directive (Oct 28). |
| C5 | **Event-only SFX** (slam on hook stamp etc.), nothing constant | 3 | HyperFrames sound.md. |

## Phase D — STRUCTURE & OUTRO (20 points)

| # | Rule | Pts | Source |
|---|---|---|---|
| D1 | **Standard outro present** — LIKE + SUBSCRIBE elements in final scene + VO ask | 8 | User directive Oct 31 (all channels). |
| D2 | **Burned-in bottom captions ABSENT** | 4 | User decision Oct 31. |
| D3 | **Channel format file followed** (identity/look/structure) | 4 | Multi-channel system. |
| D4 | **SEO package complete** (title + 2 alternates + description + tags + pinned comment) | 4 | Distribution discipline. |

## Gates (independent of score)

1. `hyperframes check --json` → **lint 0, runtime 0, layout 0** (contrast warnings: fix or justify).
2. `benchmark.py` total **≥ 85/100**.
3. No banned tells: 3-cards-in-a-row, same entrance every scene, glow/particles on titles, HUD decoration, docked logo.

## The learning sources

- **Tanmay Bhat** (OnePlus Open Conversations Ep1): oven moment, variable rewards, subscriber ≠ distribution, money math.
- **Callaway** (4 hook mistakes): delay, confusion, irrelevance, disinterest.
- **Scripting masterclass** (Hindi): full-fledged dialogue scripts, crafted punch lines, confidence = control.
- **Growth/retention science**: 27% better hook = 54x views; feel > think; visual change per sentence.
- **HyperFrames craft docs**: story/motion/look/sound/film/mixing/review (learned Oct 30, 2026).
- **User decisions**: soft clicks, captions off, one BGM mood per video, standard outro, 3 videos/day target.
