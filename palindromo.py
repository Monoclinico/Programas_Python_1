#-*- coding: utf-8 -*-

print('Teste de palíndromo')

texto = str(input('Digite um texto: ')).strip().split() #entrada de dados (strings), remove os espaços

texto = ''.join(texto) # junta tudo, assim ['m','u','n','d','o'] ==> ['mundo']

if texto == texto[::-1]: print('Esse texto é palíndromo!') # testa se a string X é igual a string X inversa

else: print('Esse texto não é palíndromo!')
