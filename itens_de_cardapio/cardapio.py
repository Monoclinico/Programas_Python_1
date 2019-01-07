# -*- coding: utf-8 -*-
"""
Script em Python que solicita o código do item de um cardápio (em formato csv) e a quantidade comprada.
Então retorna o valor total que deve ser pago pelos itens (neste caso comidas e bebidas).
"""
#importa os módulos csv (para manipular tabelas) e os (para usar funcionalidades do SO)
import csv, os 

#fução que abre o arquivo tabela1.csv
def abrir_tabela():
  caminho_csv = r'\tabela1.csv' 
  try:
    with open(caminho_csv, newline='\n') as arquivo_tabela:
      arquivo_tabela_leitura = csv.reader(arquivo_tabela,delimiter=';')
      arquivo_tabela_leitura = list(arquivo_tabela_leitura)
      return arquivo_tabela_leitura
  except:
    caminho_abs = os.getcwd()
    caminho_abs += caminho_csv
    caminho_abs = os.path.normpath(caminho_abs)
    with open(caminho_abs, newline='\n') as arquivo_tabela:
      arquivo_tabela_leitura = csv.reader(arquivo_tabela,delimiter=';')
      arquivo_tabela_leitura = list(arquivo_tabela_leitura)
      return arquivo_tabela_leitura

#pega os elementos da tabela e retorna uma tupla com eles
def opcoes():
  op = tuple(i +100 for i in range(0,len(arquivo_tabela_leitura)-1)) #100,101,102,103,104,105
  return op

#converte o valor da caluna preço da tabela1.csv em float para as se fazer as contas. Ex: R$ 2,5 ---> 2.50
def formatar_real(s):
  formatado = s.strip().lower()
  formatado = ''.join(formatado.split())
  if formatado.find('r$') == 0:  
    formatado = formatado[2:]
  if formatado.find(',') != -1:
    formatado = formatado.replace(',','.')
  formatado = float(formatado)
  return formatado

#retorna o valor em reais da quantidade escolhida de itens vezes o preço do item
def valor(cod,qua):
  for _p in range(1,len(arquivo_tabela_leitura)):
    if arquivo_tabela_leitura[_p][1] == str(cod):
      valor_t = qua * formatar_real(arquivo_tabela_leitura[_p][2])
      produto = arquivo_tabela_leitura[_p][0]
  return [produto,float(valor_t)]

#faz as perguntas para a entrada de valores e verifica os valores
def perguntas():
  dados = []
  while True:
    try:
      codigo = int(input('Código do item ({}-{}): '.format(min(opcoes()),max(opcoes()))))
      quantidade = int(input('Quantidade de itens (mínimo 0): '))
    except:
      continue
    if (codigo < 100) or (codigo > max(opcoes())) or (quantidade < 0):
      continue
    dados.append(valor(codigo,quantidade))
    dados[-1].append(quantidade)
    mais = str(input('Mais itens (s/n)? ')).strip().lower()
    if mais == 's':
      continue
    else:
      break
  return dados

#imprime na tela o valor total a pagar e os itens escolhidos
def nota(lis):
  soma_total = 0

  print('='*60)
  for i in lis:
    print('| {2:>3}{0:^30}= R$ {1:<3.3f}'.format(i[0],i[1],i[2]))
    soma_total += i[1]
  print('| {:>3}{:^30}= R$ {:.2f}'.format('','Total',soma_total))
  print('='*60)

def fazer_e_repetir():
  def pergunta():
    while True:
      p = str(input(r'Encerrar(s/n)?')).lower().strip()
      if p not in ('s','n'):
        continue
      else:
        if p == 's':
          return 1
        else:
          return 0

  while True:
    global arquivo_tabela_leitura
    arquivo_tabela_leitura = abrir_tabela()
    nota(perguntas())
    if pergunta():
      break
    else:
      continue  
fazer_e_repetir()