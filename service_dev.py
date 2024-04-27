# O código começa importando as bibliotecas necessárias - Flask, jsonify e request do módulo flask, e o módulo json
from flask import Flask, jsonify, request
import json  # Biblioteca para utilizar json no código

# Cria uma instância do aplicativo Flask Refere-se à inicialização do aplicativo Flask. * app = Flask(__name__) é a
# linha de código que cria uma nova instância do aplicativo Flask. Aqui, Flask é a classe do aplicativo Flask e
# __name__ é um argumento especial que é necessário. * __name__ é uma variável embutida em Python, que é avaliada
# como o nome do módulo atual. No caso de um script sendo executado diretamente, __name__ é definido como '__main__'.
# * Ao usar __name__ como argumento na classe Flask, você está essencialmente dizendo ao aplicativo Flask para
# configurar algumas coisas por trás das cenas para que ele possa encontrar outros arquivos e diretórios no seu
# aplicativo.
# * A instância do aplicativo Flask, que é um objeto da classe Flask, tem métodos e atributos que são
# usados para gerenciar o aplicativo, como iniciar o servidor de desenvolvimento, definir rotas, gerenciar
# solicitações e respostas, etc.
app = Flask(__name__)

# Lista de dicionários onde cada dicionário representa um desenvolvedor
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


# Devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
# Esta rota lida com as operações GET, PUT e DELETE para um desenvolvedor específico identificado pelo id
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    # Retorna os detalhes do desenvolvedor com o id especificado. Se o id não existir, retorna uma mensagem de erro
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
    # Atualiza os detalhes do desenvolvedor com o id especificado com os novos dados recebidos no corpo da solicitação
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        developers[id] = dados
    elif request.method == 'DELETE':  # Remove o desenvolvedor com o id especificado da lista de desenvolvedores
        developers.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})


# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/',
           methods=['POST', 'GET'])  # Esta rota lida com as operações POST e GET para a lista de desenvolvedores
def developer_list():
    # Adiciona um novo desenvolvedor à lista. O id do novo desenvolvedor é a posição atual na lista
    if request.method == 'POST':
        dados = json.loads(request.data)
        position = len(developers)
        dados['id'] = position
        developers.append(dados)
        return jsonify(developers[position])
    elif request.method == 'GET':  # Retorna a lista completa de desenvolvedores
        return jsonify(developers)


# * if __name__ == '__main__': é uma construção comum em scripts Python. Quando o interpretador Python lê um arquivo
#  de origem, ele executa t0do o código que encontra no arquivo. Antes de executar o código, ele define algumas
#  variáveis especiais. Por exemplo, se o interpretador Python está executando esse módulo (o arquivo de origem) como
#  o programa principal, ele define a variável especial __name__ para ter um valor "__main__". Se este arquivo está
#  sendo importado de outro módulo, __name__ será definido para o nome do arquivo do módulo.
#  * app.run(debug=True) é
#  usado para iniciar o servidor de desenvolvimento local do Flask. O argumento debug=True é usado para iniciar o
#  aplicativo em modo de depuração. Quando o modo de depuração está ativado, o servidor será reiniciado para cada
#  alteração de código e fornecerá informações úteis de depuração caso ocorra um erro. Portanto, a linha if __name__
#  == '__main__': app.run(debug=True) significa que se este script for executado no terminal (ou seja, não importado
#  como um módulo em outro script), então o servidor de desenvolvimento Flask será iniciado no modo de depuração.
#  Isso é útil para desenvolvimento, mas não é recomendado para produção. Para produção, você deve usar um servidor
#  WSGI adequado.

# Inicia o servidor de desenvolvimento do Flask se o script for executado diretamente (não importado como um módulo)
if __name__ == '__main__':
    app.run(debug=True)
