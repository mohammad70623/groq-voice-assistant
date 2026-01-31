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