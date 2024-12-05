import streamlit as st
from Audio_To_Text.utils import extract_audio_from_file, convert_to_txt, convert_to_docx
from Audio_To_Text.helper import audio_to_text, llm_model

# Streamlit App UI
st.set_page_config(page_title="Audio2Text with Summarization", layout="centered")
st.header("Audio2Text with Summarization")

# Function to handle audio file upload
def get_audio_input():
    return st.file_uploader("Upload an audio file", type=["mp3", "wav", "flac"])

# Display the upload section
uploaded_audio = get_audio_input()

if uploaded_audio:
    st.audio(uploaded_audio, format="audio/mp3")

    # Convert uploaded audio to WAV for processing
    try:
        audio_wav = extract_audio_from_file(uploaded_audio)
    except ValueError as e:
        st.error(str(e))
        st.stop()

    # Provide options for action
    action = st.radio(
        "What would you like to do with the text?",
        ("Convert to Text", "Summarize the Text")
    )

    if st.button("Process Audio"):
        st.info("Processing audio...")
        extracted_text = audio_to_text(audio_wav)

        if action == "Summarize the Text":
            summarized_text = llm_model(extracted_text)
            st.text_area("Summarized Text", summarized_text, height=300)
            st.download_button(
                label="Download as TXT",
                data=convert_to_txt(summarized_text),
                file_name="summarized_text.txt",
                mime="text/plain",
            )
            st.download_button(
                label="Download as DOCX",
                data=convert_to_docx(summarized_text),
                file_name="summarized_text.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        else:
            st.text_area("Extracted Text", extracted_text, height=300)
            st.download_button(
                label="Download as TXT",
                data=convert_to_txt(extracted_text),
                file_name="extracted_text.txt",
                mime="text/plain",
            )
            st.download_button(
                label="Download as DOCX",
                data=convert_to_docx(extracted_text),
                file_name="extracted_text.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
else:
    st.info("Please upload an audio file to get started.")
