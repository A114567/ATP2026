import random

def menu():
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")

def variavel_interna():
    lista = []
    opçao = -1

    while opçao != 0:
        menu()
        opçao = int(input("Introduza uma das opçoes"))

        if opçao == 0:
            print("Escolheu a opção sair, até à próxima!")
        elif opçao == 1:
            lista = criar_lista()
            print("A lista foi criada com sucesso", lista)
        elif opçao == 2:
            lista = ler_lista()
            print("A lista que criou foi: ", lista)
        elif opçao == 3:
            print("A soma da lista", lista, "é", soma(lista))
        elif opçao == 4:
            print("A média da lista", lista, "é", media(lista))
        elif opçao == 5:
            print("O maior elemento da lista", lista, "é", maior(lista))
        elif opçao == 6:
            print("O menor elemento da lista", lista, "é", menor(lista))
        elif opçao == 7:
            if esta_crescente(lista):
                print("Está por ordem crescente")
            else:
                print("Não está por ordem crescente")
        elif opçao == 8:
            if esta_decrescente(lista):
                print("Está por ordem decrescente")
            else:
                print("Não está por ordem decrescente")
        elif opçao == 9:
            valor = int(input("Elemento a procurar: "))
            print("Posição:", procurar(lista, valor))
        else:
            print("Valor inválido")


def criar_lista():
    num_elem = int(input("Quantos elementos irá ter a sua lista?"))
    lista = []
    for i in range(num_elem):
        lista.append(random.randint(1,100))
    return lista

def ler_lista():
    lista = []
    contador = 0
    n = int(input("Introduza o número de elementos que quer na sua lista:"))
    while n > contador:
        x = int(input("Introduza um número para a lista"))
        lista.append(x)
        contador = contador + 1
    return lista

def soma(lista):
    soma = 0
    for n in lista:
        soma = n + soma
    return soma

def media(lista):
    media = soma(lista) / len(lista)
    return media

def maior(lista):
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    return maior

def menor(lista):
    menor = lista[0]
    for n in lista:
        if n < menor:
            menor = n
    return menor

def esta_crescente(lista):
    for n in range(len(lista) - 1):
        if lista[n] > lista[n + 1]:
            return False
    return True

def esta_decrescente(lista):
    for n in range(len(lista) - 1):
        if lista[n] < lista[n + 1]:
            return False
    return True

def procurar(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

variavel_interna()