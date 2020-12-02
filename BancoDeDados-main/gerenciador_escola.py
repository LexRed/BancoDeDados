import MySQLdb
import datetime
import names
import random
import ast
import os
import sys

# Conexão com o bd:
escoladb = MySQLdb.connect(host="localhost", user="root", passwd="bd2020", db="escoladb")

# Criando cursor:
cursor = escoladb.cursor()

tabelas = {"1": "professor","2":"aluno","3":"responsavel","4":"disciplina","5":"turma","6":"avaliacao","7":"nota_final","8":"cargo","9":"pessoa"}
campos = {"1": ["matricula","formacao","pessoa_cpf"],
        "2": ["serie","periodo","matricula","pessoa_cpf"],
        "3": ["pessoa_cpf"],
        "4": ["id","plano_ensino","nome","carga_horaria"],
        "5": ["id","turno","disciplina_id"],
        "6": ["tipo","valor","data","turma_id","aluno_matricula"],
        "7": ["valor","turma_id","aluno_matricula"],
        "8": ["id","nome","funcao","pessoa_cpf"],
        "9": ["cpf","nome","telefone","endereco","nascimento","estado_civil"]
}

#################################### Geradores de campos: ############################################

def gserie():
    serie = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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
    # random.seed(random.randint(0, 9999))
    return random.randint(0, 999)


def gplano():
    return str(random.randint(1, 3)) + " provas e " + str(random.randint(1, 3)) + " trabalhos"


def gcarga():
    # return datetime.timedelta(hours=random.randint(80, 120)).total_seconds()/3600
    return datetime.timedelta(hours=random.randint(80, 120))


def gnome_cargo():
    cargo = ["Reitor", "Diretor", "Chefe de departamento",
             "Supervisor de disciplina", "Dono", "Gerente de filial"]
    return cargo[random.randint(0, 4)]


def gfuncao():
    func = ["Fingir que trabalha", "Só enrola", "Trabalha o minimo",
            "Não fazer nada mesmo", "Só recebe em conta"]
    return func[random.randint(0, 4)]


def gnota():
    return round(random.uniform(0.0, 10.0), 1)


def gava():
    ava = ["Prova", "Trabalho"]
    return ava[random.randint(0, 1)]


def gaviso():
    aviso = ["O aluno está correndo risco de reprovação", "O aluno não está frequentando as aulas",
             "O aluno se comportou de forma inadeguada", "O aluno perdeu uma avaliação"]
    return aviso[random.randint(0, 3)]

########################## Geradores de registros: #############################################


def gera_pessoa():
    tupla = (gcpf(), gnome(), gtel(), gend(), gdata(), gcivil())
    return tupla


def gera_aluno(cpf):
    # pegando pessoa ja existente para associar:
    # cursor.execute("SELECT * from pessoa")
    # resultado = cursor.fetchall()
    return (gserie(), gperiodo(), gmatri(), cpf)


def gera_prof(cpf):
    # cursor.execute("SELECT * from pessoa")
    # resultado = cursor.fetchall()
    # resultado[random.randint(0, len(resultado)-1)][0]
    return (gmatri(), gforma(), cpf)

# def gera_resp(cpf):
    # return (cpf)


def gera_dis():
    return (gid(), gplano(), gdis(), gcarga())


def gera_turma(dis_id):
    # cursor.execute("SELECT * from disciplina")
    # resultado = cursor.fetchall()
    return (gid(), gperiodo(), dis_id)


def gera_cargo(cpf):
    # cursor.execute("SELECT * from pessoa")
    # resultado = cursor.fetchall():
    # return (gid(), gnome_cargo(), gfuncao(), resultado[random.randint(0, len(resultado)-1)][0])
    return (gid(), gnome_cargo(), gfuncao(),cpf)

# Função que gera professor(cria pessoa antes)
# def insere_prof(num):
#     i = 0
#     while i <= num:
#         sql = "INSERT INTO pessoa VALUES (%s, %s, %s, %s, %s, %s)"
#         pessoa = gera_pessoa()
#         cursor.execute(sql, pessoa)
#         escoladb.commit()
#         sql = "INSERT INTO professor VALUES (%s, %s, %s)"
#         cursor.execute(sql, gera_prof(pessoa[0]))
#         escoladb.commit()
#         i += 1

