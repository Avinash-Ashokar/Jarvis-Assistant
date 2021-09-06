import pyttsx3
import speech_recognition as sr
from selenium import webdriver
import PySimpleGUI as sg
import screen_brightness_control as sbc
import pyautogui
import psutil
import GPUtil
import datetime
import pyjokes
import random
import smtplib
import requests
from ipstack import GeoLookup
import wikipedia
import wolframalpha
import os

engine = pyttsx3.init()

rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 150)  # setting up new voice rate

voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', 45)  # changing index, changes voices. 1 for female

volume = engine.getProperty('volume')
engine.setProperty('volume', 0.50)


def speak(val):
    engine.say(val)
    engine.runAndWait()


def change_voice(v):
    friday = ['female', 'Friday', 'friday']
    if contain(v, friday):
        engine.setProperty('voice', voices[1].id)
        return 'Activating Friday'
    else:
        engine.setProperty('voice', voices[0].id)
        return 'Activating Jarvis'


def get_command():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.pause_threshold = 1
        text = r.listen(source)
        try:
            recognised_text = r.recognize_google(text)
            return recognised_text
        except sr.UnknownValueError:
            print("")
        except sr.RequestError:
            print("")


def google_search(val):
    browser = webdriver.Firefox(
        executable_path='C:\\Users\\avina\\Downloads\\geckodriver-v0.28.0-win64\\geckodriver.exe')
    browser.get(url="https://www.google.com/")
    s = browser.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
    s.click()
    s.send_keys(val)
    s.send_keys('\ue007')


def youtube_search(term):
    youtube = webdriver.Firefox(
        executable_path='C:\\Users\\avina\\Downloads\\geckodriver-v0.28.0-win64\\geckodriver.exe')
    youtube.get(url="https://www.youtube.com/results?search_query=" + term)


def news_info():
    news = webdriver.Firefox(
        executable_path='C:\\Users\\avina\\Downloads\\geckodriver-v0.28.0-win64\\geckodriver.exe')
    news.get(
        url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN"
            "&ceid=IN%3Aen")


sg.theme('DarkPurple')


def input_window():
    layout = [[sg.Text("Enter the receivers mail address")],
              [sg.Input()],
              [sg.Button('Ok')]]

    window = sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True)

    event, values = window.read()
    window.close()
    return values[0]


def display_window(val):
    speak(sg.Popup(val, no_titlebar=True, button_type=5, any_key_closes=True, grab_anywhere=True))


def brightness(q):
    current_brightness = sbc.get_brightness()
    res = split(q, 'at ')
    value = res.replace('%', '')
    if ('set' in q) or ('Set' in q):
        sbc.set_brightness(int(value))
        print('Brightness is set at ' + value + '%')
        return 'Brightness is set at ' + value + '%'
    elif ('change' in q) or ('Change' in q):
        sbc.set_brightness(value)
        print('Brightness is set at ' + value + '%')
        return 'Brightness is set at ' + value + '%'
    elif 'increase' in q:
        if current_brightness == 100:
            print('This is the maximum brightness')
            return 'This is the maximum brightness'
        else:
            sbc.set_brightness(current_brightness + 10)
            print('Brightness is set at ' + str(current_brightness + 10) + '%')
            return 'Brightness is set at ' + str(current_brightness + 10) + '%'
    elif 'decrease' in q:
        if current_brightness == 0:
            print('This is the minimum brightness')
            return 'This is the minimum brightness'
        else:
            sbc.set_brightness(current_brightness - 10)
            print('Brightness is set at ' + str(current_brightness - 10) + '%')
            return 'Brightness is set at ' + str(current_brightness - 10) + '%'


def screenshot():
    img = pyautogui.screenshot()
    img.save(
        'C:\\Users\\avina\\PycharmProjects\\pythonProject\\Screenshots\\{0}{1}{2}{3}{4}{5}.png'.format(
            str(datetime.datetime.now().hour), str(
                datetime.datetime.now().minute), str(datetime.datetime.now().second), str(
                datetime.datetime.now().day), str(datetime.datetime.now().month), str(datetime.datetime.now().year)))

    return 'Screenshot taken'


