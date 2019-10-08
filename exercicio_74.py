#-*- coding:utf-8 -*-

'''
Exercicio_74
Para varios tributos, a base de calculo a o salario minimo. Fazer um algoritmo que
leia o valor do salario minimo e o valor do salario de uma pessoa. Calcular e imprimir
quantos salarios minimos ela ganha.'''

salario_munimo = float(input("Informe o valor do salario minimo: R$"))
salario_pessoa = float(input("Informe o valor do salario de uma pessoa: R$"))
salarios_minimos = salario_pessoa/salario_munimo
print("A pessoa ganha R${0}, que equivale a {1:.2} salario{2}minimo{2}".format(salario_pessoa,salarios_minimos,("s " if (salarios_minimos !=1) else " ")))