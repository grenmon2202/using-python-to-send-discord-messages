import requests
import json

def send_message():
    try:
        with open('token', 'r') as f:
            token = f.read()
    except:
        print('Please set your token first')
        return
    channel = input('Enter channel to send message to: ')
    message = input('Enter message to send: ')
    url = f'https://discord.com/api/v9/channels/{channel}/messages'

    headers = {
        'authorization': token,
        'content-type': 'application/json'
    }
    payload = {
        'content': message
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

def set_token():
    token = input('Enter your authentication token: ')
    with open('token', 'w') as f:
        f.write(token)

ch = int(input('1- Send a message, 2- Update token: '))

if ch == 1:
    send_message()
elif ch == 2:
    set_token()