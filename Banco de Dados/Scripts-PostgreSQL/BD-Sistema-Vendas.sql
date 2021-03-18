''' Criação do Banco de Dados '''
CREATE DATABASE "sistemavendaimoveis";

''' Conecte-se ao banco "sistemavendaimoveis" '''

''' Criação de Tabelas '''
CREATE TABLE Ecivil(
    id SERIAL PRIMARY KEY,
    nome VARCHAR (100) UNIQUE NOT NULL
);

CREATE TABLE Banco(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE Categoria (
	id SERIAL PRIMARY KEY,
	nome VARCHAR (100) NOT NULL UNIQUE
);

CREATE TABLE Proprietario(
    id SERIAL PRIMARY KEY,
    nome VARCHAR (150) NOT NULL,
    cpf VARCHAR (25) UNIQUE NOT NULL,
	rg VARCHAR (25) UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
	profissao VARCHAR (100) NOT NULL,
	celular VARCHAR (20) NOT NULL,
	telefone VARCHAR (20),
    email VARCHAR (150) UNIQUE NOT NULL,
	
	estado_civil_id INT NOT NULL,
	FOREIGN KEY (estado_civil_id)
		REFERENCES Ecivil(id)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Imovel(
	id SERIAL PRIMARY KEY,
	data_posse DATE NOT NULL,
	matricula VARCHAR (100) NOT NULL UNIQUE,
	
	categoria_id INT NOT NULL,
	proprietario_id INT NOT NULL,
	FOREIGN KEY (categoria_id)
		REFERENCES Categoria(id)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (proprietario_id)
		REFERENCES Proprietario(id)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Custo(
	id SERIAL PRIMARY KEY,
	luz FLOAT DEFAULT 0.0,
	agua FLOAT DEFAULT 0.0,
	condominio FLOAT DEFAULT 0.0,
	propaganda FLOAT DEFAULT 0.0,
	mes DATE DEFAULT NOW(),
	
	imovel_id INT NOT NULL,
	FOREIGN KEY (imovel_id)
		REFERENCES Imovel(id)
		ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE Cliente(
    id SERIAL PRIMARY KEY,
    nome VARCHAR (150) NOT NULL,
    cpf VARCHAR (25) UNIQUE NOT NULL,
	rg VARCHAR (25) UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
	profissao VARCHAR (100) NOT NULL,
	celular VARCHAR (20) NOT NULL,
	telefone VARCHAR (20),
    email VARCHAR (150) UNIQUE NOT NULL,
	
	estado_civil_id INT NOT NULL,
	FOREIGN KEY (estado_civil_id)
		REFERENCES Ecivil(id)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Endereco(
	id SERIAL PRIMARY KEY,
	rua VARCHAR (150) NOT NULL,
	numero VARCHAR (10) NOT NULL,
	andar INT,
	bloco INT,
	bairro VARCHAR (100) NOT NULL,
	cep VARCHAR (20) NOT NULL,
	cidade VARCHAR (100) NOT NULL,
	estado VARCHAR (100) NOT NULL,
	
	cliente_id INT,
	proprietario_id INT,
	imovel_id INT,
	FOREIGN KEY (cliente_id)
		REFERENCES Cliente(id)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (proprietario_id)
		REFERENCES Proprietario(id)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (imovel_id)
		REFERENCES Imovel(id)
		ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Transacao(
	id SERIAL PRIMARY KEY,
	valor FLOAT NOT NULL,
	data_transacao DATE NOT NULL,
	financiamento BOOLEAN NOT NULL,
	
	cliente_id INT NOT NULL,
	proprietario_id INT NOT NULL,
	banco_id INT,
	imovel_id INT NOT NULL,
	FOREIGN KEY (cliente_id)
		REFERENCES Cliente(id)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (proprietario_id)
		REFERENCES Proprietario(id)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (banco_id)
		REFERENCES Banco(id)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (imovel_id)
		REFERENCES Imovel(id)
		ON UPDATE CASCADE ON DELETE CASCADE
);

''' Inserção de valores pré-estabelecidos nas Tabelas Banco, Ecivil e Categoria '''

INSERT into public.banco (nome)
	VALUES ('Itaú'),
			('Bradesco'),
			('Santander');

INSERT into public.ecivil (nome)
	VALUES ('Solteiro'),
			('Casado'),
			('Separado'),
			('Divorciado'),
			('Viúvo');

INSERT into public.categoria (nome)
	VALUES ('Casa'),
			('Apartamento'),
			('Kitnet');


''' Inserção de valores para teste '''

INSERT into public.cliente (nome, cpf, rg, data_nascimento, profissao, celular, email, estado_civil_id)
		VALUES ('Matheus Germano Dos Santos', '99999999999', '999999999', '1994-04-17', 'Programador', '19999999999', 'santos.matheus.germano@gmail.com', 1);

INSERT into public.proprietario (nome, cpf, rg, data_nascimento, profissao, celular, email, estado_civil_id)
		VALUES ('João Tavares', '99999999999', '999999999', '1997-12-03', 'Advogado', '19982654504', 'joao@gmail.com', 2);
		
INSERT into public.endereco (rua, numero, bairro, cep, cidade, estado, cliente_id)
		VALUES ('Rua das Caixas', '395', 'Jardim Esperança', '13482000', 'Limeira', 'São Paulo', 1);

INSERT into public.endereco (rua, numero, bairro, cep, cidade, estado, proprietario_id)
		VALUES ('Rua Gato Sampaio', '19', 'Jardim Santa Josefa', '13482222', 'Campinas', 'São Paulo', 1);
				
INSERT into public.imovel (matricula, data_posse, categoria_id, proprietario_id)
		VALUES ('104.402', '2002-02-15', 1, 1);

INSERT into public.endereco (rua, numero, bairro, cep, cidade, estado, imovel_id)
		VALUES ('Rogério Bilaque', '222', 'Cambuí', '13222222', 'Campinas', 'São Paulo', 1);

INSERT into public.custo (luz, agua, propaganda, imovel_id)
		VALUES (100, 200, 400, 1);

INSERT into public.transacao (valor, data_transacao, financiamento, cliente_id, proprietario_id, banco_id, imovel_id)
		VALUES (1000000.00, '2022-03-15', True, 1, 1, 1, 1);
