import pyautogui
import psutil
import GPUtil
import datetime


# screenshot function
def screenshot():
    img = pyautogui.screenshot()
    # img.save(
    #     'C:\\Users\\avina\\PycharmProjects\\pythonProject\\Screenshots\\' + str()
    # )
    img.save(
        "C:\\Users\\avina\\PycharmProjects\\pythonProject\\Screenshots\\" + str(datetime.datetime.now().hour) + str(
            datetime.datetime.now().minute) + str(datetime.datetime.now().second) + str(
            datetime.datetime.now().day) + str(datetime.datetime.now().month) + str(datetime.datetime.now().year) + ".png")

    return 'Screenshot taken'


# battery and cpu usage
def cpu(q):
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
