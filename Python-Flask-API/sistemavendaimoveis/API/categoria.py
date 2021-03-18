'''
Criação da API REST, de namespace 'Categoria-de-Imóvel', relação de respostas possíveis.
'''

from flask import request, jsonify
from flask_restplus import Resource, fields
from sistemavendaimoveis import db, api
from sistemavendaimoveis.models import Categoria

categoria_namespace = api.namespace('Categoria-de-Imóvel',
                                    description='API para listagem, atualização, inserção e '
                                                'exclusão de categorias de imóvel.')

model_categoria = api.model('Modelo Categoria de Imóvel', {
    'nome': fields.String(required=True,
                          description='Nome da Categoria de Imóvel',
                          help='Categoria de Imóvel não pode ser branco')
})


@categoria_namespace.route('/')
class CategoriaList(Resource):

    @api.doc(description='Busca todas as categorias de imóvel')
    def get(self):
        categorias = Categoria.query.all()
        output = []
        for categoria in categorias:
            currCategoria = {}
            currCategoria['id'] = categoria.id
            currCategoria['nome'] = categoria.nome
            output.append(currCategoria)
        return jsonify(output)

    @api.expect(model_categoria)
    @api.doc(description='Cadastra nova categoria de imóvel')
    def post(self):
        dados_categoria = request.get_json()
        categoria = Categoria(nome=dados_categoria['nome'])
        db.session.add(categoria)
        db.session.commit()
        return jsonify('Categoria adicionada com sucesso!')


@categoria_namespace.route('/<int:categoria_id>')
class CategoriaCRUD(Resource):

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'categoria_id': 'Especifique o ID associado à categoria de imóvel'},
             description='Atualiza categoria de imóvel cadastrada')
    def get(self, categoria_id):
        try:
            categoria = Categoria.query.get_or_404(categoria_id)
            currCategoria = {}
            currCategoria['id'] = categoria.id
            currCategoria['nome'] = categoria.nome
            return jsonify(currCategoria)
        except KeyError as e:
            categoria_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            categoria_namespace.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'categoria_id': 'Especifique o ID associado à categoria de imóvel'},
             description='Atualiza categoria de imóvel cadastrada',
             body=model_categoria)
    def patch(self, categoria_id):
        dados_categoria = request.get_json()
        categoria = Categoria.query.get_or_404(categoria_id)
        categoria.nome = dados_categoria.get('nome', categoria.nome)
        db.session.commit()
        return jsonify('Categoria de imóvel atualizada com sucesso!')

    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
             params={'categoria_id': 'Especifique o ID associado à categoria de imóvel'},
             description='Exclui categoria de imóvel cadastrado')
    def delete(self, categoria_id):
        categoria = Categoria.query.get_or_404(categoria_id)
        db.session.delete(categoria)
        db.session.commit()
        return jsonify(f'Categoria de imóvel foi excluída!')
