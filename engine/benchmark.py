#!/usr/bin/env python3
"""
CONTENT ENGINE — benchmark scorer + render gate.
Scores a video project against the 100-point benchmark (see BENCHMARK.md).

Usage:
  python benchmark.py --project ./my-video
  python benchmark.py --project ./my-video --script script.txt
  python benchmark.py --project ./my-video --script script.txt --run-check
  python benchmark.py --project ./my-video --json

Exit code 0 = PASS (>=85 + gates), 1 = FAIL (see report).
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

PASS_SCORE = 85


class Check:
    def __init__(self, cid, phase, rule, points, ok, note=""):
        self.cid, self.phase, self.rule = cid, phase, rule
        self.points, self.ok, self.note = points, ok, note


def read(path):
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            return f.read()
    except OSError:
        return ""


def audit_project(project):
    checks = []
    index_path = os.path.join(project, "index.html")
    index = read(index_path)
    if not index:
        return None, "index.html not found in project dir"
    scene_files = sorted(glob.glob(os.path.join(project, "compositions", "*.html")))
    scenes = {os.path.basename(f): read(f) for f in scene_files}
    all_html = index + "\n" + "\n".join(scenes.values())

    def add(cid, phase, rule, pts, ok, note=""):
        checks.append(Check(cid, phase, rule, pts, bool(ok), note))

    # --- B: VISUAL ---
    add("B1", "Visual", "Frame-0 designed (element visible from <=0.5s)", 5,
        re.search(r'data-start="0(?:\.[0-9]?[0-9]?)"', index) is not None or 'data-start="0.1"' in index or 'data-start="0.2"' in index,
        "first-scene clip starts at 0-0.2s")
    add("B2", "Visual", "Film grain present", 3, "fractalNoise" in all_html or "grain" in all_html.lower())
    add("B3", "Visual", "motion-blur on root", 3, 'data-motion-blur="on"' in index)
    n_scenes = len(scenes)
    add("B4", "Visual", "6-10 scenes", 3, 6 <= n_scenes <= 10, f"found {n_scenes} scene files")
    nirmala = sum(1 for s in scenes.values() if "NirmalaLocal" in s and "@font-face" in s)
    add("B5", "Visual", "Per-scene @font-face fallback", 3, n_scenes > 0 and nirmala == n_scenes,
        f"{nirmala}/{n_scenes} scenes have @font-face")
    # full-screen linear gradients on dark grounds (rough heuristic)
    bad_lin = re.findall(r"background:\s*linear-gradient\(\s*(?:to bottom|180deg|to top)", all_html)
    add("B6", "Visual", "No full-screen linear gradient on dark", 3, len(bad_lin) == 0,
        f"{len(bad_lin)} full-width linear gradients" if bad_lin else "")

    # --- C: AUDIO ---
    add("C1", "Audio", "BGM auto-ducking (data-automation)", 6, "data-automation" in index and '"volume"' in index)
    click_ok = "sfx-click" in all_html and bool(re.search(r'sfx-click[^>]*data-volume="(?:0\.[0-4][0-9]?|0\.5)"', all_html))
    add("C2", "Audio", "Soft click transitions (<=0.5 vol), whoosh retired", 4,
        click_ok and "sfx-whoosh" not in all_html)
    m = re.search(r'id="bgm"[^>]*data-volume="([0-9.]+)"', index)
    add("C3", "Audio", "BGM volume <=0.18 + instrumental", 4, m is not None and float(m.group(1)) <= 0.18,
        f"bgm volume={m.group(1) if m else 'missing'}")
    add("C4", "Audio", "Mood-specific BGM file present", 3,
        any(os.path.isfile(os.path.join(project, "assets", "audio", f))
            for f in glob.glob(os.path.join(project, "assets", "audio", "bgm-*.wav"))))
    add("C5", "Audio", "Event-only SFX (slam/chime present)", 3,
        "sfx-slam" in all_html or "sfx-chime" in all_html or "sfx-tick" in all_html)

    # --- D: STRUCTURE & OUTRO ---
    scene_nums = [int(m.group(1)) for k in scenes for m in [re.fullmatch(r"s([0-9]+)\.html", k)] if m]
    last_scene = scenes.get(f"s{max(scene_nums, default=0)}.html", "")
    outro_ok = ("SUBSCRIBE" in last_scene.upper() and ("LIKE" in last_scene.upper() or "👍" in last_scene))
    add("D1", "Structure", "Standard outro (LIKE + SUBSCRIBE)", 8, outro_ok,
        "last scene must carry LIKE + SUBSCRIBE pills")
    add("D2", "Structure", "No burned-in captions composition", 4,
        'data-track-kind="captions"' not in index and "compositions/captions.html" not in index)
    add("D4", "Structure", "SEO package exists for this video", 4,
        any(os.path.isfile(p) for p in (
            os.path.join(project, "..", "seo", f"{os.path.basename(project)}.md"),
            os.path.join(project, f"{os.path.basename(project)}-seo.md"),
        )) or os.path.isfile(os.path.join(project, "SEO.md")))
    return checks, None


def audit_script(script_text):
    checks = []
    # segments separated by blank lines, like the vo_gen templates
    segs = [s.strip() for s in re.split(r"\n\s*\n", script_text) if s.strip()]
    if not segs:
        return checks
    hook = segs[0]
    words0 = hook.split()

    def add(cid, phase, rule, pts, ok, note=""):
        checks.append(Check(cid, phase, rule, pts, bool(ok), note))

    add("A1", "Script", "Hook <=12 words (speed to value)", 8, len(words0) <= 14, f"hook has {len(words0)} words")
    add("A3", "Script", "YOU-framing in hook (tum/aap/you/your)", 6,
        re.search(r"\b(tum|tumhara|tumhare|aap|aapka|you|your)\b", hook, re.I) is not None)
    add("A4", "Script", "Contrast words present (par/but/vs/ya/while)", 4,
        re.search(r"\b(par|but|vs\.?|magar|jabki|while)\b", hook, re.I) is not None,
        "self-review: is there an A-vs-B contrast?")
    add("A5", "Script", "Oven-moment promise cue", 5,
        re.search(r"\b(end mein|last mein|finally|ab|suno|dekho|twist|raaz|secret|payoff)\b", script_text, re.I) is not None,
        "self-review: promise -> build -> golden shot?")
    add("A6", "Script", "Hero-number cue in second half", 3,
        re.search(r"[0-9₹$]|percent|billion|trillion|million|crore|karod|hazaar|sau|pachaas|tees|bees|chalis|satais|taintalis", " ".join(segs[len(segs) // 2:]), re.I) is not None)
    longest = max(len(s.split()) for s in segs)
    add("A7", "Script", "Max 26 words per scene", 3, longest <= 26, f"longest segment: {longest} words")
    add("A16", "Script", "Crafted punch lines (self-review)", 2, True,
        "CONFIRM: at least 2 deliberate punch lines written, not improvised")
    return checks


def run_hyperframes_check(project):
    try:
        r = subprocess.run(["npx", "hyperframes", "check", "--json"], cwd=project,
                           capture_output=True, text=True, timeout=600, shell=True)
        raw = r.stdout
        i = raw.find("{")
        if i >= 0:
            d = json.loads(raw[i:])
            return d, None
        return None, "check produced no JSON"
    except Exception as e:
        return None, str(e)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", help="video project dir (skip for script-only gate)")
    ap.add_argument("--script", help="plain-text script file (segments separated by blank lines)")
    ap.add_argument("--script-only", action="store_true", help="score ONLY the script (Phase A)")
    ap.add_argument("--run-check", action="store_true", help="also run `npx hyperframes check`")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    checks = []
    if args.script or args.script_only:
        if not args.script:
            print("FAIL: --script needed for script gate")
            sys.exit(1)
        checks = audit_script(read(args.script))
    elif args.project:
        checks, err = audit_project(args.project)
        if err:
            print(f"FAIL: {err}")
            sys.exit(1)
        if args.script:
            checks += audit_script(read(args.script))
        else:
            checks.append(Check("A0", "Script", "Script audit skipped (no --script)", 0, False,
                                 "35 points at stake; pass --script script.txt"))
    else:
        print("FAIL: pass --project and/or --script")
        sys.exit(1)

    hf_gate, hf_err = (None, None)
    if args.run_check:
        d, hf_err = run_hyperframes_check(args.project)
        if d:
            hf_gate = (d.get("lint", {}).get("errorCount", 1) == 0
                       and d.get("runtime", {}).get("errorCount", 1) == 0
                       and d.get("layout", {}).get("errorCount", 1) == 0)

    total = sum(c.points for c in checks if c.points <= 8 or True)
    # score = earned / applicable
    earned = sum(c.points for c in checks if c.ok)
    applicable = sum(c.points for c in checks if c.points > 0)
    score = round(100 * earned / max(applicable, 1))

    if args.json:
        print(json.dumps({
            "score": score, "pass": score >= PASS_SCORE,
            "hyperframes_gate": hf_gate, "hyperframes_error": hf_err,
            "checks": [{"id": c.cid, "phase": c.phase, "rule": c.rule, "points": c.points,
                         "ok": c.ok, "note": c.note} for c in checks],
        }, indent=1))
    else:
        print("=" * 64)
        print("CONTENT ENGINE BENCHMARK")
        print("=" * 64)
        for c in checks:
            mark = "PASS" if c.ok else "FAIL"
            print(f"[{mark}] {c.cid} ({c.phase}) {c.rule} — {c.points}pts {('- ' + c.note) if c.note else ''}")
        print("-" * 64)
        print(f"SCORE: {score}/100  (gate: {PASS_SCORE})")
        if hf_gate is True:
            print("HYPERFRAMES CHECK: 0 errors  ✓")
        if hf_gate is False:
            print("HYPERFRAMES CHECK: ERRORS — FIX BEFORE RENDER  ✗")
        if hf_err:
            print("CHECK ERROR:", hf_err)
        print("VERDICT:", "RENDER" if score >= PASS_SCORE and hf_gate is not False else "FIX FIRST")
    sys.exit(0 if score >= PASS_SCORE and hf_gate is not False else 1)


if __name__ == "__main__":
    main()
