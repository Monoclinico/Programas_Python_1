#-*- coding:utf-8 -*-

def leitura():
  while True:
    try:
      print(('Qual o tamanho do arquivo(MB)?'))
      t = float(input('->'))
      print('Qual a velocidade da internet(Mbps)')
      v = float(input('->'))
    except:continue
    else:break
  bytes_ps = v / 8
  tempo = t / bytes_ps
  seg = tempo % 60
  minu = (tempo - seg) // 60
  print(tempo)
  print(f'Tempo: {minu:n}min e {seg:.3f}s')

leitura()