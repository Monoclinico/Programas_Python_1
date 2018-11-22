# -*- coding: utf-8 -*-
#Scrip para criar tabuadas de números. 
'''
Exemplo de uma tabuada retornada:
++++++++++++++++++++++++++++++++++++++++
CRIAR A TABUADA DO: 5
 0 x 5 = 0
 1 x 5 = 5
 2 x 5 = 10
 3 x 5 = 15
 4 x 5 = 20
 5 x 5 = 25
 6 x 5 = 30
 7 x 5 = 35
 8 x 5 = 40
 9 x 5 = 45
10 x 5 = 50
++++++++++++++++++++++++++++++++++++++++
'''
#executa a aplicação enquanto o usuário digitar n, sendo n >= 0. 
while True:
    print("+"*40) #decora com uma linha composta por 40 '+'. 
    try:
        num = float(input('CRIAR A TABUADA DO: ')) #recebe os valores (tipo ponto flutuante) do usuário. 
    except ValueError: #se "num" não receber um número float ou int, o ciclo/loop é iniciado de novo sem contruir a tabuada.
        continue
    if num < 0: #se o valor de entrada for menor que 0, a aplicação é interrompida.
        break
    for tab in range(0, 11): #cria a tabuada do número passado; de (0... até 10) * num
        print('{:.2f} x {} = {}'.format(tab, num, num * tab)) 