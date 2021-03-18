'''
Criação da API REST, de namespace 'Proprietarios', relação de respostas possíveis.
'''
from flask import request, jsonify
from flask_restplus import Resource, fields
from sistemavendaimoveis import db, api
from sistemavendaimoveis.models import Proprietario

proprietario_namespace = api.namespace('Proprietarios',
                                       description='API para listagem, atualização, inserção e '
                                                   'exclusão de proprietário')


model_proprietario = api.model('Modelo Proprietário', {
    'nome': fields.String(required = True,
                          description = 'Nome do Proprietário',
                          help='Nome não pode ser branco'),
    'cpf': fields.String(required = True,
                          description = 'CPF do Proprietário',
                          help='CPF não pode ser branco'),
    'rg': fields.String(required = True,
                          description = 'RG do Proprietário',
                          help='RG não pode ser branco'),
    'data_nascimento': fields.DateTime(required = True,
                          description = 'Data de Nascimento do Proprietário',
                          help='Data de Nascimento não pode ser branco',
                          dt_format='rfc822'),
    'profissao': fields.String(required = True,
                          description = 'Profissão do Proprietário',
                          help='Profissão não pode ser branco'),
    'celular': fields.String(required = True,
                          description = 'Celular do Proprietário',
                          help='Celular não pode ser branco'),
    'telefone': fields.String(required = False,
                          description = 'Telefone do Proprietário',
                          help='Telefone pode ser branco'),
    'email': fields.String(required = True,
                          description = 'Email do Proprietário',
                          help='Email não pode ser branco'),
    'estado_civil_id': fields.Integer(required = True,
                          description = 'ID do Estado Civil do Proprietário',
                          help='ID do Estado Civil não pode ser branco')
})

model_proprietario_patch = api.model('Modelo Proprietário', {
    'nome': fields.String(required = False,
                          description = 'Nome do Proprietário',
                          help='Nome não pode ser branco'),
    'cpf': fields.String(required = False,
                          description = 'CPF do Proprietário',
                          help='CPF não pode ser branco'),
    'rg': fields.String(required = False,
                          description = 'RG do Proprietário',
                          help='RG não pode ser branco'),
    'data_nascimento': fields.DateTime(required = False,
                          description = 'Data de Nascimento do Proprietário',
                          help='Data de Nascimento não pode ser branco',
                          dt_format='rfc822'),
    'profissao': fields.String(required = False,
                          description = 'Profissão do Proprietário',
                          help='Profissão não pode ser branco'),
    'celular': fields.String(required = False,
                          description = 'Celular do Proprietário',
                          help='Celular não pode ser branco'),
    'telefone': fields.String(required = False,
                          description = 'Telefone do Proprietário',
                          help='Telefone pode ser branco'),
    'email': fields.String(required = False,
                          description = 'Email do Proprietário',
                          help='Email não pode ser branco'),
    'estado_civil_id': fields.Integer(required = False,
                          description = 'ID do Estado Civil do Proprietário',
                          help='ID do Estado Civil não pode ser branco')
})


@proprietario_namespace.route('/')
class ProprietarioList(Resource):


    @api.doc(description= 'Busca todos os proprietários')
    def get(self):
        proprietarios = Proprietario.query.all()
        output = []
        for proprietario in proprietarios:
            currProprietario = {}
            currProprietario['nome'] = proprietario.nome
            currProprietario['cpf'] = proprietario.cpf
            currProprietario['rg'] = proprietario.rg
            currProprietario['data_nascimento'] = proprietario.data_nascimento
            currProprietario['profissao'] = proprietario.profissao
            currProprietario['celular'] = proprietario.celular
            currProprietario['telefone'] = proprietario.telefone
            currProprietario['email'] = proprietario.email
            currProprietario['estado_civil'] = proprietario.ecivil.nome
            currProprietario['id'] = proprietario.id
            currProprietario['enderecos'] = []
            currProprietario['imoveis'] = []
            if proprietario.enderecos:
                for endereco in proprietario.enderecos:
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
                    currProprietario['enderecos'].append(dict_endereco)
            output.append(currProprietario)
            if proprietario.imoveis:
                for imovel in proprietario.imoveis:
                    dict_imovel = {}
                    dict_imovel['data_posse'] = imovel.data_posse
                    dict_imovel['matricula'] = imovel.matricula
                    currProprietario['imoveis'].append(dict_imovel)
        return jsonify(output)


    @api.expect(model_proprietario)
    @api.doc(description='Cadastra novo proprietário')
    def post(self):
        dados_proprietario = request.get_json()
        proprietario = Proprietario(nome=dados_proprietario['nome'], cpf=dados_proprietario['cpf'],
                                    rg=dados_proprietario['rg'], data_nascimento=dados_proprietario['data_nascimento'],
                                    profissao=dados_proprietario['profissao'], celular=dados_proprietario['celular'],
                                    telefone=dados_proprietario['telefone'], email=dados_proprietario['email'],
                                    estado_civil_id=dados_proprietario['estado_civil_id'])
        db.session.add(proprietario)
        db.session.commit()
        return jsonify('Proprietário adicionado com sucesso!')