# Função que gera aluno
def insere_auto(tabela_num,num):
    tabela = tabelas[tabela_num]
    print(tabela)
    c = len(campos[tabela_num])
    print(c)
    values = " VALUES ("+"%s, "*(c-1)+"%s)"

    if tabela_num in ["1","2","3"]:
        val = ""
        if tabela_num == "1":
            val = "gera_prof(pessoa[0])"
        elif tabela_num == "2":
            val = "gera_aluno(pessoa[0])"
        else:
            val = "[pessoa[0]]"
        i = 0
        while i <= num:
            sql = "INSERT INTO pessoa VALUES (%s, %s, %s, %s, %s, %s)"
            pessoa = gera_pessoa()
            cursor.execute(sql, pessoa)
            escoladb.commit()
            print(values)
            print(eval(val))
            sql = "INSERT INTO "+tabela+values
            cursor.execute(sql, eval(val))
            escoladb.commit()
            i += 1
    elif tabela_num == "4":
        i = 0
        while i <= num:
            sql = "INSERT INTO "+tabela+values
            cursor.execute(sql, gera_dis())
            escoladb.commit()
            i += 1
    elif tabela_num == "5":
        i = 0
        while i <= num:
            sql = "INSERT INTO disciplina VALUES (%s, %s, %s, %s)"
            disciplina = gera_dis()
            cursor.execute(sql, disciplina)
            escoladb.commit()
            turma = gera_turma(disciplina[0])
            print(disciplina)
            print(turma)
            sql = "INSERT INTO "+tabela+values
            cursor.execute(sql, turma)
            escoladb.commit()
            i += 1
    elif tabela_num == "6":
        i = 0
        while i <= num:
            cursor.execute("SELECT * from turma")
            resultado = cursor.fetchall()
            id_turma = resultado[random.randint(0, len(resultado)-1)][0]
            print(id_turma)

            cursor.execute("SELECT * from aluno")
            resultado = cursor.fetchall()
            matri_aluno = resultado[random.randint(0, len(resultado)-1)][2]
            print(matri_aluno)
            print(values)

            sql = "INSERT INTO "+tabela+values
            print((gava(),gnota(),gdata(),id_turma,matri_aluno))
            cursor.execute(sql, (gava(),gnota(),gdata(),id_turma,matri_aluno))
            escoladb.commit()
            i += 1
    elif tabela_num == "7":
        i = 0
        while i <= num:
            cursor.execute("SELECT * from turma")
            resultado = cursor.fetchall()
            id_turma = resultado[random.randint(0, len(resultado)-1)][0]

            cursor.execute("SELECT * from aluno")
            resultado = cursor.fetchall()
            matri_aluno = resultado[random.randint(0, len(resultado)-1)][2]
            print(id_turma)
            print(matri_aluno)

            sql = "INSERT INTO "+tabela+values
            cursor.execute(sql, (gnota(),id_turma,matri_aluno))
            escoladb.commit()
            i += 1
    elif tabela_num == "8":
        i = 0
        while i <= num:
            cursor.execute("SELECT * from pessoa")
            resultado = cursor.fetchall()
            cpf = resultado[random.randint(0, len(resultado)-1)][0]

            sql = "INSERT INTO "+tabela+values
            cursor.execute(sql, gera_cargo(cpf))
            escoladb.commit()
            i += 1


# insere_auto("1",5)
# insere_auto("2",5)
# insere_auto("3",5)
# insere_auto("4",5)
# insere_auto("5",5)
# insere_auto("6",5)
# insere_auto("7",5)
# insere_auto("8",5)


#####################INTERFACE DE USUÁRIO############################:

# Interfaces de inserção(CREATE)
def menu_inserir():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecione o registro que deseja inserir:\n")
    print("1 - Professor               2 - Aluno                     3 - Responsável \n")
    print("4 - Disciplina              5 - Turma                     6 - Avaliação\n")
    print("7 - Nota final              8 - Cargo\n")
    op = input("0 - Retornar ao menu principal\n")
    if op == "0":
        menu_principal()
    else:
        inserir(op)

