create database cadastro_produtos; -- Criando database
use cadastro_produtos;

create table produtos(
id int not null auto_increment,
codigo int,
descricao varchar(50),
preco double,
categoria varchar(50),
primary key(id)

); -- criando a tabela produtos que irá armezenar os dados do programa

describe produtos; -- verificando a tabela

select * from produtos; -- verificando a tabela

alter table produtos add column data datetime; -- Adicionando uma nova coluna para receber a data
-- de criacao do produto