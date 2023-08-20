import random

def jogar():
    print("*******************************")
    print("Bem Vindo ao jogo de advinhação")
    print("*******************************")

    numero_secreto = round(random.randrange(0,101)) # random.random in range basicamente, função para gerar um numero aleatorio dentro do intervalo selecionado
    total_de_tentativas = 0
    pontos = 1000

    #print(numero_secreto)      # para sempre ver o numero que o ramdom escolheu

    print("Qual nivel de dificuldade? Digite o número escolhido.")
    print("1-Fácil?  2-Médio  3-Dífícil")

    nivel = int(input("Defina um nível: "))   # sem int() Devolve String

    if nivel == 1:
        total_de_tentativas = 15
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5        

    for rodada in range(1, total_de_tentativas + 1): # +1 é por causa do range (1,3), só vai até o 2
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Digite um número entre 1 e 100: "))    # o input smepre retorna string entao temos que converter para int
        print("Você digitou: ",chute )
        
        if chute not in range(0,101):
            print("Tem que ser um número de 1 até 100")
            continue # continua novamente o laço, desde o começo

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Parabéns voce acertou e fez {pontos} pontos!") 
            break
        else:
            if(maior):
                print("Você errou. O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou, seu número foi menor que o numero secreto.") 
            pontos_perdidos = abs(numero_secreto - chute)  # EX: 40 - 20 = 20 pontos perdidos, sem numeros negativos
            pontos = pontos - pontos_perdidos  # pontuação do jogo, conforme erra vai perdendo pontos 
                # abs = função que tranforma os numeros em absolutos, positivos 
    print("Fim do Jogo!")