def pega_pessoa():
    print("Digite os dados pessoais\n")
    cpf = input("Digite o CPF:")
    nome = input("Digite o nome:")
    telefone = input("Digite o telefone com DDD:")
    endereco = input("Digite o endereço:")
    nascimento = datetime.datetime.strptime(
        input("Digite a data de nascimento(dd/mm/aaaa):"), '%d/%m/%Y')
    nascimento = nascimento.date()
    estado_civil = input("Digite o estado civil:")
    sql = "INSERT INTO pessoa VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (cpf, nome, telefone,
                         endereco, nascimento, estado_civil))
    return cpf

def pega_prof(cpf):
    matricula = gmatri()
    print("Matricula gerada: ", matricula, "\n")
    formacao = input("Digite a formação:\n")
    pessoa_cpf = cpf
    sql = "INSERT INTO professor VALUES (%s, %s, %s)"
    cursor.execute(sql, (matricula, formacao, pessoa_cpf))


def pega_aluno(cpf):
    matricula = gmatri()
    print("Matricula gerada: ", matricula, "\n")
    serie = input("Digite a serie:\n")
    periodo = input("Digite o periodo(Matutino ou Vespertino):\n")
    pessoa_cpf = cpf
    sql = "INSERT INTO aluno VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (serie, periodo, matricula, pessoa_cpf))


def pega_resp(cpf):
    pessoa_cpf = cpf
    sql = "INSERT INTO responsavel VALUES (%s)"
    cursor.execute(sql, [pessoa_cpf])


def pega_disciplina():
    id_dis = gid()
    print("ID gerado: ", id_dis)
    plano = input("Plano de ensino:\n")
    nome = input("Nome:\n")
    carga = input("Carga horária:\n")
    carga = datetime.timedelta(hours=int(carga)).total_seconds()/3600
    sql = "INSERT INTO disciplina VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, (id_dis, plano, nome, carga))
    return id_dis


def pega_turma(id_dis):
    id_tur = gid()
    print("ID gerado: ", id_tur)
    turno = input("Digite o periodo da turma(Matutino ou Vespertino):\n")
    disciplina_id = id_dis
    sql = "INSERT INTO turma VALUES (%s,%s,%s)"
    cursor.execute(sql, (id_tur, turno, disciplina_id))


def pega_ava():
    id_tur = input("Digite o ID da turma:\n")
    matri_alu = input("Digite a matricula do aluno:\n")
    tipo = input("Tipo de avaliação(Trabalho, Prova, Teste e etc)\n")
    data = datetime.datetime.strptime(
        input("Digite a data da avaliação(dd/mm/aaaa):"), '%d/%m/%Y')
    data = data.date()
    valor = input("Digite o valor obtido:\n")
    sql = "INSERT INTO avaliacao VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql, (tipo, valor, data, id_tur, matri_alu))


def pega_nota_final():
    turma = input("Digite o ID da turma:\n")
    aluno = input("Digite o ID do aluno:\n")
    valor = input("Digite o valor da nota final:\n")
    sql = "INSERT INTO nota_final VALUES (%s,%s,%s)"
    cursor.execute(sql, (valor, turma, aluno))


def pega_cargo():
    id_cargo = gid()
    nome = input("Digite o nome do cargo:\n")
    funcao = input("Descreva a função do cargo:\n")
    print("Digite o CPF caso o cargo esteja ocupado, caso contrário prossiga com enter:\n")
    p = input()
    if p != '':
        sql = "INSERT INTO cargo VALUES (%s,%s,%s,%s)"
        cursor.execute(sql, (id_cargo, nome, funcao, p))
    else:
        sql = "INSERT INTO cargo (id, nome, funcao) VALUES (%s,%s,%s)"
        cursor.execute(sql, (id_cargo, nome, funcao))


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