def system_status(q):
    if 'cpu status' in q:
        usage = str(psutil.cpu_percent())
        print('CPU usage is at ' + usage)
        return 'CPU usage is at ' + usage
    elif 'battery status' in q:
        battery = psutil.sensors_battery()
        print("Battery is at " + str(battery.percent) + '%')
        return "Battery is at " + str(battery.percent) + '%'
    elif 'card' in q:
        gpus = GPUtil.getGPUs()
        print('GPU Name: ' + str(gpus[0].name))
        print('GPU load is at ' + str(gpus[0].load) + ' %')
        print('Temperature at ' + str(gpus[0].temperature) + ' degree celsius')
        return 'GPU Name: ' + str(gpus[0].name) + 'GPU load is at ' + str(
            gpus[0].load) + ' %' + 'Temperature at ' + str(gpus[0].temperature) + ' degree celsius'
    else:
        usage = str(psutil.cpu_percent())
        gpus = GPUtil.getGPUs()
        print('CPU usage is at ' + usage + '%')
        battery = psutil.sensors_battery()
        print("Battery is at " + str(battery.percent) + '%')
        print('Disk usage is at ' + str(psutil.disk_usage('/').percent) + '%')
        print('Ram Usage is at ' + str(psutil.virtual_memory().percent) + '%')
        print('Temp at ' + str(gpus[0].temperature) + 'degree celsius')
        return 'Disk usage is at ' + str(psutil.disk_usage('/').percent) + '%' + "Battery is at " + str(
            battery.percent) + '%' + 'Ram Usage is at ' + str(psutil.virtual_memory().percent) + '%' + 'Temp at ' + str(
            gpus[0].temperature) + ' degree celsius'


def time():
    ctime = datetime.datetime.now()
    hour = ctime.hour
    minute = str(ctime.minute)
    if hour > 12:
        hour = hour - 12
        t = str(hour) + ' ' + minute + ' ' + 'pm'
        print(t)
    else:
        t = str(hour) + ' ' + minute + ' ' + 'am'
        print(t)
    return t


def date():
    month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
             9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    d = str(month.get(datetime.datetime.now().month)) + ' ' + str(datetime.datetime.now().day) + 'th'
    print(d)
    return d


def jokes():
    j = pyjokes.get_joke()
    print(j)
    return j


def play():
    songs_dir = "C:\\Users\\avina\\PycharmProjects\\pythonProject\\music"
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir, songs[random.randrange(0, len(songs))]))
    quit()


def send_mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("jarvis.from.ultron@gmail.com", "jarvisvision")
    server.sendmail("jarvis.from.ultron@gmail.com", to, content)
    server.close()


def location():
    geo_lookup = GeoLookup("d5d0a475fe36f223581ca6e48c05a062")
    my_location = geo_lookup.get_own_location()
    return my_location.get("city")


def weather(city_name):
    api_key = "e50752ecec7c3d19c12076d9c326978a"  # generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]['description']
        result = ('in ' + city_name + ' Temperature is ' +
                  str(int(current_temperature - 273.15)) + ' degree celsius ' +
                  ', atmospheric pressure ' + str(current_pressure) + ' hpa unit' +
                  ', humidity is ' + str(current_humidity) + ' percent'
                                                             ' and ' + str(weather_description))
        print(result)
        return result
    else:
        return 'City not found'


def wiki_summary(val):
    return wikipedia.summary(val, sentences=2)


def take_notes(val):
    note = open('notes.txt', 'a')
    note.write(val)
    note.write(" ")
    note.close()
    print('Notes taken sir')


def read_notes():
    note = open('notes.txt', 'r')
    data = note.read()
    note.close()
    if data != '':
        print(data)
        return data
    else:
        return 'Notes are empty'


def start(command):
    if 'pycharm' in command:
        speak("Opening Pycharm")
        source = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"
        os.startfile(source)

    elif 'resolve' in command:
        speak("Opening Epic Games")
        path = "C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\Resolve.exe"
        os.startfile(path)

    elif 'code' in command:
        speak('Opening Visual Studio Code')
        path = "C:\\Users\\avina\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)

    elif 'games' in command:
        speak('Opening Epic Games')
        path = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
        os.startfile(path)

    elif 'Firefox' in command:
        speak('Opening Firefox')
        path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        os.startfile(path)


def remember(val):
    file = open('data.txt', 'w')
    hy = open('history.txt', 'a')
    file.write(val)
    hy.write(" ")
    hy.write(val)
    file.close()
    hy.close()
    print('Noted down sir')


def reminder():
    file = open('data.txt', 'r')
    data = file.read()
    file.close()
    if data == "":
        return "You didn't told me to remember anything"
    else:
        print(data)
        return data


def history():
    hy = open('history.txt', 'r')
    data = hy.read()
    hy.close()
    if data == "":
        return "You didn't told me to remember anything"
    else:
        print(data)
        return data


app_id = 'QP3PU3-2732W55TG7'
client = wolframalpha.Client(app_id)


def wolf_search(val):
    res = client.query(val)
    return next(res.results).speak


def check(sentence, words):
    res = [all([k in s for k in words]) for s in sentence]
    return [sentence[i] for i in range(0, len(res)) if res[i]]


