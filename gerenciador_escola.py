import MySQLdb
import datetime
import names
import random
import ast
import os


# CRIAR UMA FUNÇÃO QUE GERENCIA CADA ELEMENTO DO CRUD:
# CREATE: criar listas de valores de atributos para gerar registros aleatórios.

# Conexão com o bd:
escoladb = MySQLdb.connect(
    host="localhost", user="root", passwd="bd2020", db="escoladb")

# Criando cursor:
cursor = escoladb.cursor()


# def gera_atributo(atributo):
#     nome = eval(atributo)
#     print(nome[random.randint(0,len(nome)-1)])
# gera_atributo("serie")

#   Gerados de campos:

def gserie():
    serie = ["1ª", "2ª", "3ª", "4ª", "5ª", "6ª", "7ª", "8ª", "9ª"]
    return serie[random.randint(0, len(serie)-1)]


def gperiodo():
    periodo = ["matutino", "vespertino"]
    return periodo[random.randint(0, len(periodo)-1)]


def gcpf():
    cpf = ""
    i = 0
    while i <= 10:
        cpf += str(random.randint(0, 9))
        i += 1
    return cpf


def gnome():
    return names.get_full_name()


def gtel():
    ddd = "("+str(random.randint(0, 9))+str(random.randint(0, 9))+")"
    tel = ""
    i = 0
    while i <= 8:
        tel += str(random.randint(0, 9))
        i += 1
    return ddd+tel


def gend():
    num = "Número " + str(random.randint(0, 9)) + ", "
    rua = "Rua " + names.get_last_name() + ", "
    bairro = "Bairro " + names.get_last_name() + ", "
    cidade = "Brasilia" + ", "
    uf = "DF"
    return num + rua + bairro + cidade + uf


def gdata():
    ano = random.randint(1950, 2010)
    mes = random.randint(1, 12)
    dia = random.randint(1, 31) if mes != "02" else random.randint(1, 28)
    return datetime.date(ano, mes, dia)


def gcivil():
    civil = ["solteiro(a)", "casado(a)"]
    return civil[random.randint(0, 1)]


def gmatri():
    matricula = ""
    i = 0
    while i <= 7:
        matricula += str(random.randint(0, 9))
        i += 1
    return matricula


def gdis():
    dis = ["Matemática", "Português", "Historia", "Geografia",
           "Sociologia", "Filosofia", "Inglês", "Espanhol"]
    return dis[random.randint(0, 7)]


def gforma():
    forma = ["Mestrado em Matemática", "Doutorado em Letras",
             "Mestrado em História", "Bacharelado em Geografia", "Phd em Filosofia"]
    return forma[random.randint(0, 4)]


def gid():
    return random.randint(0, 999)


def gplano():
    return str(random.randint(1, 3)) + " provas e " + str(random.randint(1, 3)) + " trabalhos"


def gcarga():
    return datetime.timedelta(hours=random.randint(80, 120)).total_seconds()/3600


def gnome_cargo():
    cargo = ["Reitor", "Diretor", "Chefe de departamento",
             "Supervisor de disciplina", "Dono", "Gerente de filial"]
    return cargo[random.randint(0, 4)]


def gfuncao():
    func = ["Fingir que trabalha", "Só enrola", "Trabalha o minimo",
            "Não fazer nada mesmo", "Só recebe em conta"]
    return func[random.randint(0, 4)]


def gnota():
    return round(random.uniform(0.0, 10.0), 2)


def gava():
    ava = ["Prova", "Trabalho"]
    return ava[random.randint(0, 1)]


def gaviso():
    aviso = ["O aluno está correndo risco de reprovação", "O aluno não está frequentando as aulas",
             "O aluno se comportou de forma inadeguada", "O aluno perdeu uma avaliação"]
    return aviso[random.randint(0, 3)]

# Geradores de registros:


def gera_pessoa():
    tupla = (gcpf(), gnome(), gtel(), gend(), gdata(), gcivil())
    return tupla


def gera_aluno():
    # pegando pessoa ja existente para associar:
    cursor.execute("SELECT * from pessoa")
    resultado = cursor.fetchall()
    return (gserie(), gperiodo(), gmatri(), resultado[random.randint(0, len(resultado)-1)][0])


def gera_prof():
    cursor.execute("SELECT * from pessoa")
    resultado = cursor.fetchall()
    return (gmatri(), gforma(), resultado[random.randint(0, len(resultado)-1)][0])


def gera_dis():
    return (gid(), gplano(), gdis(), gcarga())


def gera_turma():
    cursor.execute("SELECT * from disciplina")
    resultado = cursor.fetchall()
    return (gid(), gperiodo(), resultado[random.randint(0, len(resultado)-1)][0])


def gera_cargo():
    cursor.execute("SELECT * from pessoa")
    resultado = cursor.fetchall()
    return (gid(), gnome_cargo(), gfuncao(), resultado[random.randint(0, len(resultado)-1)][0])


# ####################"INTERFACE" DE USUÁRIO############################:

# Interfaces de inserção(C)
def menu_inserir():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecione o registro que deseja inserir:\n")
    print("1 - Professor               2 - Aluno                     3 - Responsável \n")
    print("4 - Disciplina              5 - Turma                     6 - Avaliação\n")
    op = input("7 - Nota final              8 - Cargo\n")
    inserir(op)

def pega_pessoa():
    print("Digite os dados pessoais\n")
    cpf = input("Digite o CPF:")
    nome = input("Digite o nome:")
    telefone = input("Digite o telefone com DDD:")
    endereco = input("Digite o endereço:")
    nascimento = datetime.datetime.strptime(input("Digite a data de nascimento(dd/mm/aaaa):"), '%d/%m/%Y')
    nascimento = nascimento.date()
    estado_civil = input("Digite o estado civil:")
    sql = "INSERT INTO pessoa VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (cpf, nome, telefone, endereco, nascimento, estado_civil))

    return cpf

