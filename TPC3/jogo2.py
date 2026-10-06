import random

def iniciar():
    print("Modo 1: O computador joga primeiro ")
    print("Modo 2: O utilizador joga primeiro")

    modo = 0
    while modo != 1 and modo != 2:
        try:
            modo = int(input("Introduza 1 ou 2 para escolher o modo de jogo: "))
            if modo != 1 and modo != 2:
                print("Não existe esse modo de jogo, tente outra vez")
        except ValueError:
            print("Tens de escrever um número, tenta outra vez")

    if modo == 1:
        computador()
    elif modo == 2:
        utilizador()

def computador():
    print("O computador joga primeiro")
    total = 1
    print(f"O computador somou 1. Total: {total}")

    while total < 100:
        n = 0
        while n < 1 or n > 10:
            try:
                n = int(input("A tua jogada de 1 a 10: "))
                if n < 1 or n > 10:
                    print("Tem de ser entre 1 e 10")
            except ValueError:
                print("Tens de escrever um número")

        total = total + n
        print(f"Total: {total}")

        jogada = 11 - n
        total = total + jogada
        print(f"O computador somou", {jogada}, "Total:", {total})

    print("O computador venceu!")

def utilizador():
    print("O utilizador joga primeiro")
    total = 0

    while total < 100:
        # jogada do utilizador
        n = 0
        maximo = min(10, 100 - total)
        while n < 1 or n > maximo:
            try:
                n = int(input(f"A tua jogada de 1 a {maximo}: "))
                if n < 1 or n > maximo:
                    print(f"Tem de ser entre 1 e {maximo}")
            except ValueError:
                print("Tens de escrever um número")

        total = total + n
        print(f"Total: {total}")

        if total == 100:
            print("Venceste!")
            break

        # jogada do computador
        jogada = (1 - total) % 11
        if jogada == 0:
            jogada = random.randint(1, min(10, 100 - total))

        total = total + jogada
        print(f"O computador somou {jogada}. Total: {total}")

        if total == 100:
            print("O computador venceu!")
    
iniciar()