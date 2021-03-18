'''
Estruturação em pacotes python para proporcionar melhor organização e impedir
que ocorram erros por imports cíclicos
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Carrega informações sensíveis do arquivo .env
load_dotenv()
password = os.environ['PASSWORD']
secret_key = os.environ['SECRET_KEY']

app = Flask(__name__)

# Permite Cross-origin resource sharing
CORS(app)

# URI do PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:{password}@localhost/sistemavendaimoveis"
app.config['SECRET_KEY'] = secret_key

db = SQLAlchemy(app)

api = Api(app=app,
          version="1.0",
          title= "Sistema de Venda de Imóveis",
          description="Gerencia clientes, proprietários, imóveis, endereços, transações, categoria de imóvel, "
                      "custo de imóveis, estado civil e bancos.")

from sistemavendaimoveis.API import cliente, proprietario, estadocivil, imovel, transacao, endereco, categoria
from sistemavendaimoveis.API import custo, banco
