import os
import subprocess
from datetime import datetime

AUDIO_IN = "audio/input.wav"
AUDIO_OUT = "audio/response.wav"
LOGS_DIR = "logs"

def main():
    os.makedirs(LOGS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(LOGS_DIR, f"call_{timestamp}.txt")

    # 1. Transcribe
    transcript = subprocess.check_output(["python", "whisper_transcribe.py", AUDIO_IN], text=True).strip()

    # 2. LLM reply
    reply = subprocess.check_output(["python", "llm_reply.py", transcript], text=True).strip()

    # 3. TTS
    subprocess.run(["python", "tts_generate.py", reply, AUDIO_OUT])

    # 4. Log
    with open(log_file, "w") as f:
        f.write(f"Transcript: {transcript}\n")
        f.write(f"AI Reply: {reply}\n")
        f.write(f"Audio In: {AUDIO_IN}\n")
        f.write(f"Audio Out: {AUDIO_OUT}\n")

if __name__ == "__main__":
    main() 