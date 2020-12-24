

from scipy.io.wavfile import write

import pyttsx3

ttsengine = pyttsx3.init()
voices = ttsengine.getProperty("voices")
ttsengine.setProperty("voice", voices[0].id)
# saving speech audio into a file

print(voices)
text = "hello there, how are you doing?"
# ttsengine.save_to_file(text, "python.mp3")
# ttsengine.say(text)
# ttsengine.runAndWait()

def save_speech(input="Placeholder text"):
    # ttsengine.save_to_file(input, "tts/speech/speech.mp3")
    # ttsengine.save_to_file(input, "tts/speech/speech.mp3")
    ttsengine.say(input)
    ttsengine.runAndWait()