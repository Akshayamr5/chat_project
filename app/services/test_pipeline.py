import os
import whisper

# Force FFmpeg path manually
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

model = whisper.load_model("base")

def transcribe_audio(file_path: str) -> str:
    result = model.transcribe(file_path, fp16=False)
    return result["text"]