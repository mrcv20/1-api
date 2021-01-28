import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"likes": 10}) # enviando requisição get para endpoint
print(response.json()) # usando json para receber response com algumas informações ao i nvez de um objeto
