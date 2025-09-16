@echo off
cd /d %~dp0
echo Generating audio (this requires espeak-ng and ffmpeg)...
python generate_full_audio_offline.py
echo Verifying audio...
python verify_audio.py
pause
