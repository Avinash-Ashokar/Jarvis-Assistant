import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 150)  # setting up new voice rate

voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', 45)  # changing index, changes voices. 1 for female
engine.setProperty('voice', voices[0].id)


volume = engine.getProperty('volume')
engine.setProperty('volume', 0.50)


def text(val):
    engine.say(val)
    engine.runAndWait()


def contain(variable, keyword):
    for k in keyword:
        if k in variable:
            return True


def voice_change(v):
    friday = ['female', 'Friday', 'friday']
    if contain(v, friday):
        engine.setProperty('voice', voices[1].id)
        return'Activating Friday'
    else:
        engine.setProperty('voice', voices[0].id)
        return 'Activating Jarvis'
