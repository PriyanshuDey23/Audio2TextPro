import streamlit as st
from Audio_To_Text.utils import convert_to_txt, convert_to_docx
from Audio_To_Text.helper import save_uploaded_file, summarize_audio, audio_to_text

# Streamlit App Configuration
st.set_page_config(page_title="Audio2Text with Summarization", layout="centered")
st.title("Audio2Text with Summarization")



# Upload audio file with file size limit (50 MB)
audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3"])
if audio_file is not None:
    # Save and display uploaded audio
    try:
        audio_path = save_uploaded_file(audio_file)
        st.audio(audio_path)
    except ValueError as e:
        st.error(f"Error saving the uploaded file: {e}")
        st.stop()

    # Action selection
    action = st.radio(
        "What would you like to do?",
        ("Convert to Text", "Summarize the Audio")
    )

    # Button to process audio
    if st.button("Process Audio"):
        with st.spinner("Processing..."):
            try:
                if action == "Convert to Text":
                    extracted_text = audio_to_text(audio_path)
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
                elif action == "Summarize the Audio":
                    summarized_text = summarize_audio(audio_path)
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
            except ValueError as e:
                st.error(f"Error processing the audio: {e}")
else:
    st.info("Please upload an audio file to get started.")
