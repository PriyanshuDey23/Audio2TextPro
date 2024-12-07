
# Audio2Text with Summarization

This project is an audio-to-text conversion tool with additional summarization capabilities, powered by Google's Generative AI. It allows users to upload audio files (in WAV or MP3 format), transcribe the audio to text, and summarize the content. The app also supports downloading the transcribed and summarized text in both TXT and DOCX formats.

## **Features**
- **Audio-to-Text Conversion**: Converts audio files to text using Google Generative AI.
- **Summarization**: Summarizes the transcribed text for concise understanding.
- **Download Options**: Download the transcribed or summarized content as TXT or DOCX files.

## **Tech Stack**
- **Streamlit**: For creating the interactive web application.
- **Google Generative AI**: For transcribing and summarizing the audio.
- **gTTS (Google Text-to-Speech)**: For text-to-speech functionality.
- **SpeechRecognition**: For converting audio to text using Google's speech recognition API.
- **Pydub**: For handling audio file manipulations.
- **Python-docx**: For creating DOCX files.

## **Installation**

### Prerequisites

- Python 3.6 or higher.
- Google API Key for accessing Google's Generative AI services.

### Steps to Set Up

1. **Clone the Repository:**
   ```bash
   git clone git clone https://github.com/PriyanshuDey23/Audio2TextPro.git
   cd Audio2Text-with-Summarization
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   - Create a `.env` file in the root directory of the project.
   - Add your Google API key:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

### **Usage**

- Upload an audio file (WAV or MP3 format).
- Choose either to transcribe the audio to text or summarize the content.
- View the extracted or summarized text and download it as TXT or DOCX files.

## **File Structure**

```plaintext
Audio2Text-with-Summarization/
├── app.py               # Main Streamlit app file
├── helper.py            # Helper functions for processing audio
├── utils.py             # Utilities for converting text to TXT/DOCX
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (for storing API keys)
└── README.md            # Project documentation
```

## **Contributing**

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
