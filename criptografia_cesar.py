#!/usr/bin/python
#_*_coding:utf-8_*_
"""Módulo para criptografia e descriptografia de Júlio Cesar V1.0"""

#tratamento do texto da mensagem
def requisitar_mensagem(mensagem):
  try:
    texto_original = str(mensagem)
  except:
    return None
  texto = texto_original.strip()
  texto = texto.lower()
  char_especiais = ['á','à','é','ó','í','ã','õ','ç','ú','ê','â','ô','è']
  char_substitutivo = ['a','a','e','o','i','a','o','c','u','e','a','o','e']
  #substitui os caracteres especiais por letras simples.
  for l in range(0,len(texto)):
    if (texto[l] in char_especiais):
      texto = texto.replace(texto[l],char_substitutivo[char_especiais.index(texto[l])])
  #fim do tratamento
  return texto_original, texto

#define a chave de criptografia
def definir_chave(chave):
  chave_primaria = 0
  chave_secundaria = 0
  try:
    chave_secundaria = int(chave)
    if (chave_secundaria >=0):
      chave_primaria = abs(chave_secundaria) % 26
    else:
      chave_primaria = 26 - (abs(chave_secundaria) % 26)
  except:
    return None
  return chave_primaria, chave_secundaria

#função de criptografia
def criptografia_cesar(chave,mensagem):
  chave_primaria = chave
  texto = mensagem
  texto_cifrado = ""
  alfabeto = []
  for l in range((97), (123)): #97-122: a-z
    alfabeto.append(chr(l))
  n = 0
  for posicao in range(0,len(texto)):
    try:
      n = alfabeto.index((texto[posicao]))
      if (n+chave_primaria >25):
        n -=26
      texto_cifrado += alfabeto[n+chave_primaria]
    except:
      texto_cifrado += texto[posicao]
  return texto_cifrado

#entrada e saída as informações
def criptografar(mensagem, chave=0, cript=True):
  """Função de criptografia de Júlio Cesar.\n
    criptografar(mensagem,chave=0,cript=True)\n
    Se True: retorna uma lista [mensagem original, chave primária,chave secundária, mensagem criptografada]\n 
    Se False: retorna uma lista [mensagem original, dicionário{chave:mensagem}]"""
  mensagem_original, mensagem_tratada = requisitar_mensagem(mensagem)
  chave_p, chave_s = definir_chave(chave)
  if cript:
    mensagem_criptografada = criptografia_cesar(chave_p, mensagem_tratada)
    return [mensagem_original,chave_p,chave_s,mensagem_criptografada]
  else:
    dicionario_mensagem_descriptografada = {}
    for v in range(27):
      dicionario_mensagem_descriptografada[v] = criptografia_cesar(v, mensagem_tratada)
    return [mensagem_original,dicionario_mensagem_descriptografada]

if __name__ == "__main__":
  while True:
    try:
      _mens = str(input("Mensagem: ")).strip()
      _mod = bool(int(input("Criptografar(1) ou Descriptografar(0): ")))
      _chave = 0
      if _mod: 
        _chave = int(input("Chave: "))
      break
    except:
      continue
  resultado = criptografar(_mens, chave=_chave,cript= _mod)
  if _mod:
    print("Mensagem Original: {}".format(resultado[0]))
    print("Chave Primária: {0} | Chave Secundária: {1}".format(resultado[1],resultado[2]))
    print("Mensagem Criptografada: {}".format(resultado[3]))
  else:
    print("Mensagem Original: {}".format(resultado[0]))
    print("Mensagens Possíveis:")
    for c in resultado[1].keys():
      print("Chave {}: {}".format(c,resultado[1][c]))

