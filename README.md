# Content Engine

**Benchmark-driven video production engine.** Every video passes ONE engine; every channel plugs in its own format file.

```
┌─────────────────────────────────────────────┐
│                CONTENT ENGINE                │
│                                             │
│  1. SCRIPT   persona → hook checklist →     │
│              oven-moment → hero number       │
│  2. PRODUCE   format file (per channel) →    │
│              VO → BGM → scenes → build       │
│  3. GATE      engine/benchmark.py ≥85/100    │
│              + hyperframes check = 0 errors  │
│  4. SHIP      render → SEO package → post    │
└─────────────────────────────────────────────┘
```

## Quickstart

```bash
# 1. Pick the channel format
#    → formats/<ChannelName>.md (add one per channel)

# 2. Write the script through the engine's script rules
#    (BENCHMARK.md §Script — persona, hook 4/4, oven moment, hero number)

# 3. Produce the video with your pipeline (HyperFrames / Remotion / anything)

# 4. Run the gate
python engine/benchmark.py --project ./my-video --script script.txt
python engine/benchmark.py --project ./my-video --script script.txt --run-check

# 5. PASS (>=85) → render + SEO template. FAIL → fix the report's reds.
```

## What's inside

| Path | What |
|---|---|
| `docs/PIPELINE.md` | **The zero-setup workflow** — topic → script gate → VO → BGM → build → gates → render → SEO → publish. An agent reads this and starts producing. |
| `docs/LEARNINGS.md` | **The complete knowledge base** — every learned rule: hook science (4 mistakes), viewer-first formula, oven moment, persona scripting, viral DNA, visual/motion craft, banned tells, audio craft (delivery cues, ducking, SFX), QA gates, growth & money math, hard-won production lessons. |
| `BENCHMARK.md` | The 100-point benchmark — every rule, why it exists, and its source (Tanmay Bhat, Callaway, retention science, HyperFrames craft docs) |
| `engine/benchmark.py` | Automated scorer + render gate (script-only mode AND project audit mode) |
| `formats/TheCuriousCastOg.md` | Channel format v1.1 — the first channel spec (identity, script formula, visual/audio standards, outro, SEO) |
| `templates/vo_gen_template.py` | Gemini TTS VO generator (key rotation, backoff, skip-existing, per-segment emotional delivery cues) |
| `templates/seo_template.md` | SEO package template (title/description/tags/pinned comment/IG) |

## The zero-setup promise

Give any agent this repo and a topic. It reads `docs/PIPELINE.md` + `docs/LEARNINGS.md` + `formats/<Channel>.md`, and produces a benchmark-passing video end-to-end: script → gate → VO → build → gate → render → SEO. No hidden state, no external dependencies beyond Node + FFmpeg + a Gemini key.

## The rules the engine encodes

- **Hook = 80/20** — topic in first 2s, single interpretation, YOU-framing + pain point, A-vs-B contrast. *(Callaway's 4 hook mistakes)*
- **Oven Moment** — promise at the start, build anticipation, deliver the golden shot at the end. *(Tanmay Bhat)*
- **Viewer persona** — write to ONE real person; pre-empt their objections.
- **Full-fledged script** in your own speaking tone; punch lines are crafted, not found. *(scripting masterclass)*
- **Visual change every sentence**; instrumental-only music; soft click transitions; auto-ducked BGM. *(retention science + user feedback)*
- **One hero number** per video; 3 cards-in-a-row banned; frame-0 = designed thumbnail. *(HyperFrames craft)*
- **Standard outro** — LIKE + SUBSCRIBE, every video, every channel.

## Adding a channel

Copy `formats/TheCuriousCastOg.md` → `formats/<YourChannel>.md`, change the identity/look/structure. The engine and benchmark stay identical.

## Status

Built while producing The Curious Cast (youtube.com/@TheCuriousCastOg). MIT license — use it, break it, make it better.
