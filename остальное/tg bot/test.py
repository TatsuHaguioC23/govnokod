import requests
import json
import transliterate
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

print(transliterate.translit('Мари Эл', reversed=True))
token_smm = "7645ffc61ffd132b3b9131458176980d"
token_smm2 = "ccb29adb571e0bd57c21b42ab2652de0"
openweather_token = "http://api.openweathermap.org/data/2.5/weather?appid=1840343a10e12bec9837aca471c28ced&q="
token_1smm = "fb73667149d45a72be0a8b747b2bddb8"
nasa_token = "ubQkGCgxtk50MclgCqfWbamZFmcC2MmahJsui5iX"
token = ""
token = ""


city = (transliterate.translit("Энгельс", reversed=True))
print(city)
param={"api_token": token_smm, "action": "balance"}
#print(requests.post("https://smmpanelus.com/api/v2", json=param).json())
param={"api_token": token_smm2, "action": "services"}
#print(requests.post("https://smmpanelus.com/api/v2", json=param).json())
param={"id": "104", "quantity": "200", "link": "https://vk.com/jiulloiveeusigtuna", "token": token_1smm}
#print(requests.post("https://1-smm.com/api/", json=param))
param={"id": "104", "quantity": "200", "link": "https://vk.com/jiulloiveeusigtuna", "token": token_1smm}
#print(requests.get("https://1-smm.com/api/", json=param))
param=(requests.get(openweather_token+city+"&units=metric").json())
print(param)
print(param["main"]["temp"])

param={''}

message = 'Погода'

if message == "Погода":
    answer1="Энгельс"
    city = transliterate.translit(answer1, reversed=True)
    param=(requests.get(openweather_token+city+"&units=metric").json())
    if param['cod'] == '404':
        print('Не удалось найти такой город ＞﹏＜')
    else:
        temp = round(param["main"]["temp"])
        temp_f = round(param["main"]["feels_like"])
        cit = transliterate.translit(param["name"],'ru', reversed=True)
        vivod= (f"На данный момент в городе {answer1}:\n"
            f"Температура: {temp}, ощущается как {temp_f}")
        print(vivod)
else:
    print('sesf')



















url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/one_attachment/id/%7Bmail_id%7D/%7BatId%7D/"

headers = {
    'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com",
    'x-rapidapi-key': "998313450emshc84d468c33444fdp1c923ejsn2538a6975bd3"
    }

response = requests.request("GET", url, headers=headers)

#print(response.text)

import requests

url = "https://google-authenticator.p.rapidapi.com/new_v2/"

headers = {
    'x-rapidapi-host': "google-authenticator.p.rapidapi.com",
    'x-rapidapi-key': "998313450emshc84d468c33444fdp1c923ejsn2538a6975bd3"
    }

response = requests.request("GET", url, headers=headers)

#print(response.text)


def hello_to_you(first_name,last_name):
    print(f"Hello, {first_name} {last_name}")
    
#hello_to_you("хз", "хй")