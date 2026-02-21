import whisper

# Load Whisper model once globally
model = whisper.load_model("base")  # tiny, base, small

def transcribe_audio(file_path: str) -> str:
    result = model.transcribe(file_path)
    return result["text"]