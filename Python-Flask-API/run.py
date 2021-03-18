'''
Arquivo que deve ser executado para inicializar o banco de dados e a API.
'''

from sistemavendaimoveis import app

if __name__ == '__main__':
    app.run(debug=True)
