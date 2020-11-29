DROP SCHEMA escoladb;
CREATE SCHEMA escoladb; 
USE escoladb;

CREATE TABLE pessoa(
  cpf VARCHAR(11) NOT NULL,
  nome VARCHAR(45) NOT NULL,
  telefone VARCHAR(45) NOT NULL,
  endereco VARCHAR(300) NOT NULL,
  nascimento DATE NOT NULL,
  estado_civil VARCHAR(45) NOT NULL,
  PRIMARY KEY (cpf));

CREATE TABLE professor (
  matricula VARCHAR(8) NOT NULL,
  formacao VARCHAR(45) NOT NULL,
  pessoa_cpf VARCHAR(11) NOT NULL,
  PRIMARY KEY (matricula, pessoa_cpf),
  INDEX fk_professor_pessoa1_idx (pessoa_cpf ASC) VISIBLE,
  CONSTRAINT fk_professor_pessoa1
    FOREIGN KEY (pessoa_cpf)
    REFERENCES pessoa (cpf));

CREATE TABLE aluno (
  serie INT NOT NULL,
  periodo VARCHAR(45) NOT NULL,
  matricula VARCHAR(8) NOT NULL,
  pessoa_cpf VARCHAR(11) NOT NULL,
  PRIMARY KEY (matricula, pessoa_cpf),
  INDEX fk_aluno_pessoa1_idx (pessoa_cpf ASC) VISIBLE,
  CONSTRAINT fk_aluno_pessoa1
    FOREIGN KEY (pessoa_cpf)
    REFERENCES pessoa (cpf));

