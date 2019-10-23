#importa bibliotecas
from random import randint


#escolhe um número aleatório de 1 a 10
while True:
  print('='*50)
  print('JOGO DA ADIVINHACAO 3.1')
  print('Acerte o numero que o computador escolher')
  print('Escolha o tamanho do grupo de numeros para jogar:')
  print('[1]facil: 1 ate 10')
  print('[2]medio: 1 ate 100')
  print('[3]dificil: 1 ate 1000')
  print('[4]mais dificil: 1 ate 10000')
  print('[5]super dificil: 1 ate 100000')


  while True:
    try:
      limite = int(input('Qual sua escolha?'))
      if (limite in [1,2,3,4,5]):
        limite = 10 ** limite
        break
      else:
        continue
    except:
      continue

  #define as variáveis

  numero = randint(1, limite)
  escolha = 0
  ultima_escolha = set({})
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
        if(escolha not in ultima_escolha):
          dica_tipo = randint(1,4)
          if (dica_tipo == 1):
            if(numero %2 ==0):
              print('Dica: o numero e par')
            else:
              print('Dica: o numero e impar')
          elif (dica_tipo == 2):
            multiplo_aleatorio = randint(2,10)
            if (numero % multiplo_aleatorio == 0):
              print('Dica: o numero e multiplo de ',multiplo_aleatorio)
            else:
              print('Dica: o numero nao e multiplo de ',multiplo_aleatorio)
          elif (dica_tipo == 3):
            soma_numero = sum(list( [ float(c) for c in (str(numero))]))
            print('Dica: a soma dos digitos do numero e ', soma_numero)
          else:
            while True:
              escolha_aleatoria = randint(1,limite)
              if escolha_aleatoria != numero:
                break
              else:
                continue
            if (escolha_aleatoria > numero):
              print('Dica: e menor que ',escolha_aleatoria)
            else:
              print('Dica: e maior que ',escolha_aleatoria)
        else:
          print('Nao e', escolha, ', tente outro')

      ultima_escolha.add(escolha)
      tentativas += 1


  #define a pontuação
  pontos = (1 - ((tentativas) / pontos ))*100

  print('Tentativas: {}.\nPontuação: {:.2f}%.'.format(tentativas, pontos))

  jogar_de_novo = str(input('Deseja jogar novamente[S/N]?')).strip().upper()
  
  if (jogar_de_novo == 'S'):
    continue
  else:
    break
  
  
  
  
