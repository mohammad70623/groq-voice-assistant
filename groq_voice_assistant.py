import os
import sounddevice as sd
import soundfile as sf
from groq import Groq
from dotenv import load_dotenv
import tempfile
import pyttsx3

# Load API key
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)


# Audio recording
def record_audio(duration=5, fs=44100):
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    sf.write(tmp_file.name, recording, fs)
    return tmp_file.name

# STT using Groq
def transcribe(file_path):
    with open(file_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            file=f,
            model="whisper-large-v3-turbo"
        )
    return transcription.text

# Generate response using Groq LLM
def generate_response(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content


# TTS playback
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Main pipeline
if __name__ == "__main__":
    audio_file = record_audio(duration=5)
    user_text = transcribe(audio_file)
    print("You said:", user_text)
    
    bot_response = generate_response(user_text)
    print("Bot says:", bot_response)
    
    speak(bot_response)