CREATE TABLE disciplina (
  id INT NOT NULL,
  plano_ensino MEDIUMTEXT NOT NULL,
  nome VARCHAR(45) NOT NULL,
  carga_horaria TIME NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE turma (
  id INT NOT NULL,
  turno VARCHAR(45) NOT NULL,
  disciplina_id INT NOT NULL,
  PRIMARY KEY (id, disciplina_id),
  INDEX fk_turma_disciplina1_idx (disciplina_id ASC) VISIBLE,
  CONSTRAINT fk_turma_disciplina1
    FOREIGN KEY (disciplina_id)
    REFERENCES disciplina (id));

CREATE TABLE cargo (
  id INT NOT NULL,
  nome VARCHAR(45) NOT NULL,
  funcao VARCHAR(45) NOT NULL,
  pessoa_cpf VARCHAR(11) NULL,
  PRIMARY KEY (id),
  INDEX fk_cargo_pessoa1_idx (pessoa_cpf ASC) VISIBLE,
  CONSTRAINT fk_cargo_pessoa1
    FOREIGN KEY (pessoa_cpf)
    REFERENCES pessoa (cpf));

CREATE TABLE tempo_estudo (
  tempo TIME NOT NULL,
  turma_id INT NOT NULL,
  aluno_matricula VARCHAR(8) NOT NULL,
  PRIMARY KEY (turma_id, aluno_matricula),
  INDEX fk_tempo_estudo_aluno1_idx (aluno_matricula ASC) VISIBLE,
  CONSTRAINT fk_tempo_estudo_turma1
    FOREIGN KEY (turma_id)
    REFERENCES turma (id),
  CONSTRAINT fk_tempo_estudo_aluno1
    FOREIGN KEY (aluno_matricula)
    REFERENCES aluno (matricula));

CREATE TABLE avaliacao (
  tipo VARCHAR(45) NOT NULL,
  valor FLOAT NOT NULL,
  data DATE NOT NULL,
  turma_id INT NOT NULL,
  aluno_matricula VARCHAR(8) NOT NULL,
  PRIMARY KEY (turma_id, aluno_matricula),
  INDEX fk_avaliação_aluno1_idx (aluno_matricula ASC) VISIBLE,
  CONSTRAINT fk_avaliação_turma1
    FOREIGN KEY (turma_id)
    REFERENCES turma (id),
  CONSTRAINT fk_avaliação_aluno1
    FOREIGN KEY (aluno_matricula)
    REFERENCES aluno (matricula));

CREATE TABLE responsavel (
  pessoa_cpf VARCHAR(11) NOT NULL,
  PRIMARY KEY (pessoa_cpf),
  CONSTRAINT fk_responsavel_pessoa1
    FOREIGN KEY (pessoa_cpf)
    REFERENCES pessoa (cpf));

CREATE TABLE avisos (
  id INT NOT NULL,
  data DATE NOT NULL,
  professor_matricula VARCHAR(8) NOT NULL,
  responsavel_pessoa_cpf VARCHAR(11) NOT NULL,
  conteudo VARCHAR(300) NOT NULL,
  PRIMARY KEY (id, professor_matricula, responsavel_pessoa_cpf),
  INDEX fk_avisos_professor1_idx (professor_matricula ASC) VISIBLE,
  INDEX fk_avisos_responsavel1_idx (responsavel_pessoa_cpf ASC) VISIBLE,
  CONSTRAINT fk_avisos_professor1
    FOREIGN KEY (professor_matricula)
    REFERENCES professor (matricula),
  CONSTRAINT fk_avisos_responsavel1
    FOREIGN KEY (responsavel_pessoa_cpf)
    REFERENCES responsavel (pessoa_cpf));

CREATE TABLE nota_final (
  valor INT NOT NULL,
  turma_id INT NOT NULL,
  aluno_matricula VARCHAR(8) NOT NULL,
  PRIMARY KEY (turma_id, aluno_matricula),
  INDEX fk_nota_final_aluno1_idx (aluno_matricula ASC) VISIBLE,
  CONSTRAINT fk_nota_final_turma1
    FOREIGN KEY (turma_id)
    REFERENCES turma (id),
  CONSTRAINT fk_nota_final_aluno1
    FOREIGN KEY (aluno_matricula)
    REFERENCES aluno (matricula));

CREATE TABLE professor_disciplina (
  professor_matricula VARCHAR(8) NOT NULL,
  disciplina_id INT NOT NULL,
  PRIMARY KEY (professor_matricula, disciplina_id),
  INDEX fk_professor_has_disciplina_disciplina1_idx (disciplina_id ASC) VISIBLE,
  INDEX fk_professor_has_disciplina_professor_idx (professor_matricula ASC) VISIBLE,
  CONSTRAINT fk_professor_has_disciplina_professor
    FOREIGN KEY (professor_matricula)
    REFERENCES professor (matricula),
  CONSTRAINT fk_professor_has_disciplina_disciplina1
    FOREIGN KEY (disciplina_id)
    REFERENCES disciplina (id));

CREATE TABLE aluno_turma (
  aluno_matricula VARCHAR(8) NOT NULL,
  turma_id INT NOT NULL,
  PRIMARY KEY (aluno_matricula, turma_id),
  INDEX fk_aluno_has_turma_turma1_idx (turma_id ASC) VISIBLE,
  INDEX fk_aluno_has_turma_aluno1_idx (aluno_matricula ASC) VISIBLE,
  CONSTRAINT fk_aluno_has_turma_aluno1
    FOREIGN KEY (aluno_matricula)
    REFERENCES aluno (matricula),
  CONSTRAINT fk_aluno_has_turma_turma1
    FOREIGN KEY (turma_id)
    REFERENCES turma (id));

CREATE TABLE aluno_responsavel (
  aluno_matricula VARCHAR(8) NOT NULL,
  responsavel_pessoa_cpf VARCHAR(11) NOT NULL,
  PRIMARY KEY (aluno_matricula, responsavel_pessoa_cpf),
  INDEX fk_aluno_has_responsavel_responsavel1_idx (responsavel_pessoa_cpf ASC) VISIBLE,
  INDEX fk_aluno_has_responsavel_aluno1_idx (aluno_matricula ASC) VISIBLE,
  CONSTRAINT fk_aluno_has_responsavel_aluno1
    FOREIGN KEY (aluno_matricula)
    REFERENCES aluno (matricula),
  CONSTRAINT fk_aluno_has_responsavel_responsavel1
    FOREIGN KEY (responsavel_pessoa_cpf)
    REFERENCES responsavel (pessoa_cpf));