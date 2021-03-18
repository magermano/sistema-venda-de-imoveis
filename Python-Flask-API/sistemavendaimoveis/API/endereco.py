'''
Criação da API REST, de namespace 'Enderecos', relação de respostas possíveis.
'''

from flask import request, jsonify
from flask_restplus import Resource, fields
from sistemavendaimoveis import db, api
from sistemavendaimoveis.models import Endereco

endereco_namespace = api.namespace('Enderecos',
                                       description='API para listagem, atualização, inserção e '
                                                   'exclusão de endereços.')

model_endereco = api.model('Modelo Endereço', {
    'rua': fields.String(required = True,
                          description = 'Rua do Endereço',
                          help='Rua do Endereço não pode ser branco'),
    'numero': fields.String(required = True,
                          description = 'Número do Endereço',
                          help='Número do Endereço não pode ser branco'),
    'andar': fields.Integer(required = True,
                          description = 'Andar do Endereço',
                          help='Andar do Endereço não pode ser branco'),
    'bloco': fields.Integer(required = True,
                          description = 'Bloco do Endereço',
                          help='Bloco do Endereço não pode ser branco'),
    'bairro': fields.String(required = True,
                          description = 'Bairro do Endereço',
                          help='Bairro do Endereço não pode ser branco'),
    'cep': fields.String(required = True,
                          description = 'CEP do Endereço',
                          help='CEP do Endereço não pode ser branco'),
    'cidade': fields.String(required = True,
                          description = 'Cidade do Endereço',
                          help='Cidade do Endereço não pode ser branco'),
    'estado': fields.String(required = True,
                          description = 'Estado do Endereço',
                          help='Estado do Endereço não pode ser branco'),
    'cliente_id': fields.Integer(required = False,
                          description = 'ID do Cliente adquirente do Imóvel',
                          help='ID do Cliente não pode ser branco'),
    'proprietario_id': fields.Integer(required = False,
                          description = 'ID do Proprietário do Imóvel',
                          help='ID do Proprietário não pode ser branco'),
    'imovel_id': fields.Integer(required = False,
                          description = 'ID do Imóvel objeto da transação',
                          help='ID do Imóvel não pode ser branco')
})

model_endereco_patch = api.model('Modelo Endereço', {
    'rua': fields.String(required = False,
                          description = 'Rua do Endereço',
                          help='Rua do Endereço não pode ser branco'),
    'numero': fields.String(required = False,
                          description = 'Número do Endereço',
                          help='Número do Endereço não pode ser branco'),
    'andar': fields.Integer(required = False,
                          description = 'Andar do Endereço',
                          help='Andar do Endereço não pode ser branco'),
    'bloco': fields.Integer(required = False,
                          description = 'Bloco do Endereço',
                          help='Bloco do Endereço não pode ser branco'),
    'bairro': fields.String(required = False,
                          description = 'Bairro do Endereço',
                          help='Bairro do Endereço não pode ser branco'),
    'cep': fields.String(required = False,
                          description = 'CEP do Endereço',
                          help='CEP do Endereço não pode ser branco'),
    'cidade': fields.String(required = False,
                          description = 'Cidade do Endereço',
                          help='Cidade do Endereço não pode ser branco'),
    'estado': fields.String(required = False,
                          description = 'Estado do Endereço',
                          help='Estado do Endereço não pode ser branco'),
    'cliente_id': fields.Integer(required = False,
                          description = 'ID do Cliente adquirente do Imóvel',
                          help='ID do Cliente não pode ser branco'),
    'proprietario_id': fields.Integer(required = False,
                          description = 'ID do Proprietário do Imóvel',
                          help='ID do Proprietário não pode ser branco'),
    'imovel_id': fields.Integer(required = False,
                          description = 'ID do Imóvel objeto da transação',
                          help='ID do Imóvel não pode ser branco')
})


