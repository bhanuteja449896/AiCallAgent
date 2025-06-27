import sys
from TTS.api import TTS

def tts(text, output_path):
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
    tts.tts_to_file(text=text, file_path=output_path)

if __name__ == "__main__":
    tts(sys.argv[1], sys.argv[2]) 