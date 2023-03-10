import json

import requests
import socketio


TOKEN = "XXXXXXXXXX"  # XXXXXXXXXX = Donationalerts token
NIGHTBOT = 'XXXXXXXXXX'  # XXXXXXXXXX = Nightbot auth token

sio = socketio.Client()


@sio.on('connect')
def on_connect():
    sio.emit('add-user', {"token": TOKEN, "type": "alert_widget"})


@sio.on('donation')
def on_message(data):
    y = json.loads(data)
    if y['alert_type'] == '19':
        pass
    else:
        with open('donate.json', 'w', encoding='utf8') as outfile:
            json.dump(y, outfile)
        # Nightbot
        requests.post('https://api.nightbot.tv/1/channel/send',
                      headers={'Authorization': 'Bearer ' + NIGHTBOT},
                      data=dict(
                          message=f"/announceorange 💳 New donate from {y['username']} , "
                                  f"{y['amount_formatted']} {y['currency']} ,"
                                  f" message: {y['message']}"))


sio.connect('wss://socket.donationalerts.ru:443', transports='websocket')
