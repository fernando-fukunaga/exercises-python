'''
Desafio:
Crie um programa em Python que consuma a API pública do OpenWeatherMap (https://openweathermap.org/api) 
para obter informações sobre o clima em uma cidade específica e exibir algumas informações em sua tela. 
O programa deve pedir que o usuário informe o nome de uma cidade e, em seguida, deve exibir as seguintes informações:
-Nome da cidade
-Temperatura atual em graus Celsius
-Descrição atual do clima
-Velocidade do vento
-Umidade atual
-Pressão atmosférica

Dicas:
-Você precisará criar uma conta no OpenWeatherMap para obter uma chave de API.
-Utilize a biblioteca requests para realizar as requisições HTTP.
-A API do OpenWeatherMap retorna dados em formato JSON, portanto, utilize a biblioteca json para converter as respostas em objetos Python.
-Consulte a documentação da API do OpenWeatherMap para obter mais informações sobre as rotas disponíveis e como utilizá-las.
'''

import requests
import json

class ConsumindoApiWeather:
    def __init__(self, key, city):
        self.key = key
        self.city = city

    def get_lat_e_lon(self):
        response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={self.city}&limit=5&appid={self.key}')