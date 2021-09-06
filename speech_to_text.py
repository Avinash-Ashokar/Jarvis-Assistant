import speech_recognition as sr

def speech():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.pause_threshold = 1
        text = r.listen(source)
        try:
            recognised_text = r.recognize_google(text)
            return recognised_text
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")