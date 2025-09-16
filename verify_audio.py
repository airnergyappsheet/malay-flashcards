# verify_audio.py
import os, json
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
VOCAB_PATH = os.path.join(PROJECT_ROOT, "public", "vocab.json")
with open(VOCAB_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
OUT_DIR = os.path.join(PROJECT_ROOT, "public", "audio")
missing = []
total = 0
for cat, items in data.items():
    for item in items:
        malay = item if isinstance(item, str) else item.get("malay", "")
        malay = malay.strip()
        if not malay: continue
        fname = f"{cat}_{malay.replace(' ','_')}".lower()
        total += 1
        mp3 = os.path.join(OUT_DIR, fname + ".mp3")
        ogg = os.path.join(OUT_DIR, fname + ".ogg")
        if not os.path.exists(mp3) or not os.path.exists(ogg):
            missing.append(fname)
print(f"Checked {total} items.")
if missing:
    print(f"Missing {len(missing)} files:")
    for m in missing:
        print(' -', m)
else:
    print('All files present!')
