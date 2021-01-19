#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import datetime

x = datetime.datetime.now()
datatime = x.strftime('%d/%m/%Y-%H:%M:%S')
print(datatime)

headers = {
    'Authorization': 'Bearer eyJrIjoiMDE0Vms3SUF5UjAzMkIzdzRVU3lFQm9XYzl1M3dBQU4iLCJuIjoiQXBpVGVsZWdyYW0iLCJpZCI6MX0=',
}

params = (
    ('orgId', '1'),
    ('refresh', '1m'),
    ('fullscreen', ''),
    ('width', '1920'),
    ('height', '1700'),
    ('kiosk', 'tv'),
    ('from', 'now-1h'),
    ('to', 'now'),
    ('var-machine', ''),
    ('var-ideal', '12'),
)

response = requests.get('http://192.168.0.249:3000/render/d/000000005/zbx-dashboard-abdi', headers=headers, params=params)

with open("/tmp/response.png", "wb") as f:
    f.write(response.content)
print(response.url)

###ENVIANDO A IMAGEM .PNP PARA GRUPO LINUX TELEGRAM
import json

bot_token = '1459207785:AAEGNH4SiP3Xy9IocrZ1LOo3w5IZ48FlGGM'
chat_id = "-227617514"
file = r"/tmp/response.png"

files = {
    'photo': open(file, 'rb')
}

msg = "✅ ➤ DASHBOARD ABDI"

messagem = ('https://api.telegram.org/bot'+ bot_token + '/sendMessage?chat_id='
           + chat_id + '&text=' + msg + " " + datatime) 

fotoPNG = ('https://api.telegram.org/bot'+ bot_token + '/sendPhoto?chat_id=' 
           + chat_id)
send2 = requests.post(messagem)
send = requests.post(fotoPNG, files = files)



