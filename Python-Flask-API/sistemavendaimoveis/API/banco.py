'''
Criação da API REST, de namespace 'Bancos', relação de respostas possíveis.
'''

from flask import request, jsonify
from flask_restplus import Resource, fields
from sistemavendaimoveis import db, api
from sistemavendaimoveis.models import Banco

banco_namespace = api.namespace('Bancos',
                                    description='API para listagem, atualização, inserção e '
                                                'exclusão de bancos.')

model_banco = api.model('Modelo Bancos', {
    'nome': fields.String(required=True,
                          description='Nome do Banco',
                          help='Nome do banco não pode ser branco')
})


@banco_namespace.route('/')
class BancoList(Resource):

    @api.doc(description='Busca todos os bancos cadastrados')
    def get(self):
        bancos = Banco.query.all()
        output = []
        for banco in bancos:
            currBanco = {}
            currBanco['id'] = banco.id
            currBanco['nome'] = banco.nome
            output.append(currBanco)
        return jsonify(output)

    @api.expect(model_banco)
    @api.doc(description='Cadastra novo banco')
    def post(self):
        dados_banco = request.get_json()
        banco = Banco(nome=dados_banco['nome'])
        db.session.add(banco)
        db.session.commit()
        return jsonify('Banco adicionado com sucesso!')


@banco_namespace.route('/<int:banco_id>')
class BancoCRUD(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'banco_id': 'Especifique o ID associado ao banco'},
             description='Atualiza banco cadastrado')
    def get(self, banco_id):
        try:
            banco = Banco.query.get_or_404(banco_id)
            currBanco = {}
            currBanco['id'] = banco.id
            currBanco['nome'] = banco.nome
            return jsonify(currBanco)
        except KeyError as e:
            banco_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            banco_namespace.abort(400, e.__doc__, status="Invalid Argument", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'banco_id': 'Especifique o ID associado ao banco'},
             description='Atualiza banco cadastrado',
             body=model_banco)
    def patch(self, banco_id):
        try:
            dados_banco = request.get_json()
            banco = Banco.query.get_or_404(banco_id)
            banco.nome = dados_banco.get('nome', banco.nome)
            db.session.commit()
            return jsonify('Banco atualizado com sucesso!')
        except KeyError as e:
            banco_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            banco_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'banco_id': 'Especifique o ID associado ao banco'},
             description='Exclui banco cadastrado')
    def delete(self, banco_id):
        try:
            banco = Banco.query.get_or_404(banco_id)
            db.session.delete(banco)
            db.session.commit()
            return jsonify(f'Banco foi excluído!')
        except KeyError as e:
            banco_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            banco_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
