import requests
import json

bot_token = '1459207785:AAEGNH4SiP3Xy9IocrZ1LOo3w5IZ48FlGGM'
chat_id = "-227617514"
file = r"/home/danilo/teste.png"

files = {
    'photo': open(file, 'rb')
}

msg = "DASHBOARD ABDI"

messagem = ('https://api.telegram.org/bot'+ bot_token + '/sendMessage?chat_id='
           + chat_id + '&text=' + msg) 

fotoPNG = ('https://api.telegram.org/bot'+ bot_token + '/sendPhoto?chat_id=' 
           + chat_id)
send2 = requests.post(messagem)
send = requests.post(fotoPNG, files = files)

