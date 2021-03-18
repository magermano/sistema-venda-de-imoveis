'''
Criação da API REST, de namespace 'Estados-Civis', relação de respostas possíveis.
'''

from flask import request, jsonify
from flask_restplus import Resource, fields
from sistemavendaimoveis import db, api
from sistemavendaimoveis.models import Ecivil


ecivil_namespace = api.namespace('Estados-Civis',
                                       description='API para listagem, atualização, inserção e '
                                                   'exclusão de estados civis.')

model_ecivil = api.model('Modelo Estado Civil', {
    'nome': fields.String(required = True,
                          description = 'Nome do Estado Civil',
                          help='Nome não pode ser branco')
})


@ecivil_namespace.route('/')
class EcivilList(Resource):

    @api.doc(description= 'Busca todos os estados civis')
    def get(self):
        ecivis = Ecivil.query.all()
        output = []
        for ecivil in ecivis:
            currEcivil = {}
            currEcivil['nome'] = ecivil.nome
            currEcivil['id'] = ecivil.id
            output.append(currEcivil)
        return jsonify(output)

    @api.expect(model_ecivil)
    @api.doc(description='Cadastra novo estado civil')
    def post(self):
        dados_ecivil = request.get_json()
        ecivil = Ecivil(nome=dados_ecivil['nome'])
        db.session.add(ecivil)
        db.session.commit()
        return jsonify('Estado Civil adicionado com sucesso!')


@ecivil_namespace.route('/<int:ecivil_id>')
class EcivilCRUD(Resource):


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'ecivil_id': 'Especifique o ID associado ao estado civil'},
             description='Atualiza estado civil cadastrado')
    def get(self, ecivil_id):
        try:
            ecivil = Ecivil.query.get_or_404(ecivil_id)
            currEcivil = {}
            currEcivil['nome'] = ecivil.nome
            currEcivil['id'] = ecivil.id
            return jsonify(currEcivil)
        except KeyError as e:
            ecivil_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            ecivil_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'ecivil_id': 'Especifique o ID associado ao estado civil'},
             description='Atualiza estado civil cadastrado',
             body=model_ecivil)
    def patch(self, ecivil_id):
        try:
            dados_ecivil = request.get_json()
            ecivil = Ecivil.query.get_or_404(ecivil_id)
            ecivil.nome = dados_ecivil.get('nome', ecivil.nome)
            db.session.commit()
            return jsonify('Estado civil atualizado com sucesso!')
        except KeyError as e:
            ecivil_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            ecivil_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'ecivil_id': 'Especifique o ID associado ao estado civil'},
             description='Exclui estado civil cadastrado')
    def delete(self, ecivil_id):
        try:
            ecivil = Ecivil.query.get(ecivil_id)
            db.session.delete(ecivil)
            db.session.commit()
            return jsonify(f'Estado Civil foi excluído!')
        except KeyError as e:
            ecivil_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            ecivil_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
