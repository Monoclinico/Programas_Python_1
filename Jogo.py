#importa bibliotecas
from random import randint
from time import sleep

#escolhe um número aleatório de 1 a 10
print('JOGO DA ADIVINHAÇÃO 1.0')
print('Escolhendo um número de 1 a 100...', end='')

#define as variáveis
numero = randint(1, 100)
escolha = 0

tentativas = 0
pontos = 101

#mostra os acertos e erros
while True:
    escolha = -1

    #repete a pergunta
    while 1 > escolha or escolha > 100:
        escolha = input('\nQual seu palpite de 1 a 100: ')
        if escolha == '' or escolha.isnumeric() != True:
            escolha = -1
        else:
            escolha = int(escolha)
    if escolha == numero:
        print('Você acertou!')
        break
    else:
        if (escolha > numero):
          print('Voce errou, o numero e menor')
        else:
          print('Voce errou, o numero e maior')

    tentativas += 1

#define a pontuação
pontos -= tentativas
print('{} tentativas.\n{} pontos.'.format(tentativas, pontos))
