import requests
from ipstack import GeoLookup


def weather():
    geo_lookup = GeoLookup("d5d0a475fe36f223581ca6e48c05a062")
    location = geo_lookup.get_own_location()
    l = location.get("city")
    return w(l)


# weather condition

def w(city_name):
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
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidity) + ' percent'
                                                        ' and ' + str(weather_description))
        print(r)
        return r
    else:
        return 'City not found'
