drop database EscolaBD;
create database EscolaBD;

use EscolaBD;
/*criando tabelas*/
create table pessoa (
	CPF int primary key not null,
    matricula int,
    nome varchar(45) not null,
	telefone varchar(45) not null,
    endereco varchar(45) not null,
    estadoCivil varchar(45) not null,
    nascimento date);
create table disciplina (
	idDisciplina int primary key not null,
    idturma int not null,
    matricula int 
);
create table professor (
    formacao varchar(45) not null,
    idDisciplina varchar(45) not null,
    turma varchar(1) not null);
create table cargo (
	idcargo int primary key not null,
    nome varchar(45) not null,
    funcao varchar(45) not null);
create table aluno( 
	serie int not null,
    periodo varchar(45) not null
);
create table turma (
	idturma int not null primary key,
    turno varchar(45)
);
create table disciplina (
	idDisciplina int not null primary key,
    idturma int not null,
    matricula int 
);
create table avisos (
	idAviso int not null,
    dataAviso date,
    matricula varchar(40), /*id professor remetente da mensagem*/
    CPFresponsalvel varchar(40) /*destinatario da mensagem*/
);
create table responsavel (
	filhos int not null
);
create table avaliacao (
	tipo varchar(45) not null,
    dataAvaliacao date not null,
    idDisciplina int not null,
    idturma int not null,
    notaAvialicao int
);
create table tempoEstudo (
	idDisciplina int not null,
    matricula int not null, /*aluno*/
    tempo time
);
create table notafinal (
	idDisciplina int not null,
    idturma int not null,
    matricula int, /*aluno*/
    nota int
);
/*registro, tem que ser 5 p/ cada tabela */
insert into pessoa (CPF, matricula, nome, telefone, endereco, estadoCivil, nascimento) values ('01', '001', 'Marcella', 'rua 01 casa 159', '1111', 'casada', '1970-05-09');
insert into pessoa (CPF, matricula, nome, telefone, endereco, estadoCivil, nascimento) values ('02', '002', 'Mauricio', 'rua 02 casa 198', '1112', 'casado', '1988-03-01');
insert into pessoa (CPF, matricula, nome, telefone, endereco, estadoCivil, nascimento) values ('03', '003', 'Denilson', 'rua 03 casa 155', '1113', 'casado', '1982-04-03');
insert into pessoa (CPF, matricula, nome, telefone, endereco, estadoCivil, nascimento) values ('04', '004', 'Julianna', 'rua 04 casa 199', '1114', 'casada', '1988-09-05');
insert into pessoa (CPF, matricula, nome, telefone, endereco, estadoCivil, nascimento) values ('05', '005', 'Fabricio', 'rua 05 casa 200', '1115', 'solteiro', '1988-08-22');

insert into disciplina (idDisciplina, idturma, matricula) values ('1', '1', '001');
insert into disciplina (idDisciplina, idturma, matricula) values ('2', '2', '002');
insert into disciplina (idDisciplina, idturma, matricula) values ('3', '3', '003');
insert into disciplina (idDisciplina, idturma, matricula) values ('4', '4', '004');
insert into disciplina (idDisciplina, idturma, matricula) values ('5', '5', '005');

insert into professor (formacao, idDisciplina, turma) values ('matematica', '1', 'A');
insert into professor (formacao, idDisciplina, turma) values ('geografia', '2', 'A');
insert into professor (formacao, idDisciplina, turma) values ('fisica', '3', 'A');
insert into professor (formacao, idDisciplina, turma) values ('quimica', '4', 'A');
insert into professor (formacao, idDisciplina, turma) values ('biologia', '5', 'A');

/*views*/
drop view pessoas;
create view pessoas as
select 'Meteria', matricula, idturma, idDisciplina from disciplina
union all
select 'professor', formacao, turma, idDisciplina from professor
order by idDisciplina;

select * from pessoas;





