
# Audio2TextPro with Summarization

This project allows you to convert audio files into text and summarize the extracted text using a Generative Language Model (Google Gemini). It utilizes the power of SpeechRecognition for audio processing and a custom LLM for text summarization. The output can be downloaded in TXT or DOCX formats.

## Features

- Convert audio (MP3, WAV, FLAC) to text using the SpeechRecognition library.
- Summarize extracted text using a language model.
- Download the extracted or summarized text in TXT or DOCX formats.
- Streamlit-based UI for easy interaction.

## Prerequisites

- Python 3.10+
- ffmpeg (required by `pydub` for audio file conversion)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PriyanshuDey23/Audio2TextPro.git
   cd audio2text-summarization
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install ffmpeg:
   - **Windows**: Download `ffmpeg` from [ffmpeg.org](https://ffmpeg.org/download.html) and add the `bin` folder to your system’s PATH.
   - **macOS**: Install via Homebrew:
     ```bash
     brew install ffmpeg
     ```
   - **Linux**: Install via package manager:
     ```bash
     sudo apt-get install ffmpeg
     ```

## Environment Variables

You will need to set up your Google API key to interact with the Google Gemini model. Create a `.env` file in the root directory of the project with the following content:

```
GOOGLE_API_KEY=your_google_api_key_here
```

## Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to `http://localhost:8501` to interact with the application.

## Usage

1. Upload an audio file (MP3, WAV, or FLAC).
2. Choose whether you want to:
   - Convert the audio to text.
   - Summarize the extracted text.
3. The extracted or summarized text will appear on the screen.
4. You can download the text in TXT or DOCX format.

## Contributing

Feel free to fork the repository, make changes, and create pull requests. If you encounter any issues, please open an issue in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
