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