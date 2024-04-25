from flask import Flask, jsonify, request
import json

app = Flask(__name__)

'''Serviço usando parâmetro na URI'''
@app.route('/<int:id>')
def pessoa(id):
    soma = 1 + id
    return jsonify({'id':id, 'nome':'João', 'profissão':'Desenvolvedor'})

# @app.route('/soma/<int:valor1>/<int:valor2>/')
# def soma(valor1, valor2):
#     return jsonify({'soma':valor1 + valor2})

'''Método com passagem de parâmetros no body'''
@app.route('/soma', methods=['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma':total})

if __name__ == '__main__':
    app.run(debug=True)