'''
Criação da API REST, de namespace 'Transacoes', relação de respostas possíveis.
'''
from flask import request, jsonify
from flask_restplus import Resource, fields
from sistemavendaimoveis import db, api
from sistemavendaimoveis.models import Transacao

transacao_namespace = api.namespace('Transacoes',
                                       description='API para listagem, atualização, inserção e '
                                                   'exclusão de transações.')

model_transacao = api.model('Modelo Transação', {
    'valor': fields.Float(required = True,
                          description = 'Valor da Transação',
                          help='Valor da Transação não pode ser branco'),
    'data_transacao': fields.DateTime(required = True,
                          description = 'Data da Transacao',
                          help='Data da Transacao não pode ser branco',
                          dt_format='rfc822'),
    'financiamento': fields.Boolean(required = True,
                          description = 'Financiamento do Imóvel',
                          help='Financiamento do Imóvel não pode ser branco. Valor "True" para imóvel financiado e '
                               '"False" para pagamento à vista'),
    'cliente_id': fields.Integer(required = True,
                          description = 'ID do Cliente adquirente do Imóvel',
                          help='ID do Cliente não pode ser branco'),
    'proprietario_id': fields.Integer(required = True,
                          description = 'ID do Proprietário do Imóvel',
                          help='ID do Proprietário não pode ser branco'),
    'banco_id': fields.Integer(required = False,
                          description = 'ID do Banco Financiador do Imóvel',
                          help='ID do Banco não pode ser branco'),
    'imovel_id': fields.Integer(required = True,
                          description = 'ID do Imóvel objeto da transação',
                          help='ID do Imóvel não pode ser branco')
})

model_transacao_patch = api.model('Modelo Transação', {
    'valor': fields.Float(required = False,
                          description = 'Valor da Transação',
                          help='Valor da Transação não pode ser branco'),
    'data_transacao': fields.DateTime(required = True,
                              description = 'Data da Transacao',
                              help='Data da Transacao não pode ser branco',
                              dt_format='rfc822'),
    'financiamento': fields.Boolean(required = False,
                          description = 'Financiamento do Imóvel',
                          help='Financiamento do Imóvel não pode ser branco. Valor "True" para imóvel financiado e '
                               '"False" para pagamento à vista'),
    'cliente_id': fields.Integer(required = False,
                          description = 'ID do Cliente adquirente do Imóvel',
                          help='ID do Cliente não pode ser branco'),
    'proprietario_id': fields.Integer(required = False,
                          description = 'ID do Proprietário do Imóvel',
                          help='ID do Proprietário não pode ser branco'),
    'banco_id': fields.Integer(required = False,
                          description = 'ID do Banco Financiador do Imóvel',
                          help='ID do Banco não pode ser branco'),
    'imovel_id': fields.Integer(required = False,
                          description = 'ID do Imóvel objeto da transação',
                          help='ID do Imóvel não pode ser branco')
})


@transacao_namespace.route('/')
class TransacaoList(Resource):

    @api.doc(description= 'Busca todas as transações')
    def get(self):
        transacoes = Transacao.query.all()
        output = []
        for transacao in transacoes:
            currTransacao = {}
            currTransacao['id'] = transacao.id
            currTransacao['valor'] = transacao.valor
            currTransacao['data_transacao'] = transacao.data_transacao
            currTransacao['financiamento'] = transacao.financiamento
            currTransacao['cliente'] = transacao.cliente.nome
            currTransacao['proprietario'] = transacao.proprietario.nome
            currTransacao['banco'] = transacao.banco.nome
            currTransacao['imovel'] = transacao.imovel.matricula
            output.append(currTransacao)
        return jsonify(output)

    @api.expect(model_transacao_patch)
    @api.doc(description='Cadastra nova transação')
    def post(self):
        try:
            dados_transacao = request.get_json()
            transacao = Transacao(valor=dados_transacao['valor'],
                                  data_transacao=dados_transacao['data_transacao'],
                                  financiamento=dados_transacao['financiamento'],
                                  cliente_id=dados_transacao['cliente_id'],
                                  proprietario_id=dados_transacao['proprietario_id'],
                                  banco_id=dados_transacao['id'],
                                  imovel_id=dados_transacao['imovel_id'])
            db.session.add(transacao)
            db.session.commit()
            return jsonify('Transação adicionada com sucesso!')
        except KeyError as e:
            transacao_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            transacao_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


@transacao_namespace.route('/<int:transacao_id>')
class TransacaoCRUD(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'transacao_id': 'Especifique o ID associado à transação'},
             description='Atualiza transação cadastrada')
    def get(self, transacao_id):
        try:
            transacao = Transacao.query.get_or_404(transacao_id)
            currTransacao = {}
            currTransacao['id'] = transacao.id
            currTransacao['valor'] = transacao.valor
            currTransacao['data_transacao'] = transacao.data_transacao
            currTransacao['financiamento'] = transacao.financiamento
            currTransacao['cliente'] = transacao.cliente.nome
            currTransacao['proprietario'] = transacao.proprietario.nome
            currTransacao['banco'] = transacao.banco.nome
            currTransacao['imovel'] = transacao.imovel.matricula
            return jsonify(currTransacao)
        except KeyError as e:
            transacao_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            transacao_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'transacao_id': 'Especifique o ID associado à transação'},
             description='Atualiza transação cadastrada',
             body=model_transacao_patch)
    def patch(self, transacao_id):
        try:
            dados_transacao = request.get_json()
            transacao = Transacao.query.get_or_404(transacao_id)
            transacao.valor = dados_transacao.get('valor', transacao.valor)
            transacao.data_transacao = dados_transacao.get('data_transacao', transacao.data_transacao)
            transacao.financiamento = dados_transacao.get('financiamento', transacao.financiamento)
            transacao.cliente_id = dados_transacao.get('cliente_id', transacao.cliente_id)
            transacao.proprietario_id = dados_transacao.get('proprietario_id', transacao.proprietario_id)
            transacao.banco_id = dados_transacao.get('banco_id', transacao.banco_id)
            transacao.imovel_id = dados_transacao.get('imovel_id', transacao.imovel_id)
            db.session.commit()
            return jsonify('Transação atualizada com sucesso!')
        except KeyError as e:
            transacao_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            transacao_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'transacao_id': 'Especifique o ID associado à transação'},
             description='Exclui transação cadastrada')
    def delete(self, transacao_id):
        try:
            transacao = Transacao.query.get_or_404(transacao_id)
            db.session.delete(transacao)
            db.session.commit()
            return jsonify(f'Transação foi excluída!')
        except KeyError as e:
            transacao_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            transacao_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
