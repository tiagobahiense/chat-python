import requests
import json
import threading
import time
server_url = "XXXXX"
def post_message(sender: str, text: str) -> int:
    url = f"{server_url}/message"
    data = {
        'sender': sender,
        'text': text
    }
    response = requests.post(url, data=data)
    if response.status_code != 201:
        print('Failed to send message')
    print(response.json())
class receiver(threading.Thread):
    def set_sender(self, sender: str):
        self.sender = sender
    def get_messages(self):
        url = f"{server_url}/message/{self.last}"
        response = requests.get(url)
        if response.status_code != 200:
            print('Failed to get messages')
            print(response.json())
        else:
            messages = response.json()['messages']
            for message in messages:
                if id >= self.last:
                    print(f">> [{message['when']}] {message['sender']}: {message['text']}")
                    self.last = int(message['id'])
        def run(self, *args, **kwargs):
            self.last = 0
        #Loop para receber mensagens
        while True:
            self.get_messages()
            time.sleep(5)
sender = input('>> Digite seu nome: ')
rcv = receiver()
rcv.set_sender(sender)
rcv.start()
time.sleep(1)
#Loop para envio de mensagens
while True:
    text = input
    ('$> ')
    post_message(sender, text)
    rcv.get_messages()