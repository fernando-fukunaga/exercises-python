'''
Desafio:
Crie um programa em Python que consuma a API pública do Github (https://api.github.com) 
para obter informações sobre um usuário específico e exibir algumas informações em sua tela. 
O programa deve pedir que o usuário informe o nome de um usuário do Github e, em seguida, deve exibir as seguintes informações:
-Nome do usuário
-Número de repositórios públicos
-Número de seguidores
-Lista com o nome dos repositórios públicos (até 5)
-Data de criação da conta no Github

Dicas:
-Utilize a biblioteca requests para realizar as requisições HTTP.
-A API do Github utiliza o formato JSON para retornar dados, portanto, utilize a biblioteca json para converter as respostas em objetos Python.
-Consulte a documentação da API do Github para obter mais informações sobre as rotas disponíveis e como utilizá-las.
'''

import requests
import json

class ConsumindoApiGithub:
    def __init__(self, usuario):
        self.usuario = usuario

    def _chama_user(self):
        response = requests.get(f'https://api.github.com/users/{self.usuario}')
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def _chama_repos(self):
        response = requests.get(f'https://api.github.com/users/{self.usuario}/repos')
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def _list_repo_names(self):
        repos = self._chama_repos()
        list = []
        for i in range(0,5):
            list.append(repos[i]['name'])
        return list
        
    def imprime_info(self):
        response = self._chama_user()
        username = response['login']
        repos = response['public_repos']
        followers = response['followers']
        repo_names = self._list_repo_names()
        creation_date = response['created_at']
        print(f'Nome do usuário: {username}\nNúmero de repositórios públicos: {repos}\nNúmero de seguidores: {followers}\nLista com o nome dos repositórios públicos (até 5): {repo_names}\nData de criação da conta no Github: {creation_date}')
        
username = input("Digite o nome de usuário desejado: ")

user = ConsumindoApiGithub(username)

user.imprime_info()