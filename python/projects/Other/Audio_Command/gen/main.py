import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    voice = r.listen(source)
try:
    print(r.recognize_google(voice, language="ru-RU"))
except sr.UnknownValueError:
    print("The robot did not hear the phrase")
except sr.RequestError as e:
    print("Service error {0}".format(e))
