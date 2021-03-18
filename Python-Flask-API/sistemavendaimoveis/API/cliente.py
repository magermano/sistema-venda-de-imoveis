'''
Criação da API REST, de namespace 'Clientes', relação de respostas possíveis.
'''

from flask import request, jsonify
from flask_restplus import Resource, fields
from sistemavendaimoveis import db, api
from sistemavendaimoveis.models import Cliente


cliente_namespace = api.namespace('Clientes',
                                  description='API para listagem, atualização, inserção e '
                                              'exclusão de cliente.')



model_cliente = api.model('Modelo Cliente', {
    'nome': fields.String(required = True,
                          description = 'Nome do Cliente',
                          help='Nome não pode ser branco'),
    'cpf': fields.String(required = True,
                          description = 'CPF do Cliente',
                          help='CPF não pode ser branco'),
    'rg': fields.String(required = True,
                          description = 'RG do Cliente',
                          help='RG não pode ser branco'),
    'data_nascimento': fields.DateTime(required = True,
                          description = 'Data de Nascimento do Cliente',
                          help='Data de Nascimento não pode ser branco',
                          dt_format='rfc822'),
    'profissao': fields.String(required = True,
                          description = 'Profissão do Cliente',
                          help='Profissão não pode ser branco'),
    'celular': fields.String(required = True,
                          description = 'Celular do Cliente',
                          help='Celular não pode ser branco'),
    'telefone': fields.String(required = False,
                          description = 'Telefone do Cliente',
                          help='Telefone pode ser branco'),
    'email': fields.String(required = True,
                          description = 'Email do Cliente',
                          help='Email não pode ser branco'),
    'estado_civil_id': fields.Integer(required = True,
                          description = 'ID do Estado Civil do Cliente',
                          help='ID do Estado Civil não pode ser branco')
})

model_cliente_patch = api.model('Modelo Cliente', {
    'nome': fields.String(required = False,
                          description = 'Nome do Cliente',
                          help='Nome não pode ser branco'),
    'cpf': fields.String(required = False,
                          description = 'CPF do Cliente',
                          help='CPF não pode ser branco'),
    'rg': fields.String(required = False,
                          description = 'RG do Cliente',
                          help='RG não pode ser branco'),
    'data_nascimento': fields.DateTime(required = False,
                          description = 'Data de Nascimento do Cliente',
                          help='Data de Nascimento não pode ser branco',
                          dt_format='rfc822'),
    'profissao': fields.String(required = False,
                          description = 'Profissão do Cliente',
                          help='Profissão não pode ser branco'),
    'celular': fields.String(required = False,
                          description = 'Celular do Cliente',
                          help='Celular não pode ser branco'),
    'telefone': fields.String(required = False,
                          description = 'Telefone do Cliente',
                          help='Telefone pode ser branco'),
    'email': fields.String(required = False,
                          description = 'Email do Cliente',
                          help='Email não pode ser branco'),
    'estado_civil_id': fields.Integer(required = False,
                          description = 'ID do Estado Civil do Cliente',
                          help='ID do Estado Civil não pode ser branco')
})

@cliente_namespace.route('/')
class ClienteList(Resource):

    @api.doc(description= 'Busca todos os clientes')
    def get(self):
        clientes = Cliente.query.all()
        output = []
        for cliente in clientes:
            currCliente = {}
            currCliente['nome'] = cliente.nome
            currCliente['cpf'] = cliente.cpf
            currCliente['rg'] = cliente.rg
            currCliente['data_nascimento'] = cliente.data_nascimento
            currCliente['profissao'] = cliente.profissao
            currCliente['celular'] = cliente.celular
            currCliente['telefone'] = cliente.telefone
            currCliente['email'] = cliente.email
            currCliente['estado_civil'] = cliente.ecivil.nome
            currCliente['id'] = cliente.id
            currCliente['enderecos'] = []
            if cliente.enderecos:
                for endereco in cliente.enderecos:
                    dict_endereco = {}
                    dict_endereco['rua'] = endereco.rua
                    dict_endereco['numero'] = endereco.numero
                    if endereco.andar:
                        dict_endereco['andar'] = endereco.andar
                    if endereco.bloco:
                        dict_endereco['bloco'] = endereco.bloco
                    dict_endereco['bairro'] = endereco.bairro
                    dict_endereco['cep'] = endereco.cep
                    dict_endereco['cidade'] = endereco.cidade
                    dict_endereco['estado'] = endereco.estado
                    currCliente['enderecos'].append(dict_endereco)
            output.append(currCliente)
        return jsonify(output)

    @api.expect(model_cliente)
    @api.doc(description='Cadastra novo cliente')
    def post(self):
        dados_cliente = request.get_json()
        cliente = Cliente(nome=dados_cliente['nome'], cpf=dados_cliente['cpf'], rg=dados_cliente['rg'],
                          data_nascimento=dados_cliente['data_nascimento'], profissao=dados_cliente['profissao'],
                          celular=dados_cliente['celular'], telefone=dados_cliente['telefone'],
                          email=dados_cliente['email'], estado_civil_id=dados_cliente['estado_civil_id'])
        db.session.add(cliente)
        db.session.commit()
        return jsonify(dados_cliente)


