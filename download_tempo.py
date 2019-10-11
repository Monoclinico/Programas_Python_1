#-*- coding:utf-8 -*-

def leitura():
  while True:
    try:
      print(('Qual o tamanho do arquivo(MB)?'))
      tamanho = float(input('->'))
      print('Qual a velocidade da internet(Mbps)')
      velocidade = float(input('->'))
    except:continue
    else:break
  tempo = (tamanho*8.0) / velocidade
  minutos = tempo // 60
  segundos_restantes = tempo % 60
  print(f'Tempo: {minutos:n}min e {segundos_restantes:.3f}s')

leitura()