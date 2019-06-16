#-*- coding: utf-8 -*-

print('Teste de palíndromo')
texto = str(input('Digite um texto: '))#entrada de dados (strings)
texto = texto.replace(" ","")#remove todos os espaços
if texto == texto[::-1]: 
  print('Esse texto é palíndromo!') # testa se a string X é igual a string X inversa
else: 
  print('Esse texto não é palíndromo!')