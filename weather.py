# import requests
# import math
# TOKEN = '5603688976:AAEKZQ1m7SyzJMouAMVYfrmYB3LSrvnIPK4'

# city_name= 'Bukhara'

# def get_request(city_name, TOKEN):
#     bot_json = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates').json()
#     city_json = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=ba5f0db5da7eed99dc585cd6a768b237').json()
#     return city_json, bot_json 

# def get_request_city(city_name):
#     city_json = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=ba5f0db5da7eed99dc585cd6a768b237').json()
#     return city_json 

# def get_info_city(city_json):
#     city_name = city_json['name']
#     today = city_json['weather'][0]['main']
#     description = city_json['weather'][0]['description']
#     wind = city_json['wind']['speed']
#     city_temp = round((city_json['main']['temp'] - 273.15), 2)
#     pressure = city_json['main']['pressure']
#     humidity = city_json['main']['humidity']

#     if today == 'Clouds':
#         text = f'City: {city_name} \nToday: {today} ☁️\nTemperatura: {city_temp}°C \nDescription: {description} \nWind: {wind} m/s \nPressure: {pressure} Pa \nHumidity: {humidity}%'
#     elif today == 'Rain':
#         text = f'City: {city_name} \nToday: {today} 🌧\nTemperatura: {city_temp}°C \nDescription: {description} \nWind: {wind} m/s \nPressure: {pressure} Pa \nHumidity: {humidity}%'
    
#     return text

# def get_info_bot(bot_json):
#     result_up = bot_json['result'][-1]
#     chat_id = result_up['message']['chat']['id']
#     text = result_up['message']['text']
#     message_id = result_up['message']['message_id']
#     return chat_id, text, message_id

# def create_button(chat_id, text):
#     button_tashkent={'text': 'Tashkent'}
#     button_samarkand={'text': 'Samarkand'}
#     button_navoi={'text': 'Navoi'}
#     button_bukhara={'text': 'Bukhara'}
#     keyboard = [
#         [button_tashkent, button_samarkand],
#         [button_navoi, button_bukhara]
#     ]
#     reply_markup = {'keyboard': keyboard, 'resize_keyboard': True}
#     data = {
#         'chat_id': chat_id,
#         'text': text,
#         'reply_markup': reply_markup
#     }
#     return data

# def sendWeather(data):
#     requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', json=data)



# new_id = -1

# while True:
#     getRequestR = get_request(city_name, TOKEN)
#     city_json, bot_json = getRequestR

#     chat_id, text_city_name, message_id = get_info_bot(bot_json)
#     get_all_info = get_request_city(text_city_name)
#     text_weather = get_info_city(get_all_info) #15 gradus
#     data = create_button(chat_id, text_weather)

#     if new_id != message_id:
#         sendWeather(data)
#         new_id = message_id




















import re
import requests
TOKEN = '5603688976:AAEKZQ1m7SyzJMouAMVYfrmYB3LSrvnIPK4'

def get_request(TOKEN):
    r = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    if r.status_code == 200:
        bot_json = r.json()
        return bot_json
    else:
        return 'Enter the correct city name' 

def get_request_city(city_name):
    city_json = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=ba5f0db5da7eed99dc585cd6a768b237').json()
    return city_json 

def get_info_city(city_json):
    city_name = city_json['name']
    today = city_json['weather'][0]['main']
    description = city_json['weather'][0]['description']
    wind = city_json['wind']['speed']
    city_temp = round((city_json['main']['temp'] - 273.15), 2)
    pressure = city_json['main']['pressure']
    humidity = city_json['main']['humidity']
    
    if today == 'Clouds':
        text = f'City: {city_name} \nToday: {today} ☁️\nTemperatura: {city_temp}°C \nDescription: {description} \nWind: {wind} m/s \nPressure: {pressure} Pa \nHumidity: {humidity}%'
    elif today == 'Rain':
        text = f'City: {city_name} \nToday: {today} 🌧\nTemperatura: {city_temp}°C \nDescription: {description} \nWind: {wind} m/s \nPressure: {pressure} Pa \nHumidity: {humidity}%'
    else:
        text = f'City: {city_name} \nToday: {today} \nTemperatura: {city_temp}°C \nDescription: {description} \nWind: {wind} m/s \nPressure: {pressure} Pa \nHumidity: {humidity}%'
    return text

def get_info_bot(bot_json):
    result_up = bot_json['result'][-1]
    chat_id = result_up['message']['chat']['id']
    text = result_up['message']['text']
    message_id = result_up['message']['message_id']
    return chat_id, text, message_id

def create_button(chat_id, text):
    button_tashkent={'text': 'Tashkent'}
    button_samarkand={'text': 'Samarkand'}
    button_navoi={'text': 'Navoi'}
    button_bukhara={'text': 'Bukhara'}
    keyboard = [
        [button_tashkent, button_samarkand],
        [button_navoi, button_bukhara]
    ]
    reply_markup = {'keyboard': keyboard, 'resize_keyboard': True}
    data = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': reply_markup
    }
    return data

def sendWeather(data):
    requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage', json=data)



new_id = -1

while True:
    getRequestR = get_request(TOKEN)
    bot_json = getRequestR

    chat_id, text_city_name, message_id = get_info_bot(bot_json)
    get_all_info = get_request_city(text_city_name)
    text_weather = get_info_city(get_all_info)
    data = create_button(chat_id, text_weather)

    if new_id != message_id:
        sendWeather(data)
        new_id = message_id