<<<<<<< HEAD
import pyaudio
import numpy as np
import speech_recognition as sr
def audio_gen(temp=3):
    p = pyaudio.PyAudio()
    volume = 1
    fs = 44100
    duration = temp
    f = 550
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
    samples
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)
    stream.write(volume*samples)
    stream.stop_stream()
    stream.close()
    p.terminate()
def audio_get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        voice = r.listen(source)
    try:
        return r.recognize_google(voice, language="ru-RU")
    except sr.UnknownValueError:
        print("The robot did not hear the phrase")
    except sr.RequestError as e:
        print("Service error {0}".format(e))
=======
import pyaudio
import numpy as np
import speech_recognition as sr
def audio_gen(temp=3):
    p = pyaudio.PyAudio()
    volume = 1
    fs = 44100
    duration = temp
    f = 550
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
    samples
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)
    stream.write(volume*samples)
    stream.stop_stream()
    stream.close()
    p.terminate()
def audio_get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        voice = r.listen(source)
    try:
        return r.recognize_google(voice, language="ru-RU")
    except sr.UnknownValueError:
        print("The robot did not hear the phrase")
    except sr.RequestError as e:
        print("Service error {0}".format(e))
>>>>>>> Some error have exists
