#importa bibliotecas
from random import randint


#escolhe um número aleatório de 1 a 10
while True:
  print('='*50)
  print('JOGO DA ADIVINHAÇÃO 2.0')
  print('Acerte o numero que o computador escolher')
  print('Escolha o tamanho do grupo de numeros para jogar:')
  print('[1]facil: 1 ate 10')
  print('[2]medio: 1 ate 100')
  print('[3]dificil: 1 ate 1000')


  while True:
    try:
      limite = int(input('Qual sua escolha?'))
      if (limite in [10,100,1000]):
      
        break
      else:
        continue
    except:
      continue

  #define as variáveis

  numero = randint(1, limite)
  escolha = 0

  tentativas = 0
  pontos = limite

  #mostra os acertos e erros
  while True:
      escolha = -1

      #repete a pergunta
      while 1 > escolha or escolha > limite:
          escolha = input('\nQual seu palpite de 1 a {0}: '.format(limite))
          if escolha == '' or escolha.isnumeric() != True:
              escolha = -1
          else:
              escolha = int(escolha)
      if tentativas == pontos-1:
        tentativas +=1
        break
      if escolha == numero:
          print('Você acertou!')
          if (tentativas > 0):
            tentativas += 1
          break
      else:
          if (escolha > numero):
            print('Voce errou, o numero e menor')
          else:
            print('Voce errou, o numero e maior')
      tentativas += 1


  #define a pontuação
  pontos = (1 - ((tentativas) / pontos ))*100

  print('Tentativas: {}.\nPontuação: {:.2f}%.'.format(tentativas, pontos))
  jogar_de_novo = str(input('Deseja jogar novamente[S/N]?')).strip().upper()
  
  if (jogar_de_novo == 'S'):
    continue
  else:
    break
  
  
  
  
