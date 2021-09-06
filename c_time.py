import datetime


def current_time():
    ctime = datetime.datetime.now()
    hour = ctime.hour
    minute = str(ctime.minute)
    if hour > 12:
        hour = hour - 12
        time = str(hour) + ' ' + minute + ' ' + 'pm'
        print(time)
    else:
        time = str(hour) + ' ' + minute + ' ' + 'am'
        print(time)
    return time


def date():
    month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
             9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    d = str(month.get(datetime.datetime.now().month)) + ' ' + str(datetime.datetime.now().day) + 'th'
    print(d)
    return d
