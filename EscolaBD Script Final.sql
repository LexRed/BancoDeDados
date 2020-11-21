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

create table professor (
    formacao varchar(45) not null,
    disciplina varchar(45) not null,
    turma varchar(1) not null);

create table cargo (
	idcargo int primary key not null,
    nome varchar(45) not null,
    funcao varchar(45) not null);
    
    
create table aluno( 
	serie int not null,
    periodo varchar(45) not null,
);

create table turma (
	idturma int not null primary key,
    turno varchar(45)
);
    


