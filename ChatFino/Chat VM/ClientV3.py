import requests
import json
import threading
import time

# URL da API de criação de usuário
server_url = 'XXXXXXXXX'

# Dados para criar o usuário
user_data = {
    "name": "user1",
    "password": "123456"
}

# Função para criar o usuário
def criar_usuario():
    url = f"{server_url}/user/"
    data = {
        'name': "tiago",
        'password': "40294029"
    }

    response = requests.post(url, json=data)
    
    if response.status_code == 201:
        print("Usuário criado com sucesso!")
        return response.json()  # O ID do usuário será retornado
    else:
        print(f"Erro ao criar usuário: {response.status_code}")
        print(response.text)

# Criar o usuário e capturar o ID
usuario = criar_usuario()
print(f"ID do usuário: {usuario['id']}")

# Função para autenticar e obter o token
def autenticar_usuario():
    # URL da API de autenticação
    url_auth = f'{server_url}/auth/'
    # Dados de autenticação (use o mesmo nome e senha que usou na criação do usuário)
    auth_data = {
    "password": "40294029"
    }
    response = requests.post(url_auth, json=auth_data)
    
    if response.status_code == 200:
        print("Autenticado com sucesso!")
        return response.json()  # Retorna o token
    else:
        print(f"Erro ao autenticar: {response.status_code}")
        print(response.text)

# Autenticar o usuário e capturar o token
token = autenticar_usuario()['token']
print(f"Token de autenticação: {token}")

# Função para enviar uma mensagem
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

# Classe para receber mensagens
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
        # Loop para receber mensagens
        while True:
            self.get_messages()
            time.sleep(5)

# Função para deslogar o usuário
def deslogar_usuario(token):
    url_logout = f"{server_url}/auth/1"  # Certifique-se de passar o ID correto do usuário
    headers = {
        'Authorization': token
    }
    response = requests.delete(url_logout, headers=headers)
    
    if response.status_code == 200:
        print("Deslogado com sucesso!")
    else:
        print(f"Erro ao deslogar: {response.status_code}")
        print(response.text)

# Autenticação do usuário e obtenção do token
token = autenticar_usuario()

# Garantir que o token foi obtido com sucesso
if token:
    # Nome do remetente
    sender = input('>> Digite seu nome: ')

    # Inicializa o receptor de mensagens
    rcv = receiver()
    rcv.set_sender(sender, token)
    rcv.start()

    time.sleep(1)

    # Loop para envio de mensagens
    while True:
        text = input('$> ')
        if text.lower() == 'logout':
            deslogar_usuario(token)
            break
        else:
            post_message(sender, text, token)
            rcv.get_messages()
