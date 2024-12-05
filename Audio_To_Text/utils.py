from pydub import AudioSegment
import io
from docx import Document

# Function to convert any audio file to WAV format
def extract_audio_from_file(audio_file):
    try:
        audio = AudioSegment.from_file(audio_file)
        audio_wav = io.BytesIO()
        audio.export(audio_wav, format="wav")
        audio_wav.seek(0)  # Reset the pointer to the start of the file
        return audio_wav
    except Exception as e:
        raise ValueError(f"Error processing audio file: {e}")

# Function to convert text to a TXT file
def convert_to_txt(response):
    try:
        return str(response).encode('utf-8', errors='ignore')
    except Exception as e:
        raise ValueError(f"Error converting to TXT: {e}")

# Function to convert text to a DOCX file
def convert_to_docx(response):
    try:
        doc = Document()
        doc.add_heading("Translated", 1)
        doc.add_paragraph(response)
        file_stream = io.BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)
        return file_stream
    except Exception as e:
        raise ValueError(f"Error converting to DOCX: {e}")
