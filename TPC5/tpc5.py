def menu():
    print("Menu de operações:")
    print("1: Criar uma turma")
    print("2: Inserir um aluno na turma")
    print("3: Listar a turma")
    print("4: Consultar um aluno por id")
    print("5: Guardar a turma em arquivo")
    print("6: Carregar uma turma dum arquivo")
    print("0: Sair da aplicação")

def criarturma():
    turma = []
    nomedaturma = input("Introduza o nome da turma: ")
    print(f"A turma {nomedaturma} foi criada")
    return turma 

def inseriraluno(turma):
    nomedoaluno = input("Insira o nome do aluno: ")
    id_aluno = input("Insira o id do aluno: ")

    while ver_id(id_aluno, turma):
        id_aluno = input("Já há um aluno com este id. Tente outra vez: ")

    notaTPC = vernota("Inserir nota do TPC: ")
    notaPROJ = vernota("Inserir nota do projeto: ")
    notaTESTE = vernota("Inserir nota do teste: ")

    aluno = (nomedoaluno, id_aluno, [notaTPC, notaPROJ, notaTESTE])
    turma.append(aluno)
    print(f"O aluno {aluno} foi inserido")
    return turma


def ver_id(id_aluno, turma):
    rep = False
    for aluno in turma:
        if aluno[1] == id_aluno:
            rep = True
    return rep

def vernota(texto):
    nota = float(input(texto))
    while nota < 0 or nota > 20:
        nota = float(input("Introduza uma nota de 0 a 20: "))
    return nota

def listarTurma(turma):
    if turma == []:
        print("Insira alunos na turma primeiro: ")
        op()
    else:
        for aluno in turma:
            print(f"Nome: {aluno[0]} \nId: {aluno[1]} \nNota do TPC: {aluno[2][0]} \nNota do Projeto: {aluno[2][1]} \nNota do Teste: {aluno[2][2]}\n")

def consultarAluno(turma):
    édaturma = False
    consultarid = input("Introduza o id do aluno")
    for aluno in turma:
        if aluno[1] == consultarid:
            print(f"O aluno tem: id {consultarid}: \nNome: {aluno[0]} \nNota do TPC: {aluno[2][0]} \nNota do Projeto: {aluno[2][1]} \nNota do Teste: {aluno[2][2]}")
            édaturma = True
    if édaturma == False:
        print("O id não corresponde a nenhum aluno")

def guardarturma(turma):
    nomefile = input("Indica o nome do ficheiro: ")
    file = open(f"{nomefile}.txt", "w")
    for aluno in turma:
        file.write(f"{aluno[0]}|{aluno[1]}|{aluno[2][0]}|{aluno[2][1]}|{aluno[2][2]}\n")
    file.close()
    print(f"A turma foi guardada no ficheiro {nomefile}")

def carregarturma():
    nomefile = input("Indica o nome do ficheiro a abrir: ")
    turma = []
    file = open(f"{nomefile}.txt", "r")
    for line in file:
        dados = line.split ("|")
        nome = dados [0]
        id = dados [1]
        notas = [float(dados [2]), float(dados [3]), float(dados[4])]
        aluno = (nome, id, notas) 
        turma.append (aluno)
    file.close()
    return turma

def op():
    turma = []
    opcao = -1
    while opcao != 0:
            menu()
            opcao = int(input("Escolha uma opção para a operação que pretende efetuar: "))
    
            if opcao == 0:
                print("\nA terminar a aplicação. Até à próxima!")
            elif opcao == 1:
                criarturma()
            elif opcao == 2:
                inseriraluno(turma)
            elif opcao == 3:
                listarTurma(turma)
            elif opcao == 4:
                consultarAluno(turma)
            elif opcao == 5:
                guardarturma (turma)
            elif opcao == 6:
                carregarturma()
                print(turma)
            else:
                print("Opção inválida! Tente novamente.")

op()
