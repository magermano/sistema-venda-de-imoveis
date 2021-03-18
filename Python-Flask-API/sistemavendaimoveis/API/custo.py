'''
Criação da API REST, de namespace 'Custos-de-Imóvel', relação de respostas possíveis.
'''

from flask import request, jsonify
from flask_restplus import Resource, fields
from sistemavendaimoveis import db, api
from sistemavendaimoveis.models import Custo

custo_namespace = api.namespace('Custos-de-Imóvel',
                                  description='API para listagem, atualização, inserção e '
                                              'exclusão de custos de imóvel.')


model_custo = api.model('Modelo Custos de Imóvel', {
    'luz': fields.Float(required = False,
                          description = 'Valor gasto com energia',
                          help='Valor padrão é 0',
                          default=0),
    'agua': fields.Float(required = False,
                          description = 'Valor gasto com agua',
                          help='Valor padrão é 0',
                          default=0),
    'condominio': fields.Float(required = False,
                          description = 'Valor gasto com condomínio',
                          help='Valor padrão é 0',
                          default=0),
    'propaganda': fields.Float(required = False,
                          description = 'Valor gasto com propaganda',
                          help='Valor padrão é 0',
                          default=0),
    'mes': fields.DateTime(required = True,
                          description = 'Data em que os gastos foram realizados',
                          help='O campo não pode ser branco',
                          dt_format='rfc822'),
    'imovel_id': fields.Integer(required = True,
                          description = 'ID do Imóvel referente aos gastos',
                          help='ID do Imóvel não pode ser branco')
})

model_custo_patch = api.model('Modelo Custos de Imóvel', {
    'luz': fields.Float(required = False,
                          description = 'Valor gasto com energia',
                          help='Valor padrão é 0',
                          default=0),
    'agua': fields.Float(required = False,
                          description = 'Valor gasto com agua',
                          help='Valor padrão é 0',
                          default=0),
    'condominio': fields.Float(required = False,
                          description = 'Valor gasto com condomínio',
                          help='Valor padrão é 0',
                          default=0),
    'propaganda': fields.Float(required = False,
                          description = 'Valor gasto com propaganda',
                          help='Valor padrão é 0',
                          default=0),
    'mes': fields.DateTime(required = False,
                          description = 'Data em que os gastos foram realizados',
                          help='O campo não pode ser branco',
                          dt_format='rfc822'),
    'imovel_id': fields.Integer(required = False,
                          description = 'ID do Imóvel referente aos gastos',
                          help='ID do Imóvel não pode ser branco')
})

@custo_namespace.route('/')
class CustoList(Resource):

    @api.doc(description= 'Busca todos os custos')
    def get(self):
        custos = Custo.query.all()
        output = []
        for custo in custos:
            currCusto = {}
            currCusto['luz'] = custo.luz
            currCusto['agua'] = custo.agua
            currCusto['condominio'] = custo.condominio
            currCusto['propaganda'] = custo.propaganda
            currCusto['mes'] = custo.mes
            currCusto['imovel'] = custo.imovel.matricula
            output.append(currCusto)
        return jsonify(output)

    @api.expect(model_custo)
    @api.doc(description='Cadastra novo custo')
    def post(self):
        dados_custo = request.get_json()
        custo = Custo(luz=dados_custo['luz'],
                      agua=dados_custo['agua'],
                      condominio=dados_custo['condominio'],
                      propaganda=dados_custo['propaganda'],
                      mes=dados_custo['mes'],
                      imovel_id=dados_custo['imovel_id'])
        db.session.add(custo)
        db.session.commit()
        return jsonify('Custo adicionado com sucesso!')


@custo_namespace.route('/<int:custo_id>')
class CustoCRUD(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'custo_id': 'Especifique o ID associado ao custo'},
             description='Atualiza custo cadastrado')
    def get(self, custo_id):
        try:
            custo = Custo.query.get_or_404(custo_id)
            currCusto = {}
            currCusto['luz'] = custo.luz
            currCusto['agua'] = custo.agua
            currCusto['condominio'] = custo.condominio
            currCusto['propaganda'] = custo.propaganda
            currCusto['mes'] = custo.mes
            currCusto['imovel'] = custo.imovel.matricula
            return jsonify(currCusto)
        except KeyError as e:
            custo_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            custo_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.expect(model_custo_patch)
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'custo_id': 'Especifique o ID associado ao custo'},
             description='Atualiza custo cadastrado. Permite atualizar um ou mais campos',
             body=model_custo_patch)
    def patch(self, custo_id):
        try:
            dados_custo = request.get_json()
            print(type(dados_custo))
            custo = Custo.query.get_or_404(custo_id)
            custo.luz = dados_custo.get('luz', custo.luz)
            custo.agua = dados_custo.get('agua', custo.agua)
            custo.condominio = dados_custo.get('condominio', custo.condominio)
            custo.propaganda = dados_custo.get('propaganda', custo.propaganda)
            custo.mes = dados_custo.get('mes', custo.mes)
            custo.imovel_id = dados_custo.get('imovel_id', custo.imovel_id)
            db.session.commit()
            return jsonify('Custo atualizado com sucesso!')
        except KeyError as e:
            custo_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            custo_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'custo_id': 'Especifique o ID associado ao custo'},
             description='Exclui custo cadastrado')
    def delete(self, custo_id):
        try:
            custo = Custo.query.get_or_404(custo_id)
            db.session.delete(custo)
            db.session.commit()
            return jsonify(f'Custo foi excluído(a)!')
        except KeyError as e:
            custo_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            custo_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
