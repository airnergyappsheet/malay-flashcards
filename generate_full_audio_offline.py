# generate_full_audio_offline.py
import os, json, subprocess, shutil, sys
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
VOCAB_PATH = os.path.join(PROJECT_ROOT, "public", "vocab.json")
ESPEAK = shutil.which("espeak-ng.exe") or shutil.which("espeak-ng")
FFMPEG = shutil.which("ffmpeg")
if ESPEAK is None or FFMPEG is None:
    print("Please ensure espeak-ng and ffmpeg are installed and in PATH.")
    sys.exit(1)
with open(VOCAB_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
OUT_DIR = os.path.join(PROJECT_ROOT, "public", "audio")
os.makedirs(OUT_DIR, exist_ok=True)
def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr)
for cat, items in data.items():
    for item in items:
        malay = item if isinstance(item, str) else item.get("malay", "")
        malay = malay.strip()
        if not malay: continue
        fname = f"{cat}_{malay.replace(' ','_')}".lower()
        wav = os.path.join(OUT_DIR, fname + ".wav")
        mp3 = os.path.join(OUT_DIR, fname + ".mp3")
        ogg = os.path.join(OUT_DIR, fname + ".ogg")
        run([ESPEAK, "-v", "ms", "-s", "140", "-w", wav, malay])
        run([FFMPEG, "-y", "-i", wav, "-vn", "-c:a", "libmp3lame", "-q:a", "2", mp3])
        run([FFMPEG, "-y", "-i", wav, "-vn", "-c:a", "libvorbis", "-qscale:a", "5", ogg])
        try: os.remove(wav)
        except: pass
print("Done")
