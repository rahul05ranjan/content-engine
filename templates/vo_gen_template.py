# Gemini VO generator — CONTENT ENGINE template
# Fill SEGMENTS, point OUT at your project's assets/audio, run.
# KEY from GEMINI_KEY env or paste. Handles: 429 rotation, no-content retry,
# silence-trim, skip-existing resume, per-segment emotional delivery cues.
import base64, json, os, subprocess, time, urllib.request, urllib.error, wave

OUT = r"<PROJECT_DIR>/assets/audio"          # EDIT
os.makedirs(OUT, exist_ok=True)

BASE = (
    "You are a Hinglish storyteller for a tech shorts channel. "
    "Natural Hinglish (Roman Hindi + English tech words), talking DIRECTLY to one viewer. "
    "Punch CAPS words. Numbers as words. "
    # + channel voice rules from formats/<Channel>.md
)

# Script rules (BENCHMARK.md Phase A): hook <=12 words YOU-framed with contrast;
# every scene <=26 words; oven-moment promise; ONE hero number; 2+ crafted punch lines.
SEGMENTS = [
    # ("<name>", "<text>", "<delivery cue>"),
    ("vo1", "HOOK: tum-first line with A-vs-B contrast", "URGENT, first word immediately."),
    ("vo2", "...", "..."),
    ("vN", "OUTRO: ... LIKE kar do, SUBSCRIBE bhi. The <Channel>—", "WARM genuine ask, abrupt loop end."),
]

KEY = os.environ.get("GEMINI_KEY", "<PASTE_KEY>")   # rotate on 429
FALLBACK_KEYS = []
MODEL = "gemini-2.5-flash-preview-tts"
VOICE = "Kore"                                       # per format file


def trim_and_save(name, pcm):
    raw = os.path.join(OUT, f"{name}.raw")
    open(raw, "wb").write(pcm)
    wav = os.path.join(OUT, f"{name}.wav")
    subprocess.run(["ffmpeg", "-y", "-f", "s16le", "-ar", "24000", "-ac", "1", "-i", raw, "-af",
                    "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,"
                    "areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.15,areverse",
                    wav], check=True, capture_output=True)
    os.remove(raw)
    with wave.open(wav, "rb") as w:
        return w.getnframes() / w.getframerate()


total = 0.0
for name, text, delivery in SEGMENTS:
    final = os.path.join(OUT, f"{name}.wav")
    if os.path.exists(final):                       # resume-safe
        with wave.open(final, "rb") as w:
            total += w.getnframes() / w.getframerate()
        print(f"{name}: EXISTS", flush=True)
        continue
    payload = {"contents": [{"parts": [{"text": BASE + " Delivery: " + delivery + " "}, {"text": text}]}],
               "generationConfig": {"responseModalities": ["AUDIO"],
               "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": VOICE}}}}}
    for attempt in range(12):
        try:
            req = urllib.request.Request(
                f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
                data=json.dumps(payload).encode(),
                headers={"x-goog-api-key": KEY, "Content-Type": "application/json"})
            d = json.loads(urllib.request.urlopen(req, timeout=120).read())
            pcm = base64.b64decode(d["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
            dur = trim_and_save(name, pcm)
            total += dur
            print(f"{name}: {dur:.2f}s", flush=True)
            break
        except urllib.error.HTTPError as e:
            if e.code == 429:
                if FALLBACK_KEYS:
                    KEY = FALLBACK_KEYS.pop(0)
                else:
                    time.sleep(min(60 * (attempt + 1), 300))
            else:
                raise
        except (KeyError, IndexError):
            time.sleep(20 * (attempt + 1))
print(f"TOTAL: {total:.2f}s", flush=True)
