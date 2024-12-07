from gtts import gTTS
import os

# Define the multiline text
text = """India, officially the Republic of India, is a country in South Asia. 
It is the seventh-largest country in the world by area and the most populous country. 
Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, 
it shares land borders with Pakistan to the west; China, Nepal, and Bhutan to the north; 
and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; 
its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia."""

# Create a gTTS object
tts = gTTS(text=text, lang='en')

# Save the audio file
tts.save("test_audio.mp3")

# Optionally, play the audio (if on a system with a sound player)
os.system("start test_audio.mp3")  # For Windows
