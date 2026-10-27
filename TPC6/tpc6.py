def menu():
    print("Menu de operações:")
    print("1: Média das temperaturas")
    print("2: Guardar tabela meteriológica")
    print("3: Carregar tabela meteriológica")
    print("4: Temp mínima mais baixa")
    print("5: Amplitude térmica")
    print("6: Dia com maior precipitação")
    print("7: Dias com prec superior a um limite")
    print("8: Maior período de calor")
    print("9: Gráficos da temp mínima, máxima e de pluviosidade.")
    print("0: Sair da aplicação")

def medias(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        media = (tmin + tmax) / 2
        res.append((data, media))
    return res

def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")  
    for data, tmin, tmax, prec in t:
        ano, mes, dia = data
        file.write(f"{ano}-{mes}-{dia}| {tmin} |{tmax}| {prec} |\n")
    file.close()
    return

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r") 
    for line in file:
        data, tmin, tmax, prec, _ = line.split("|")
        ano, mes, dia = data.split("-")
        tuplo = ((ano, mes, dia), tmin, tmax, prec[:-1])
        res.append(tuplo)
    file.close()
    return res

def minMin(tabMeteo):
    i = 1
    minima = tabMeteo[0][1]
    if tabMeteo[i][1] < minima:
        minima = tabMeteo[i][1]
        i = i + 1
    return minima

def amplTerm(tabMeteo):
    res = []
    for previsao in tabMeteo:
        data, min, max, prec = previsao
        amplitude = max - min
        res.append((data, amplitude))
    return res

def maxChuva(tabMeteo):
    maxima = tabMeteo[0][3]
    i = 1
    if tabMeteo[i][3] > maxima:
        maxima = tabMeteo[i][3]
        data_max = tabMeteo[i][0]
        i = i + 1
    return(data_max, maxima)

def diasChuvosos(tabMeteo, p):
    prec_superior = []
    for data, tmax, tmin, prec in tabMeteo:
        if prec > p:
            prec_superior.append((data,prec))
    return prec_superior

def maxPeriodoCalor(tabMeteo, p):
    max_consecutivos = 0
    consecutivos_atual = 0
    for previsao in tabMeteo:
        prec = previsao[3]
        if prec < p:
            consecutivos_atual = consecutivos_atual + 1
            max_consecutivos = consecutivos_atual 
        consecutivos_atual = 0

    if consecutivos_atual > max_consecutivos:
        max_consecutivos = consecutivos_atual
    return max_consecutivos

from matplotlib import pyplot as plt #biblioteca

def grafTabMeteo(t):
    #y_min = [elem[1] for elem in t]
    y_min = [tmin for data, tmin, tmax, prec in t]
    y_max = [tmax for data, tmin, tmax, prec in t]
    y_prec = [prec for data, tmin, tmax, prec in t]

    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]

    plt.plot(x,y_min, color="green", marker = "o", label = "Tmin ºC")
    plt.plot(x,y_max, color="red", marker = "o", label = "Tmax ºC")
    plt.title("Temperatura mínima")
    plt.legend()
    plt.grid()
    plt.show()

    plt.bar(x,y_max, color = "green", label = "Precipitação(mm)")
    plt.title("Precipitação")
    plt.show()
    return
    


def op():
    tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]
    print(f"Tabela meteriológica:{tabMeteo1}")
    opcao = -1
    while opcao != 0:
            menu()
            opcao = int(input("Escolha uma opção para a operação que pretende efetuar: "))
    
            if opcao == 0:
                print("\nA terminar a aplicação. Até à próxima!")
            elif opcao == 1:
                print(medias(tabMeteo1))
            elif opcao == 2:
                print(guardaTabMeteo(tabMeteo1, "meteriologia.txt"))
            elif opcao == 3:
                print(carregaTabMeteo("meteriologia.txt"))
            elif opcao == 4:
                print(minMin(tabMeteo1))
            elif opcao == 5:
                print(amplTerm(tabMeteo1))
            elif opcao == 6:
               print(maxChuva(tabMeteo1))
            elif opcao == 7:
                print(diasChuvosos(tabMeteo1, 0))
            elif opcao == 8:
                print(maxPeriodoCalor(tabMeteo1, 0.6))
            elif opcao ==9:
                print(grafTabMeteo(tabMeteo1))
            else:
                print("Opção inválida! Tente novamente.")

op()
