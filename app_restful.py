from flask import Flask, request
from flask_restful import Resource, Api
from skills import Skills
import json

app = Flask(__name__)
api = Api(app)

developers = [
    {
        'id':'0',
        'nome':'Karl',
        'habilidades':['Python', 'Flask']
    },
    {
        'id':1,
        'nome':'Millany',
        'habilidades':['Python', 'Django']
    }
]


# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            message = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':message}
        except Exception:
            message = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':message}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        developers[id] = dados
        return dados

    def delete(self, id):
        developers.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro excluído'}

# Lista todos os desenvolvedor e permite registrar um novo desenvolvedor
class DevelopersList(Resource):
    def get(self):
        return developers

    def post(self):
        body = json.loads(request.data)
        position = len(developers)
        body['id'] = position
        developers.append(body)
        return developers[position]

api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(DevelopersList, '/dev/')
api.add_resource(Skills, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)