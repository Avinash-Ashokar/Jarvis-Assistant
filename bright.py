# importing the module
import screen_brightness_control as sbc


# get current brightness value

def split(variable, keyword):
    mystring = variable
    before_keyword, keyword, after_keyword = mystring.partition(keyword)
    return after_keyword


def bright(q):
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