@proprietario_namespace.route('/<int:proprietario_id>')
class ProprietarioCRUD(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'proprietario_id': 'Especifique o ID associado ao proprietario'},
             description='Atualiza proprietário cadastrado')
    def get(self, proprietario_id):
        try:
            proprietario = Proprietario.query.get(proprietario_id)
            currProprietario = {}
            currProprietario['nome'] = proprietario.nome
            currProprietario['cpf'] = proprietario.cpf
            currProprietario['rg'] = proprietario.rg
            currProprietario['data_nascimento'] = proprietario.data_nascimento
            currProprietario['profissao'] = proprietario.profissao
            currProprietario['celular'] = proprietario.celular
            currProprietario['telefone'] = proprietario.telefone
            currProprietario['email'] = proprietario.email
            currProprietario['estado_civil'] = proprietario.ecivil.nome
            currProprietario['id'] = proprietario.id
            currProprietario['enderecos'] = []
            currProprietario['imoveis'] = []
            if proprietario.enderecos:
                for endereco in proprietario.enderecos:
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
                    currProprietario['enderecos'].append(dict_endereco)
            if proprietario.imoveis:
                for imovel in proprietario.imoveis:
                    dict_imovel = {}
                    dict_imovel['data_posse'] = imovel.data_posse
                    dict_imovel['matricula'] = imovel.matricula
                    currProprietario['imoveis'].append(dict_imovel)
            return jsonify(currProprietario)
        except KeyError as e:
            proprietario_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            proprietario_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


    @api.expect(model_proprietario_patch)
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'proprietario_id': 'Especifique o ID associado ao proprietario'},
             description='Atualiza proprietário cadastrado. Permite atualizar um ou mais campos',
             body=model_proprietario_patch)
    def patch(self, proprietario_id):
        try:
            dados_proprietario = request.get_json()
            proprietario = Proprietario.query.get_or_404(proprietario_id)
            proprietario.nome = dados_proprietario.get('nome', proprietario.nome)
            proprietario.cpf = dados_proprietario.get('cpf', proprietario.cpf)
            proprietario.rg = dados_proprietario.get('rg', proprietario.rg)
            proprietario.data_nascimento = dados_proprietario.get('data_nascimento', proprietario.data_nascimento)
            proprietario.profissao = dados_proprietario.get('profissao', proprietario.profissao)
            proprietario.celular = dados_proprietario.get('celular', proprietario.celular)
            proprietario.telefone = dados_proprietario.get('telefone', proprietario.telefone)
            proprietario.email = dados_proprietario.get('email', proprietario.email)
            proprietario.estado_civil_id = dados_proprietario.get('estado_civil_id', proprietario.estado_civil_id)
            db.session.commit()
            return jsonify('Proprietario atualizado com sucesso!')
        except KeyError as e:
            proprietario_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            proprietario_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'proprietario_id': 'Especifique o ID associado ao proprietario'},
             description='Exclui proprietário cadastrado')
    def delete(self, proprietario_id):
        try:
            proprietario = Proprietario.query.get_or_404(proprietario_id)
            db.session.delete(proprietario)
            db.session.commit()
            return jsonify(f'Proprietário foi excluído(a)!')
        except KeyError as e:
            proprietario_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            proprietario_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")