# Interface de leitura (R):
def menu_read():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecione o que deseja consultar:")
    print("1 - Professor               2 - Aluno                     3 - Responsável \n")
    print("4 - Disciplina              5 - Turma                     6 - Avaliação\n")
    print("7 - Nota final              8 - Cargo                     9 - Dados pessoais\n")
    op = input("0 - Retornar ao menu principal\n")
    if op == "0":
        menu_principal()
    else:
        read_tabela(op)

# Função para fazer READ:
def read_tabela(op):
    tabela = tabelas[op]
    os.system('cls' if os.name == 'nt' else 'clear')
    res = input("1 - Todos                     2 - Usar condição\n")
    resultado = ''
    if res=="2":
        fcam = input("Digite o campo que deseja usar como filtro da consulta:\n")
        fvcam = input("Digite o valor que será usado como filtro\n")
        cursor.execute("SELECT * FROM "+tabela+" WHERE "+fcam+" = "+fvcam)
        resultado = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM "+tabela)
        resultado = cursor.fetchall()
    mostra(op,resultado)
    menu_read()

# Interface para deletar (D):
def menu_del():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecione o que deseja deletar:")
    print("1 - Professor               2 - Aluno                     3 - Responsável \n")
    print("4 - Disciplina              5 - Turma                     6 - Avaliação\n")
    print("7 - Nota final              8 - Cargo                     9 - Dados pessoais\n")
    op = input("0 - Menu principal\n")
    if op == "0":
        menu_principal()
    else:
        del_tabela(op)

# Função para realizar DELETE
def del_tabela(op):
    tabela = tabelas[op]
    os.system('cls' if os.name == 'nt' else 'clear')
    fcam = input("Digite o campo que deseja usar como filtro da exclusão:\n")
    fvcam = input("Digite o valor que será usado como filtro\n")
    cursor.execute("DELETE FROM "+tabela+" WHERE "+fcam+" = "+fvcam)
    escoladb.commit()
    cursor.execute("SELECT * FROM "+tabela)
    resultado = cursor.fetchall()
    mostra(op,resultado)
    menu_del()

# Interface de atualização de dados (U):
def menu_up():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecione o que deseja alterar:")
    print("1 - Professor               2 - Aluno                     3 - Responsável \n")
    print("4 - Disciplina              5 - Turma                     6 - Avaliação\n")
    print("7 - Nota final              8 - Cargo                     9 - Dados pessoais\n")
    op = input("0 - Menu principal\n")
    if op == "0":
        menu_principal()
    else:
        up_tabela(op)

# Função para realizar UPDATE:
def up_tabela(op):
    tabela = tabelas[op]
    os.system('cls' if os.name == 'nt' else 'clear')
    campo = input("Digite o nome do campo que deseja alterar:\n")
    vcam = input("Digite o novo valor do campo:\n")
    fcam = input("Digite o campo que deseja usar como filtro da alteração:\n")
    fvcam = input("Digite o valor que será usado como filtro\n")
    # sql = "UPDATE "+tabela+" SET "+campo+" = "+vcam+" WHERE "+fcam+" = "+fvcam+";"
    sql = "UPDATE "+tabela+" SET "+campo+" = "+vcam+" WHERE "+fcam+" = "+fvcam
    # print(sql)
    cursor.execute(sql)
    escoladb.commit()
    cursor.execute("SELECT * FROM "+tabela+" WHERE "+campo+" = "+vcam)
    resultado = cursor.fetchall()
    mostra(op,resultado)
    menu_up()

# Apenas mostra o registros recebidos:
def mostra(op,resultado):

    #print("Os registros foram atualizados!\n")
    for registro in resultado:
        linha = '| '
        i = 0
        for r in registro:
            linha += campos[op][i]+": "+str(r)+" |"
            i += 1
        linha += "\n"
        print(linha)
    input(" ")
    
# Menu que gerencia acesso a outras areas do programa:
def menu_principal():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecione deseja fazer:\n")
    print("1 - Inserir registros               2 - Visualizar registros\n")
    print("3 - Atualizar registros             4 - Excluir registros\n")
    op = input("Enter para sair\n")
    funcoes = {"1": "menu_inserir()","2": "menu_read()","3": "menu_up()","4": "menu_del()","":"sys.exit()"}
    eval(funcoes[op])  

menu_principal()
