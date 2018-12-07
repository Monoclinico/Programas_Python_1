#-*- coding: utf-8 -*-

"""
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
isto é, considere latas cheias.
"""

cobertura = (1,6) # (litros,metros²)
lata = (18,80)
galao = (3.6,25)

def litros_n(l,n,v):
  q = 0
  while q*l < n:
    q += 1 
  return (q,v*q)

def lata_e_galao(qu):
  q = [] #[(1)(2)]
  if qu // 18 > 0:
    resto = qu % 18
    if resto == 0:
      q.append(litros_n(18,qu,80))
      q.append((0,0))
    else:
      if resto <= 10.8:
        q.append(litros_n(18,(qu//18)*18,80))
        q.append(litros_n(3.6,resto,25))
      else:
        q.append(litros_n(18,qu,80))
        q.append((0,0))
  else:
    if qu <= 10.8:
      q.append((0,0))
      q.append(litros_n(3.6,qu,25))
    else:
      q.append(litros_n(18,qu,80))
      q.append((0,0))
  return q

def linhas(i=25):
  print('-=-'*int(i))

while True:
  try:
    linhas()
    area = float(input('Área a ser pintada (m²):'))
    litros = (area * cobertura[0]) / cobertura[1]
  except ValueError:
    continue
  else:
    break


q_galao = litros_n(galao[0],litros,galao[1])
q_lata = litros_n(lata[0],litros,lata[1])
q_g_l = lata_e_galao(litros)

linhas(15)
print('Quantidade de tinta necessária: '+format(litros,'.3f')+'L')
print('Se comprar só latas de 18L será necessário {} lata(s), dando R$ {:.2f}.'.format(*q_lata))
print('Se comprar só galões de 3,6L será necessário {} galão(galões), dando R$ {:.2f}.'.format(*q_galao))
print('Se comprar latas e galões será necessário {} lata(s) e {} galão(galões), dando R$ {}.'.format(q_g_l[0][0],q_g_l[1][0],q_g_l[0][1]+q_g_l[1][1]))

