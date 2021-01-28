from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__) # instancia da class Flask "app"

api = Api(app) # instância da class Api "api"

class HelloWorld(Resource): # herdando de Resource para a criação de funções que serão mapeadas em metodos HTTP
    def get(self): 
        return {"data":"Hello World"}

api.add_resource(HelloWorld, "/helloworld") # registrando a class HelloWorld como Resource, definindo sua endpoint "helloworld"



if __name__ == '__main__':
    app.run(debug=True)