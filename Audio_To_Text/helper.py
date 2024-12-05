import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from Audio_To_Text.prompt import PROMPT

# Load environment variables
load_dotenv()

# Configure the Google Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")
genai.configure(api_key=api_key)

# Initialize the LLM model globally
model = genai.GenerativeModel("gemini-1.5-flash-8b")

# Function to convert audio to text using SpeechRecognition
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    # Use SpeechRecognition to process the uploaded audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            text = "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            text = f"Could not request results from Google Speech Recognition service; {e}"

    return text


# Function to summarize text using the LLM
def llm_model(user_input):
    prompt = PROMPT.format(user_input=user_input)
    response = model.generate_content(prompt)
    return response.text
