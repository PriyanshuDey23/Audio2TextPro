from gtts import gTTS
import os

# Define the text
text = """India, officially the Republic of India,[j][20] is a country in South Asia. It is the seventh-largest country in the world by area and the most populous country. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[k] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia.

Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago.[22][23][24] Their long occupation, initially in varying forms of isolation as hunter-gatherers, has made the region highly diverse, second only to Africa in human genetic diversity.[25] Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago, evolving gradually into the Indus Valley Civilisation of the third millennium BCE.[26] By at least 1200 BCE, an archaic form of Sanskrit, an Indo-European language, had diffused into India from the northwest.[27][28] Its evidence today is found in the hymns of the Rigveda. Preserved by an oral tradition that was resolutely vigilant, the Rigveda records the dawning of Hinduism in India.[29] The Dravidian languages of India were supplanted in the northern and western regions.[30] By 400 BCE, stratification and exclusion by caste had emerged within Hinduism,[31] and Buddhism and Jainism had arisen, proclaiming social orders unlinked to heredity.[32] Early political consolidations gave rise to the loose-knit Maurya and Gupta Empires based in the Ganges Basin.[33] Their collective era was suffused with wide-ranging creativity,[34] but also marked by the declining status of women,[35] and the incorporation of untouchability into an organised system of belief.[l][36] In South India, the Middle kingdoms exported Dravidian-languages scripts and religious cultures to the kingdoms of Southeast Asia"

"""
# Create a gTTS object
tts = gTTS(text=text, lang='en')

# Save the audio file
tts.save("test_audio.mp3")