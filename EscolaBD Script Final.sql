drop database EscolaBD;
create database EscolaBD;

use EscolaBD;

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