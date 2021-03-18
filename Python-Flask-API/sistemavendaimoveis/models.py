'''
Criação das tabelas utilizando SQLAlchemy

Utilizado 'db.relationship' com 'backref' para relações 'one-to-many',
que permite utilizar o atributo backref como se fosse uma coluna da tabela pai.
O SQLAlchemy roda uma query no background e nos permite conseguir os dados de forma prática.

Criado um __repr__ para retornar uma string de objeto mais amigável ao usuário.
'''

from sistemavendaimoveis import db
from datetime import datetime


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.String(20), nullable=False, unique=True)
    rg = db.Column(db.String(20), nullable=False, unique=True)
    data_nascimento = db.Column(db.DateTime, nullable=False)
    profissao = db.Column(db.String(100), nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(150), nullable=False, unique=True)
    estado_civil_id = db.Column(db.Integer, db.ForeignKey('ecivil.id'), nullable=False)
    enderecos = db.relationship('Endereco', cascade="all,delete", backref='cliente', lazy=True)
    transacoes = db.relationship('Transacao', cascade="all,delete", backref='cliente', lazy=True)

    def __repr__(self):
        return f"Cliente('{self.nome}', '{self.cpf}', '{self.rg}', '{self.data_nascimento.strftime('%d/%m/%Y')}', " \
               f"'{self.profissao}', {self.celular}', '{self.telefone}', '{self.email}', '{self.ecivil.nome}')"


class Proprietario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.String(20), nullable=False, unique=True)
    rg = db.Column(db.String(20), nullable=False, unique=True)
    data_nascimento = db.Column(db.DateTime, nullable=False)
    profissao = db.Column(db.String(100), nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(150), nullable=False, unique=True)
    estado_civil_id = db.Column(db.Integer, db.ForeignKey('ecivil.id'), nullable=False)
    enderecos = db.relationship('Endereco', cascade="all,delete", backref='proprietario', lazy=True)
    transacoes = db.relationship('Transacao', cascade="all,delete", backref='proprietario', lazy=True)
    imoveis = db.relationship('Imovel', cascade="all,delete", backref='proprietario', lazy=True)

    def __repr__(self):
        return f"Proprietario('{self.nome}', '{self.cpf}', '{self.rg}', '{self.data_nascimento.strftime('%d/%m/%Y')}', " \
               f"'{self.profissao}', '{self.celular}', '{self.telefone}', '{self.email}', '{self.ecivil.nome}')"


class Ecivil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    clientes = db.relationship('Cliente', cascade="all,delete", backref='ecivil', lazy=True)
    proprietarios = db.relationship('Proprietario', cascade="all,delete", backref='ecivil', lazy=True)

    def __repr__(self):
        return f"Estado Civil('{self.nome}')"


class Imovel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_posse = db.Column(db.DateTime, nullable=False)
    matricula = db.Column(db.String(100), nullable=False, unique=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    proprietario_id = db.Column(db.Integer, db.ForeignKey('proprietario.id'), nullable=False)
    enderecos = db.relationship('Endereco', cascade="all,delete", backref='imovel', lazy=True)
    custos = db.relationship('Custo', cascade="all,delete", backref='imovel', lazy=True)
    transacoes = db.relationship('Transacao', cascade="all,delete", backref='imovel', lazy=True)

    def __repr__(self):
        return f"Imovel('{self.data_posse.strftime('%d/%m/%Y')}')"


class Transacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_transacao = db.Column(db.DateTime, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    financiamento = db.Column(db.Boolean, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    proprietario_id = db.Column(db.Integer, db.ForeignKey('proprietario.id'), nullable=False)
    banco_id = db.Column(db.Integer, db.ForeignKey('banco.id'))
    imovel_id = db.Column(db.Integer, db.ForeignKey('imovel.id'), nullable=False)

    def __repr__(self):
        return f"Transacao('{self.valor}', '{self.data_transacao.strftime('%d/%m/%Y')}')"


class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(150), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    andar = db.Column(db.Integer)
    bloco = db.Column(db.Integer)
    bairro = db.Column(db.String(100), nullable=False)
    cep = db.Column(db.String(20), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado= db.Column(db.String(100), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    proprietario_id = db.Column(db.Integer, db.ForeignKey('proprietario.id'))
    imovel_id = db.Column(db.Integer, db.ForeignKey('imovel.id'))

    def __repr__(self):
        return f"Endereco('{self.rua}', '{self.numero}', '{self.andar}', '{self.bloco}'," \
               f"'{self.bairro}', '{self.cidade}', '{self.cep}', '{self.estado}')"


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    imoveis = db.relationship('Imovel', cascade="all,delete", backref='categoria', lazy=True)

    def __repr__(self):
        return f"Categoria('{self.nome}')"


class Custo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    luz = db.Column(db.Float, default=0)
    agua = db.Column(db.Float, default=0)
    condominio = db.Column(db.Float, default=0)
    propaganda = db.Column(db.Float, default=0)
    mes = db.Column(db.DateTime, default=datetime.utcnow)
    imovel_id = db.Column(db.Integer, db.ForeignKey('imovel.id'))

    def __repr__(self):
        return f"Custo('{self.mes.strftime('%m')}', '{self.luz}', '{self.agua}', '{self.condominio}', " \
               f"'{self.propaganda}')"


class Banco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False, unique=True)
    transacoes = db.relationship('Transacao', cascade="all,delete", backref='banco', lazy=True)

    def __repr__(self):
        return f"Banco('{self.nome}')"
