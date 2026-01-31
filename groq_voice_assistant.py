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
