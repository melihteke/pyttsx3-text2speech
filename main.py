import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties
rate = engine.getProperty('rate')   # Get the current speech rate
engine.setProperty('rate', rate - 25)  # Decrease the speech rate

# Text to be spoken
text = "Hello, this is a text-to-speech test."

# Speak the text
engine.say(text)
engine.runAndWait()