@endereco_namespace.route('/')
class EnderecoList(Resource):

    @api.doc(description= 'Busca todos os endereços')
    def get(self):
        enderecos = Endereco.query.all()
        output = []
        for endereco in enderecos:
            currEndereco = {}
            currEndereco['id'] = endereco.id
            currEndereco['rua'] = endereco.rua
            currEndereco['numero'] = endereco.numero
            if endereco.andar:
                currEndereco['andar'] = endereco.andar
            if endereco.bloco:
                currEndereco['bloco'] = endereco.bloco
            currEndereco['bairro'] = endereco.bairro
            currEndereco['cep'] = endereco.cep
            currEndereco['cidade'] = endereco.cidade
            currEndereco['estado'] = endereco.estado
            if endereco.cliente:
                currEndereco['cliente'] = endereco.cliente.nome
            elif endereco.proprietario:
                currEndereco['proprietario'] = endereco.proprietario.nome
            elif endereco.imovel:
                currEndereco['imovel'] = endereco.imovel.matricula
            output.append(currEndereco)
        return jsonify(output)

    @api.expect(model_endereco_patch)
    @api.doc(description='Cadastra novo endereço')
    def post(self):
        dados_endereco = request.get_json()
        endereco = Endereco(rua=dados_endereco['rua'],
                            numero=dados_endereco['numero'],
                            andar=dados_endereco['numero'],
                            bloco=dados_endereco['bloco'],
                            bairro=dados_endereco['bairro'],
                            cep=dados_endereco['cep'],
                            cidade=dados_endereco['cidade'],
                            estado=dados_endereco['estado'],
                            cliente_id=dados_endereco['cliente_id'],
                            proprietario_id=dados_endereco['proprietario_id'],
                            imovel_id=dados_endereco['imovel_id'])
        db.session.add(endereco)
        db.session.commit()
        return jsonify('Endereço adicionada com sucesso!')


@endereco_namespace.route('/<int:endereco_id>')
class EnderecoCRUD(Resource):


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'endereco_id': 'Especifique o ID associado ao endereço'},
             description='Atualiza endereço cadastrado')
    def get(self, endereco_id):
        try:
            endereco = Endereco.query.get_or_404(endereco_id)
            currEndereco = {}
            currEndereco['id'] = endereco.id
            currEndereco['rua'] = endereco.rua
            currEndereco['numero'] = endereco.numero
            currEndereco['andar'] = endereco.andar
            currEndereco['bloco'] = endereco.bloco
            currEndereco['bairro'] = endereco.bairro
            currEndereco['cep'] = endereco.cep
            currEndereco['cidade'] = endereco.cidade
            currEndereco['estado'] = endereco.estado
            if endereco.cliente:
                currEndereco['cliente'] = endereco.cliente.nome
            elif endereco.proprietario:
                currEndereco['proprietario'] = endereco.proprietario.nome
            elif endereco.imovel:
                currEndereco['imovel'] = endereco.imovel.matricula
            return jsonify(currEndereco)
        except KeyError as e:
            endereco_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            endereco_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'endereco_id': 'Especifique o ID associado ao endereço'},
             description='Atualiza endereço cadastrado',
             body=model_endereco_patch)
    def patch(self, endereco_id):
        try:
            dados_endereco = request.get_json()
            endereco = Endereco.query.get_or_404(endereco_id)
            endereco.rua = dados_endereco.get('rua', endereco.rua)
            endereco.numero = dados_endereco.get('numero', endereco.numero)
            endereco.andar = dados_endereco.get('andar', endereco.andar)
            endereco.bloco = dados_endereco.get('bloco', endereco.bloco)
            endereco.bairro = dados_endereco.get('bairro', endereco.bairro)
            endereco.cep = dados_endereco.get('cep', endereco.cep)
            endereco.cidade = dados_endereco.get('cidade', endereco.cidade)
            endereco.estado = dados_endereco.get('estado', endereco.estado)
            endereco.cliente_id = dados_endereco.get('cliente_id', endereco.cliente_id)
            endereco.proprietario_id = dados_endereco.get('proprietario_id', endereco.proprietario_id)
            endereco.imovel_id = dados_endereco.get('imovel_id', endereco.imovel_id)
            db.session.commit()
            return jsonify('Endereço atualizado com sucesso!')
        except KeyError as e:
            endereco_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            endereco_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'endereco_id': 'Especifique o ID associado ao endereço'},
             description='Exclui endereço cadastrado')
    def delete(self, endereco_id):
        try:
            endereco = Endereco.query.get_or_404(endereco_id)
            db.session.delete(endereco)
            db.session.commit()
            return jsonify(f'Endereço foi excluído!')
        except KeyError as e:
            endereco_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            endereco_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
