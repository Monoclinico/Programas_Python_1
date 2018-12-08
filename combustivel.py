#-*- coding: utf-8 -*-
"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro 
    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível, codificado da seguinte forma: 
    A-álcool, G-gasolina. 
    Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 
    o preço do litro do álcool é R$ 1,90. 
"""
def escreva_preco(p):
  print('Preço total: R$ {:.2f}'.format(p))


def preco(ti,v):
  p = 0
  a = 1.90
  g = 2.50
  if ti == 'A':
    p = v * a
    if v > 20:
      p = p - (p * 0.05) 
    else:
      p = p - (p * 0.03) 
  else:
    p = v * g 
    if v > 20:
      p = p - (p * 0.06) 
    else:
      p = p - (p * 0.04) 
  return escreva_preco(p) 


def volume_e_tipo():
  while True:
    try:
      vol = float(input('Volume de combustível em litros: '))
      tipo = str(input('Tipo de combustível: gasolina(G) ou álcool(A): ')).strip().upper()
    except:
      continue
    else:
      if (vol >= 0) and (tipo in ['A','G']):
        break
      else:
        continue
  return preco(tipo,vol)     


def tabela_precos():
  print(format('Álcool','=^49'))
  print('|',format('até 20 litros','^18'),'|','3% de desconto por litro','|')
  print('|', format('acima de 20 litros','^18'),'|', '5% de desconto por litro','|')
  print(format('=','=^49'))
  print(format('Gasolina','=^49'))
  print('|',format('até 20 litros','^18'),'|','4% de desconto por litro','|')
  print('|', format('acima de 20 litros','^18'),'|', '6% de desconto por litro','|')
  print(format('=','=^49'))


tabela_precos()
volume_e_tipo()


