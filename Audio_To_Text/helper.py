import os
from dotenv import load_dotenv
import google.generativeai as genai
import tempfile
from pydub import AudioSegment
import speech_recognition as sr

# Load environment variables
load_dotenv()

# Configure the Google API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")
genai.configure(api_key=GOOGLE_API_KEY)

# Function to initialize the generative model
def get_model():
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        return model
    except Exception as e:
        raise ValueError(f"Error initializing the model: {e}")

# Function to upload audio and generate a summary
def summarize_audio(audio_file_path):
    """Summarize audio using Google's Generative API."""
    try:
        model = get_model()
        audio_file = genai.upload_file(path=audio_file_path)
        response = model.generate_content(
            [
                "Please summarize the following audio.",
                audio_file
            ]
        )
        return response.text
    except Exception as e:
        raise ValueError(f"Error summarizing audio: {e}")

# Function to save uploaded audio file
def save_uploaded_file(uploaded_file):
    """Save uploaded audio file to a temporary file."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        raise ValueError(f"Error saving uploaded file: {e}")

# Function to extract text from audio using Google's Generative API
def audio_to_text(audio_file_path):
    """Convert audio to text using Google's Generative API."""
    try:
        model = get_model()
        # Upload audio file to Google API
        audio_file = genai.upload_file(path=audio_file_path)
        # Request the model to transcribe audio to text
        response = model.generate_content(
            [
                "Please transcribe the following audio.",
                audio_file
            ]
        )
        return response.text
    except Exception as e:
        raise ValueError(f"Error converting audio to text: {e}")