@cliente_namespace.route('/<int:cliente_id>')
class ClienteCRUD(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'cliente_id': 'Especifique o ID associado ao cliente'},
             description='Atualiza cliente cadastrado')
    def get(self, cliente_id):
        try:
            cliente = Cliente.query.get_or_404(cliente_id)
            currCliente = {}
            currCliente['nome'] = cliente.nome
            currCliente['cpf'] = cliente.cpf
            currCliente['rg'] = cliente.rg
            currCliente['data_nascimento'] = cliente.data_nascimento
            currCliente['profissao'] = cliente.profissao
            currCliente['celular'] = cliente.celular
            currCliente['telefone'] = cliente.telefone
            currCliente['email'] = cliente.email
            currCliente['estado_civil'] = cliente.ecivil.nome
            currCliente['id'] = cliente.id
            currCliente['enderecos'] = []
            if cliente.enderecos:
                for endereco in cliente.enderecos:
                    dict_endereco = {}
                    dict_endereco['rua'] = endereco.rua
                    dict_endereco['numero'] = endereco.numero
                    if endereco.andar:
                        dict_endereco['andar'] = endereco.andar
                    if endereco.bloco:
                        dict_endereco['bloco'] = endereco.bloco
                    dict_endereco['bairro'] = endereco.bairro
                    dict_endereco['cep'] = endereco.cep
                    dict_endereco['cidade'] = endereco.cidade
                    dict_endereco['estado'] = endereco.estado
                    currCliente['enderecos'].append(dict_endereco)
            return jsonify(currCliente)
        except KeyError as e:
            cliente_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            cliente_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.expect(model_cliente_patch)
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'cliente_id': 'Especifique o ID associado ao cliente'},
             description='Atualiza cliente cadastrado. Permite atualizar um ou mais campos',
             body=model_cliente_patch)
    def patch(self, cliente_id):
        try:
            dados_cliente = request.get_json()
            print(type(dados_cliente))
            cliente = Cliente.query.get_or_404(cliente_id)
            cliente.nome = dados_cliente.get('nome', cliente.nome)
            cliente.cpf = dados_cliente.get('cpf', cliente.cpf)
            cliente.rg = dados_cliente.get('rg', cliente.rg)
            cliente.data_nascimento = dados_cliente.get('data_nascimento', cliente.data_nascimento)
            cliente.profissao = dados_cliente.get('profissao', cliente.profissao)
            cliente.celular = dados_cliente.get('celular', cliente.celular)
            cliente.telefone = dados_cliente.get('telefone', cliente.telefone)
            cliente.email = dados_cliente.get('email', cliente.email)
            cliente.estado_civil_id = dados_cliente.get('estado_civil_id', cliente.estado_civil_id)
            db.session.commit()
            return jsonify('Cliente atualizado com sucesso!')
        except KeyError as e:
            cliente_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            cliente_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'cliente_id': 'Especifique o ID associado ao cliente'},
             description='Exclui cliente cadastrado')
    def delete(self, cliente_id):
        try:
            cliente = Cliente.query.get_or_404(cliente_id)
            nome_cliente = cliente.nome
            db.session.delete(cliente)
            db.session.commit()
            return jsonify(f'Cliente {nome_cliente} foi excluído(a)!')
        except KeyError as e:
            cliente_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            cliente_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
