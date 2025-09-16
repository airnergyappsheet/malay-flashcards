Bundle with placeholders and scripts
-----------------------------------
- public/vocab.json : full vocab list
- public/audio/ : placeholder .mp3/.ogg files (empty) for each vocab item
- generate_full_audio_offline.py : script to generate real audio (requires espeak-ng & ffmpeg)
- verify_audio.py : verifies presence of mp3 + ogg files
- generate_and_verify.bat : runs generation + verification (double-click)

IMPORTANT: Placeholders are empty files. To create real audio, install eSpeak NG and ffmpeg, then run the generator script.
