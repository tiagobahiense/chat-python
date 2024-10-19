import requests
import json
import threading
import time

server_url = 'XXXXXXXXX'

user_data = {
    "name": "user1",
    "password": "123456"
}

def criar_usuario():
    url = f"{server_url}/user/"
    data = {
        'name': "tiago",
        'password': "XXXXXXX"
    }

    response = requests.post(url, json=data)
    
    if response.status_code == 201:
        print("Usuário criado com sucesso!")
        return response.json()
    else:
        print(f"Erro ao criar usuário: {response.status_code}")
        print(response.text)


usuario = criar_usuario()
print(f"ID do usuário: {usuario['id']}")


def autenticar_usuario():
    
    url_auth = f'{server_url}/auth/'
    
    auth_data = {
    "password": "40294029"
    }
    response = requests.post(url_auth, json=auth_data)
    
    if response.status_code == 200:
        print("Autenticado com sucesso!")
        return response.json() 
    else:
        print(f"Erro ao autenticar: {response.status_code}")
        print(response.text)


token = autenticar_usuario()['token']
print(f"Token de autenticação: {token}")


def post_message(sender: str, text: str, token: str) -> int:
    url = f"{server_url}/message"
    data = {
        'sender': sender,
        'text': text
    }
    headers = {
        'Authorization': token
    }
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code != 200:
        print('Falha ao enviar a mensagem')
        print(response.json())
    else:
        print('Mensagem enviada com sucesso!')


class receiver(threading.Thread):
    def set_sender(self, sender: str, token: str):
        self.sender = sender
        self.token = token

    def get_messages(self):
        url = f"{server_url}/message/{self.last}"
        headers = {
            'Authorization': self.token
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print('Falha ao receber mensagens')
            print(response.json())
        else:
            messages = response.json()['messages']
            for message in messages:
                id = int(message['id'])
                if id >= self.last:
                    print(f">> [{message['when']}] {message['sender']}: {message['text']}")
                    self.last = int(message['id'])

    def run(self, *args, **kwargs):
        self.last = 0
 
        while True:
            self.get_messages()
            time.sleep(5)


def deslogar_usuario(token):
    url_logout = f"{server_url}/auth/1" 
    headers = {
        'Authorization': token
    }
    response = requests.delete(url_logout, headers=headers)
    
    if response.status_code == 200:
        print("Deslogado com sucesso!")
    else:
        print(f"Erro ao deslogar: {response.status_code}")
        print(response.text)

token = autenticar_usuario()


if token:
    
    sender = input('>> Digite seu nome: ')

    
    rcv = receiver()
    rcv.set_sender(sender, token)
    rcv.start()

    time.sleep(1)

   
    while True:
        text = input('$> ')
        if text.lower() == 'logout':
            deslogar_usuario(token)
            break
        else:
            post_message(sender, text, token)
            rcv.get_messages()
