'''
Criação da API REST, de namespace 'Imoveis', relação de respostas possíveis.
'''

from flask import request, jsonify
from flask_restplus import Resource, fields
from sistemavendaimoveis import db, api
from sistemavendaimoveis.models import Imovel

imovel_namespace = api.namespace('Imoveis',
                                       description='API para listagem, atualização, inserção e '
                                                   'exclusão de imóveis.')

model_imovel = api.model('Modelo Imóvel', {
    'data_posse': fields.DateTime(required = True,
                          description = 'Data da Posse do Imóvel',
                          help='Data da Posse não pode ser branco',
                          dt_format='rfc822'),
    'matricula': fields.String(required = True,
                          description = 'Matrícula do Imóvel',
                          help='Matrícula não pode ser branco'),
    'categoria_id': fields.Integer(required = True,
                          description = 'ID da Categoria do Imóvel',
                          help='ID da Categoria não pode ser branco'),
    'proprietario_id': fields.Integer(required = True,
                          description = 'ID do Proprietário do Imóvel',
                          help='ID do Estado Civil não pode ser branco')
})

model_imovel_patch = api.model('Modelo Imóvel', {
    'data_posse': fields.DateTime(required = False,
                          description = 'Data da Posse do Imóvel',
                          help='Data da Posse não pode ser branco',
                          dt_format='rfc822'),
    'matricula': fields.String(required = False,
                          description = 'Matrícula do Imóvel',
                          help='Matrícula não pode ser branco'),
    'categoria_id': fields.Integer(required = False,
                          description = 'ID da Categoria do Imóvel',
                          help='ID da Categoria não pode ser branco'),
    'proprietario_id': fields.Integer(required = False,
                          description = 'ID do Proprietário do Imóvel',
                          help='ID do Estado Civil não pode ser branco')
})


@imovel_namespace.route('/')
class ImovelList(Resource):

    @api.doc(description= 'Busca todos os imóveis')
    def get(self):
        imoveis = Imovel.query.all()
        output = []
        for imovel in imoveis:
            currImovel = {}
            currImovel['id'] = imovel.id
            currImovel['data_posse'] = imovel.data_posse
            currImovel['matricula'] = imovel.matricula
            currImovel['categoria'] = imovel.categoria.nome
            currImovel['proprietario'] = imovel.proprietario.nome
            output.append(currImovel)
        return jsonify(output)

    @api.expect(model_imovel_patch)
    @api.doc(description='Cadastra novo imóvel')
    def post(self):
        try:
            dados_imovel = request.get_json()
            imovel = Imovel(data_posse=dados_imovel['data_posse'], matricula=dados_imovel['matricula'],
                            categoria_id=dados_imovel['categoria_id'], proprietario_id=dados_imovel['proprietario_id'])
            db.session.add(imovel)
            db.session.commit()
            return jsonify('Imóvel adicionado com sucesso!')
        except KeyError as e:
            imovel_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            imovel_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


@imovel_namespace.route('/<int:imovel_id>')
class ImovelCRUD(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'imovel_id': 'Especifique o ID associado ao imóvel'},
             description='Atualiza imóvel cadastrado')
    def get(self, imovel_id):
        try:
            imovel = Imovel.query.get_or_404(imovel_id)
            currImovel = {}
            currImovel['id'] = imovel.id
            currImovel['data_posse'] = imovel.data_posse
            currImovel['matricula'] = imovel.matricula
            currImovel['categoria'] = imovel.categoria.nome
            currImovel['proprietario'] = imovel.proprietario.nome
            currImovel['custos'] = []
            if imovel.custos:
                for custo in imovel.custos:
                    dict_custo = {}
                    if custo.luz:
                        dict_custo['luz'] = custo.luz
                    if custo.agua:
                        dict_custo['agua'] = custo.agua
                    if custo.propaganda:
                        dict_custo['propaganda'] = custo.propaganda
                    if custo.condominio:
                        dict_custo['condominio'] = custo.condominio
                    if custo.mes:
                        dict_custo['mes'] = custo.mes
                    currImovel['custos'].append(dict_custo)
            return jsonify(currImovel)
        except KeyError as e:
            imovel_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            imovel_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'imovel_id': 'Especifique o ID associado ao imóvel'},
             description='Atualiza imóvel cadastrado',
             body=model_imovel_patch)
    def patch(self, imovel_id):
        try:
            dados_imovel = request.get_json()
            imovel = Imovel.query.get_or_404(imovel_id)
            imovel.data_posse = dados_imovel.get('data_posse', imovel.data_posse)
            imovel.matricula = dados_imovel.get('matricula', imovel.matricula)
            imovel.categoria_id = dados_imovel.get('categoria_id', imovel.categoria_id)
            imovel.proprietario_id = dados_imovel.get('proprietario_id', imovel.proprietario_id)
            db.session.commit()
            return jsonify('Imóvel atualizado com sucesso!')
        except KeyError as e:
            imovel_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            imovel_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'imovel_id': 'Especifique o ID associado ao imóvel'},
             description='Exclui imóvel cadastrado')
    def delete(self, imovel_id):
        try:
            imovel = Imovel.query.get_or_404(imovel_id)
            matricula_imovel = imovel.matricula
            db.session.delete(imovel)
            db.session.commit()
            return jsonify(f'Imóvel de matrícula "{matricula_imovel}" foi excluído!')
        except KeyError as e:
            imovel_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            imovel_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
