import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld") # enviando requisição get para URL
print(response.json()) # usando json para receber response com algumas informações ao invez de um objeto
