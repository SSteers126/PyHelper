import ctypes

myappid = u'Zestyy.PyHelper.Win.V0BETA' # these lines are used to seperate the app from the python 'umbrella'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import urllib.request as urllib3

import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
recogniser = sr.Recognizer()

import pyaudio, wave

def record(time=3, samplerate = 44100, output="stt/recorded/recorded.wav"):
    # recording = sd.rec(int(time * samplerate), samplerate=samplerate, channels=2)
    # sd.wait()  # Wait until recording is finished
    # write(output, samplerate, recording)  # Save as WAV file

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = samplerate  # Record at 44100 samples per second
    seconds = time
    filename = output

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def conv_offline(input="stt/recorded/recorded.wav"):
    # open the file
    with sr.AudioFile(input) as source:
        # listen for the data (load audio to memory)
        audio_data = recogniser.record(source)
        # recognize (convert from speech to text)
        text = recogniser.recognize_sphinx(audio_data)
        return text

def conv_online(input="stt/recorded/recorded.wav"):
    # open the file
    with sr.AudioFile(input) as source:
        # listen for the data (load audio to memory)
        audio_data = recogniser.record(source)
        # recognize (convert from speech to text)
        text = recogniser.recognize_google(audio_data)
        return text

# conv_online("../16-122828-0002.wav")

# from gtts import gTTS
# import os

# # define variables
# s = "hello there"
# file = "file.mp3"
#
# # initialize tts, create mp3 and play
# tts = gTTS(s, 'en')
# ttmp3 = gTTS(text=s, lang="en", tld="translate.google.com")
# tts.save(file)
# os.system("mpg123 " + file)