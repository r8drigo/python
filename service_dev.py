from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {
        'id': '0',
        'nome': 'Pedro',
        'habilidades': ['Python', 'Flask']
    },

    {
        'id': 1,
        'nome': 'Mateus',
        'habilidades': ['Java', 'Spring']
    }
]


# Desvolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            message = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': message}
        except Exception:
            message = 'Erro desconhecido.'
            response = {'status': 'erro', 'mensagem': message}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        developers[id] = dados
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})


# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def developer_list():
    if request.method == 'POST':
        dados = json.loads(request.data)
        position = len(developers)
        dados['id'] = position
        developers.append(dados)
        return jsonify(developers[position])
    elif request.method == 'GET':
        return jsonify(developers)


if __name__ == '__main__':
    app.run(debug=True)
