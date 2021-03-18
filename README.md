I-) Mapa de Pastas:

1-) Angular
1.1-) vendas* 

2-) Banco de Dados
2.1-) Modelo Conceitual e Lógico
2.2-) Scripts-PostgreSQL

3-) Python-Flask-API*
 - requirements.txt  # pacotes que devem ser instalados.

Legenda:
*Abra esta pasta no seu Editor!



II-) Instruções:

1-) Criação do Banco de Dados no PostgreSQL:
    1.1-) Utilize o script BD-Sistema-Vendas da pasta Scripts-PostgreSQL e execute a linha de criação do banco de dados;
    1.2-) Mude a conexão para o banco recém-criado;
    1.3-) Execute as linhas de criação das tabelas;
    1.4-) Insira os valores pré-estabelecidos;
    1.5-) Insira os valores para teste;

2-) Crie uma máquina virtual, ative-a e instale os pacotes necessários:
	2.1-) No terminal: python -m venv [diretório];
    2.2-) Vá até o diretório utilizando cd;
	2.3-) .\Scripts\activate  # Inicializa a venv
	2.4-) cd [diretório requirements.txt]
	2.5-) pip install -r requirements.txt  # Instala os pacotes necessários

3-) No seu editor de código, selecione a pasta 'Python-Flask-API'. Escolha a venv recém-criada como interpretador.
    3.1-) Adicione a sua senha do PostgreSQL no arquivo '.env';
    3.2-) Rode o arquivo 'run.py';
    3.3-) Acesse '127.0.0.1:5000/' para ter acesso ao Swagger, a API está funcionando!

4-) No seu editor de código, selecione a pasta 'vendas'.
    4.1-) No terminal, execute 'npm install' para instalar a pasta node_modules;
    4.2-) No terminal, execute ng serve;
    4.3-) Acesse 'localhost:4200/' para ter acesso ao 'DOMINIUM - Sistema de Venda de Imóveis'