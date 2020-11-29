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
create table avisos (
	idAviso int not null,
    dataAviso date,
    matricula varchar(40), /*id professor remetente da mensagem*/
    CPFresponsalvel varchar(40) /*destinatario da mensagem*/
);
create table responsavel (
	nome varchar(45) not null,
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

insert into professor (formacao, idDisciplina, idturma) values ('matematica', '1', '5');
insert into professor (formacao, idDisciplina, idturma) values ('geografia', '2', '6');
insert into professor (formacao, idDisciplina, idturma) values ('fisica', '3', '7');
insert into professor (formacao, idDisciplina, idturma) values ('quimica', '4', '8');
insert into professor (formacao, idDisciplina, idturma) values ('biologia', '5', '9');

insert into cargo (idcargo, nome, funcao) values ('10', 'Mara', 'Diretora');
insert into cargo (idcargo, nome, funcao) values ('11', 'Mario', 'professor');
insert into cargo (idcargo, nome, funcao) values ('12', 'Marta', 'aluna');
insert into cargo (idcargo, nome, funcao) values ('13', 'Marcio', 'responsavel');
insert into cargo (idcargo, nome, funcao) values ('14', 'Martin', 'aluno');

insert into aluno (idturma, nome, turno) values ('5', 'Chico' , 'diurno');
insert into aluno (idturma, nome, turno) values ('5', 'Carlos', 'diurno');
insert into aluno (idturma, nome, turno) values ('5', 'Carla' , 'diurno');
insert into aluno (idturma, nome, turno) values ('8', 'Cassia', 'diurno');
insert into aluno (idturma, nome, turno) values ('9', 'Cassio', 'diurno');

insert into turma (idturma, turno) values ('5', 'diurno');
insert into turma (idturma, turno) values ('6', 'diurno');
insert into turma (idturma, turno) values ('7', 'diurno');
insert into turma (idturma, turno) values ('8', 'diurno');
insert into turma (idturma, turno) values ('9', 'diurno');

insert into avisos (idAviso,dataAviso,matricula, CPFresponsalvel) values ('01','2020-10-10','220','01');
insert into avisos (idAviso,dataAviso,matricula, CPFresponsalvel) values ('02','2020-09-10','221','02');
insert into avisos (idAviso,dataAviso,matricula, CPFresponsalvel) values ('01','2020-10-10','220','01');
insert into avisos (idAviso,dataAviso,matricula, CPFresponsalvel) values ('01','2020-10-10','220','01');
insert into avisos (idAviso,dataAviso,matricula, CPFresponsalvel) values ('01','2020-10-10','220','01');


insert into responsavel (nome ,filhos) values ('Anna',1);
insert into responsavel (nome ,filhos) values ('Allan',2);
insert into responsavel (nome ,filhos) values ('Paula',2);
insert into responsavel (nome ,filhos) values ('Paulo',3);
insert into responsavel (nome ,filhos) values ('Amanda',5);

insert into avaliacao (	tipo, dataAvaliacao, idDisciplina, idturma, notaAvialicao) values ('prova','2020-12-05','1','5','10');
insert into avaliacao (	tipo, dataAvaliacao, idDisciplina, idturma, notaAvialicao) values ('prova','2020-10-25','2','6','10');
insert into avaliacao (	tipo, dataAvaliacao, idDisciplina, idturma, notaAvialicao) values ('trabalho','2020-9-04','3','7','10');
insert into avaliacao (	tipo, dataAvaliacao, idDisciplina, idturma, notaAvialicao) values ('teste','2020-12-03','4','8','5');
insert into avaliacao (	tipo, dataAvaliacao, idDisciplina, idturma, notaAvialicao) values ('teste','2020-12-08','5','9','5');
 
insert into tempoEstudo (idDisciplina,matricula,tempo) values ('9','220','01:00:00');
insert into tempoEstudo (idDisciplina,matricula,tempo) values ('8','221','02:00:00');
insert into tempoEstudo (idDisciplina,matricula,tempo) values ('7','222','00:00:00');
insert into tempoEstudo (idDisciplina,matricula,tempo) values ('6','223','09:00:00');
insert into tempoEstudo (idDisciplina,matricula,tempo) values ('5','224','06:00:00');

insert into notafinal (idDisciplina,idturma,matricula, nota) values ('1','5','220','0');
insert into notafinal (idDisciplina,idturma,matricula, nota) values ('2','6','221','10');
insert into notafinal (idDisciplina,idturma,matricula, nota) values ('3','7','222','5');
insert into notafinal (idDisciplina,idturma,matricula, nota) values ('4','8','223','6');
insert into notafinal (idDisciplina,idturma,matricula, nota) values ('5','9','224','9');

/*views*/
drop view pessoas;
create view pessoas as
select 'Meteria', matricula, idturma, idDisciplina from disciplina
union all
select 'professor', formacao, turma, idDisciplina from professor
order by idDisciplina;

select * from pessoas;

DELIMITER $$
DROP PROCEDURE IF EXISTS mediaAluno $$
CREATE PROCEDURE mediaAluno (n1 FLOAT, n2 int)
main: BEGIN 

DECLARE MEDIA FLOAT;
DECLARE NOTAFINAL FLOAT;
set MEDIA = n1 + n2;
set NOTAFINAL = MEDIA/2;
SELECT NOTAFINAL AS notaFinal;

END $$

DELIMITER ;

CALL mediaAluno(7,7);