def pega_prof(cpf):
    matricula = gmatri()
    print("Matricula gerada: ",matricula,"\n")
    formacao = input("Digite a formação:\n")
    pessoa_cpf = cpf
    sql = "INSERT INTO professor VALUES (%s, %s, %s)"
    cursor.execute(sql, (matricula, formacao, pessoa_cpf))

def pega_aluno(cpf):
    matricula = gmatri()
    print("Matricula gerada: ",matricula,"\n")
    serie = input("Digite a serie:\n")
    periodo = input("Digite o periodo(Matutino ou Vespertino):\n")
    pessoa_cpf = cpf
    sql = "INSERT INTO aluno VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (serie, periodo, matricula, pessoa_cpf))

def pega_resp(cpf):
    pessoa_cpf = cpf
    sql = "INSERT INTO responsavel VALUES (%s)"
    cursor.execute(sql, (pessoa_cpf))

def pega_disciplina():
    id_dis = gid()
    print("ID gerado: ", id_dis)
    plano = input("Plano de ensino:\n")
    nome = input("Nome:\n")
    carga = input("Carga horária:\n")
    carga = datetime.timedelta(hours=int(carga)).total_seconds()/3600
    sql = "INSERT INTO disciplina VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, (id_dis,plano,nome,carga))
    return id_dis

def pega_turma(id_dis):
    id_tur = gid()
    print("ID gerado: ", id_tur)
    turno = input("Digite o periodo da turma(Matutino ou Vespertino):\n")
    disciplina_id = id_dis
    sql = "INSERT INTO turma VALUES (%s,%s,%s)"
    cursor.execute(sql, (id_tur,turno,disciplina_id))

def pega_ava():
    id_tur = input("Digite o ID da turma:\n")
    matri_alu = input("Digite a matricula do aluno:\n")
    tipo = input("Tipo de avaliação(Trabalho, Prova, Teste e etc)\n")
    data =  datetime.datetime.strptime(input("Digite a data da avaliação(dd/mm/aaaa):"), '%d/%m/%Y')
    data = data.date()
    valor = input("Digite o valor obtido:\n")
    sql = "INSERT INTO avaliacao VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, (tipo,valor,data,id_tur,matri_alu))

def pega_nota_final():
    turma = input("Digite o ID da turma:\n")
    aluno = input("Digite o ID do aluno:\n")
    valor = input("Digite o valor da nota final:\n")
    sql = "INSERT INTO avaliacao VALUES (%s,%s,%s)"
    cursor.execute(sql, (valor,turma,aluno))

def pega_cargo():
    id_cargo = gid()
    nome = input("Digite o nome do cargo:\n")
    funcao = input("Descreva a função do cargo:\n")
    print("Digite o CPF caso o cargo esteja ocupado, caso contrário prossiga com enter:\n")
    p = input()
    if p != '':
        sql = "INSERT INTO avaliacao VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (id_cargo,nome,funcao,p))
    else:
        sql = "INSERT INTO avaliacao (id, nome, funcao) VALUES (%s,%s,%s)"
        cursor.execute(sql, (id_cargo,nome,funcao))    

def inserir(op):

    if op == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        pega_prof(pega_pessoa())
        escoladb.commit()
        print("Professor registrado!")
        input(" ")
        menu_inserir()
    if op == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        pega_aluno(pega_pessoa())
        escoladb.commit()
        print("Aluno registrado!")
        input(" ")
        menu_inserir()
    if op == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        pega_resp(pega_pessoa())
        escoladb.commit()
        print("Responsável registrado!")
        input(" ")
        menu_inserir()
    if op == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        pega_disciplina()
        escoladb.commit()
        print("Disciplina registrada!")
        input(" ")
        menu_inserir()
    if op == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        r = input("Deseja registrar disciplina primeiro?(s/n)\n")
        if r == "s":
            pega_turma(pega_disciplina())
        else:
            id_dis = input("Digite o id da disciplina existente:\n")
            pega_turma(id_dis)

        escoladb.commit()
        print("Turma registrada!")
        input(" ")
        menu_inserir()
    if op == "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        pega_ava()
        escoladb.commit()
        print("Avaliacao registrada!")
        input(" ")
        menu_inserir()
    if op == "7":
        os.system('cls' if os.name == 'nt' else 'clear')
        pega_nota_final()
        escoladb.commit()
        print("Nota final registrada!")
        input(" ")
        menu_inserir()
    if op == "8":
        os.system('cls' if os.name == 'nt' else 'clear')
        pega_cargo()
        escoladb.commit()
        print("Cargo registrado!")
        input(" ")
        menu_inserir()

menu_inserir()

# Interface de leitura (R):

def menu_leitura():
    print("Selecione o que deseja consultar:\n)
    


# Criação de tabela
# cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Create
# cursor.execute("INSERT INTO agente VALUES (97, '20:20:10','2019-05-10','Fernando')")
# escoladb.commit()

# Read
# cursor.execute("SELECT * from pessoa")
# resultado = cursor.fetchall()
# for registro in resultado:
# print("ID:", registro[0], "Tempo de serviço:", str(registro[1]), "Data do contrato:", str(registro[2]), "Nome:", registro[3])
# print(registro)

# Update
# cursor.execute("UPDATE agente set nome = 'Mauricio Santos' WHERE matricula = 84")
# escoladb.commit()

# Delete
# cursor.execute("DELETE FROM agente WHERE matricula = 86")
# escoladb.commit()