def split(variable, keyword):
    mystring = variable
    before_keyword, keyword, after_keyword = mystring.partition(keyword)
    return after_keyword


def contain(variable, keyword):
    for k in keyword:
        if k in variable:
            return True


def clean(variable, keyword):
    edit_string_as_list = variable.split()
    final_list = [word for word in edit_string_as_list if word not in keyword]
    final_string = ' '.join(final_list)
    return final_string


def functions(dvar):
    reminder_history_keywords = ['history', 'command', 'comments', 'comment']
    read_notes_keyword = ['read', 'note']
    voice = ['voice', 'activate']
    google = ['Search', 'search', 'in', 'Google', 'google', 'Find', 'find']
    youtube = ['Search', 'search', 'in', 'YouTube', 'youtube']
    wolf = ['Search', 'search', 'in', 'Yahoo', 'yahoo']
    song = ['song', 'songs', 'Song', 'Songs', 'music', 'Music']
    joke = ['joke', 'Joke', 'Jokes', 'Joke', 'Comedy', 'comedy', 'funny', 'Funny']
    jarvis = ['terminate', 'offline', 'Offline', 'Terminate']
    mail = ['Email', 'mail', 'email', 'Mail']
    time_keyword = ['current time', 'present time', 'time now']
    remin = ['you to remind', 'you to remember']
    if dvar is not None:
        if "time" in dvar:
            if contain(dvar, time_keyword):
                val = "The time is " + str(time())
                speak(val)
                print(val)
                return 'online'
        elif "remember that" in dvar:
            remember(split(dvar, "remember that"))
            speak("Noted down sir")
            return 'online'
        elif contain(dvar, remin):
            v = reminder()
            speak(v)
            return 'online'
        elif check(list(dvar.split("$")), reminder_history_keywords):
            h = history()
            speak(h)
            return 'online'
        elif 'take notes' in dvar:
            speak("taking notes")
            speak(take_notes(get_command()))
            return 'online'
        elif check(list(dvar.split("$")), read_notes_keyword):
            speak(read_notes())
            return 'online'
        elif contain(dvar, jarvis):
            speak('Jarvis shutting down')
            return 'offline'
        elif 'open' in dvar:
            start(dvar)
            return 'offline'
        elif "date" in dvar:
            speak(date())
            return 'online'
        elif contain(dvar, voice):
            speak(change_voice(dvar))
            return 'online'
        elif contain(dvar, song):
            speak("Playing Songs...")
            play()
            return 'offline'
        elif contain(dvar, mail):
            try:
                to = input_window()
                speak("What is the content for the email")
                print('Listening...')
                content = get_command()
                print(content)
                send_mail(to, content)
                speak("Email has sent")
                display_window(
                    'Sender\'s Mail Address: your-mailaddress@gmail.com\nReceiver\'s mail address: {0}\nDate: {'
                    '1}\nTime: {2}\nContent: {3}'.format(
                        str(to), str(date()), str(time()), str(content)))
                return 'online'
            except Exception as e:
                print(e)
                speak("Unable to send email check the address of the recipient")
                return 'online'
        elif contain(dvar, joke):
            speak(jokes())
            return "online"
        elif 'status' in dvar:
            speak(system_status(dvar))
            return 'online'
        elif "logout" in dvar:
            speak('Logging Out')
            os.system("shutdown -1")
            return 'offline'
        elif "restart" in dvar:
            speak('system restarting')
            os.system("shutdown /r /t 1")
            return 'offline'
        elif "shut down" in dvar:
            speak('System Shutting down')
            os.system("shutdown /r /t 1")
            return 'offline'
        elif "weather" in dvar:
            speak(weather(location()))
            return 'online'
        elif 'screenshot' in dvar:
            speak(screenshot())
            return 'online'
        elif 'brightness' in dvar:
            speak(brightness(dvar))
            return 'online'
        elif 'news' in dvar:
            news_info()
            return 'offline'
        elif 'Google' in dvar:
            google_search(clean(dvar, google))
            return 'offline'
        elif 'YouTube' in dvar:
            youtube_search(clean(dvar, youtube))
            return 'online'
        elif 'Yahoo' in dvar:
            wol = wolf_search(clean(dvar, wolf))
            print(wol)
            speak(wol)
            return 'online'
        else:
            print('These are the current functions I am capable of ', '\n', '1. Tell Time', '\n',
                  '2. Remember few lines',
                  '\n', '3. Take Notes')
            return 'online'
    else:
        print('Please give me some command')
        return 'online'


def status(val):
    if val == 'online':
        print('listening...')
        command = get_command()
        print(command)
        var = functions(command)
        status(var)
    else:
        print('program is ended')


speak("Jarvis at your service sir")
status('online')
