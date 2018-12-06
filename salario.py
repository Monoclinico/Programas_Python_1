#-*- coding: utf-8 -*-

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""

ganho_h = float(input('Digite seu ganho por hora: '))
horas = float(input('Digite suas horas trabalhadas: '))
ganho_t = ganho_h * horas
ir = ganho_t * 0.11
inss = ganho_t * 0.08
sind = ganho_t * 0.05
ganho_l = ganho_t - (ir + inss + sind)
print('+Salário Bruto: R$ {:.2f}\n'
  '-IR (11%): R$ {:.2f}\n'
  '-INSS (8%): R$ {:.2f}\n'
  '-Sindicato (5%): R$ {:.2f}\n'
  '=Salário Líquido: R$ {:.2f}'.format(ganho_t,ir,inss,sind,ganho_l))




