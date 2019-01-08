#coding:utf-8

tele = {}

while True:
  try:
    f = int(input( 58*'-' + '\nAdicionar[1]---Remover[2]---Ler[3]---Pesquisar[4]---Sair[5]: '))
  except:
    continue
  if f == 1:
    nome = str(input('Nome: ')).strip()
    numero = int(input('Número: '))
    if numero not in tele:
      tele[numero] = nome
    else:
      print('Número já existente no banco dados.')
      print(tele[numero],':',numero)
      continue
  elif f == 2:
    try:
      nume2 = int(input('Remover número ou tudo (-1): '))
    except:
      continue
    if nume2 != -1:
      if nume2 in tele:
        print(tele[nume2],':',nume2,'>> removido')
        del tele[nume2]
      else:
        print('Número não existente no banco dados.')
        continue
    else:
      tele.clear()
  elif f == 3:
    if len(tele) == 0:
      print('Banco de dados está vazio.')
    else:
      for o in tele:
        print(tele[o],':',o)
  elif f == 4:
    while True:
      try:
        pesq = int(input('Pesquisar por nome[1], número[2] ou sair[3]:'))
      except:
        continue
      if pesq == 1:
        nome_p = str(input('Nome desejado:')).strip()
        if len(tele) > 0:
          quant = 0
          for l in tele.keys():
            if nome_p == tele[l]:
              print(tele[l],':',l)
              quant = 1
          if quant == 0:
            print('Nada encontrado')
            continue
        else:
          print('Banco de dados está vazio.')
          continue
      elif pesq == 2:
        num_p = int(input('Número desejado:'))
        if len(tele) > 0:
          quant2 = 0
          for l in tele.keys():
            if num_p == l:
              print(tele[l],':',l)
              quant2 = 1
          if quant2 == 0:
            print('Nada encontrado')
            continue
      elif pesq == 3:
        break
  elif f == 5:
    print('BD encerrado!')
    break