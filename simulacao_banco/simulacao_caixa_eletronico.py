from time import sleep
import datetime
import acessar_contas

#imprime uma linha formatada
def linha_estetica(quebra_antes=True,quebra_depois=True):
  if (quebra_antes):
    print()
  print("="*60)
  if (quebra_depois):
    print()

#imprime o nome do banco formatado
def nome_banco():
  linha_estetica(True,False)
  print(format("BANCO PYTHON","=^60"))
  linha_estetica(False,False)

#imprime a mensagem de alguma sessao encerrada
def encerrar(sessao=""):
  print()
  print(format("SESSAO DE "+sessao+" ENCERRADA","=^60"))

#imprime um painel de opcoes de acesso ao banco 
def opcoes_conta():
  nome_banco()
  print(format("CRIAR CONTA [0] ---- [1] ACESSAR CONTA"," ^60"))
  print(format("       SAIR [2] ----                  "," ^60"))
  linha_estetica(False,False)

def opcoes_acesso(numero_conta, nome_pessoa,saldo_pessoa=0,mostrar=False):
  nome_banco()
  print("NOME: "+nome_pessoa)
  print("CONTA: "+ numero_conta)
  if (mostrar):
    print("SALDO: {:.2f}".format(saldo_pessoa))
  else:
    print("SALDO: ######")
  print(format(format("MOSTRAR SALDO [0] ---- [1] SACAR"," ^37")," ^60"))
  print(format("    DEPOSITAR [2] ---- [3] TRANSFERIR"," ^60"))
  print(format("       VOLTAR [4] ---- [5] SAIR      "," ^60"))
  linha_estetica(False,False)

def conta_criada_com_sucesso():
  print()
  print(format("CONTA CRIADA COM SUCESSO","=^60"))

def deposito_realizado_com_sucesso():
  print()
  print(format("DEPOSITO REALIZADO COM SUCESSO","=^60"))

#interface para acessar o saque
def acessar_deposito(usuario):
  VALOR_MAX = 50000
  VALOR_MIN = 5
  valor = 0
  while True:
    nome_banco()
    valor = 0
    print("-> Valor minimo para depositar: R$ 5,00.")
    print("-> Valor maximo para depositar: R$ 50.000,00")
    print("-> Nao possivel depositar moedas.")
    valor = str(input('VALOR PARA DEPOSITAR: R$')).strip()
    if ((valor.isnumeric()) and (valor.count(" ") <1)):
      if valor.count(',') >= 1:
          print('-> Digite o valor sem virgula ou ponto, por favor.')
      elif valor.count('.') >= 1:
          print('-> Digite o valor sem virgula ou ponto, por favor.')
      elif int(valor) < VALOR_MIN:
          print('-> O minimo para deposito e R$ 5,00.')
      else:
        if (int(valor) <= VALOR_MAX):
            print('-> Este valor pode ser depositado nesta maquina.')
            resposta_deposito = str(input("CONFIRMAR DEPOSITO[S/N]? ")).strip().upper()
            if (resposta_deposito == 'S'):
              acessar_contas.modificar_saldo(usuario,True,valor)  
              deposito_realizado_com_sucesso()
              break
            else:
              resposta_deposito_cancelar1 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
              if (resposta_deposito_cancelar1 == 'S'):
                continue
              else:  
                break
        else:
            print('-> Este valor nao pode ser depositado nesta maquina.')
            resposta_deposito_cancelar2 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
            if (resposta_deposito_cancelar2 == 'S'):
              continue
            else:  
              break
    else:
      print("-> Valor invalido.")
      resposta_deposito_cancelar3 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
      if (resposta_deposito_cancelar3 == 'S'):
        continue
      else:  
        break
  encerrar("DEPOSITO")    


def acessar_transferencia(usuario):
  VALOR_MAX = 50000
  conta_pessoa = None
  valor = 0
  while True:
    nome_banco()
    valor = 0
    print("Para cancelar a transferencia nao preencha com o valor")
    conta_pessoa = str(input('Numero da Conta que recebera o valor: ')).strip()
    dados_destino = acessar_contas.retornar_conta_e_nome(conta_pessoa)
    print('Nome: '+dados_destino[0][1]+ ' Conta: '+dados_destino[0][0])
    valor = str(input('Valor Minimo Permitido para transferir: R$ 5,00.\nValor para transferir: R$ ')).strip()
    if (valor.isnumeric()):
      if valor.count(',') >= 1:
          print('Digite o valor sem virgula ou ponto, por favor.')
      elif valor.count('.') > 1:
          print('Digite o valor so com um ponto, por favor.')
      elif float(valor) < 10:
          print('O minimo para transferir e R$ 10,00.')
      else:
        if (float(valor) <= VALOR_MAX):
            print('Este valor pode ser transferido.')
            break
        else:
            print('Este valor nao pode ser transferido.')
    else:
      break

  acessar_contas.modificar_saldo(usuario,False,valor)  
  acessar_contas.modificar_saldo(dados_destino,True,valor)

def acessar_caixa(usuario):
  Total = 5000
  while True:
      cancelar_saque = False
      if Total < 5:
          print('\nAcabaram as cedulas desta maquina')
          break
      while True:
          nome_banco()

          print("Para cancelar o saque nao preencha com o valor")
          valor = str(input('\nValor Minimo Permitido para Sacar: R$ 5,00.\nValor para sacar(Nao possivel sacar moedas): R$ ')).strip()
          if (valor.isnumeric()):
            if valor.count(',') >= 1:
                print('Digite o valor sem virgula ou ponto, por favor.')
            elif valor.count('.') >= 1:
                print('Digite o valor sem virgula ou ponto, por favor.')
            elif int(valor) < 5:
                print('O minimo para saque e R$ 5,00.')
            else:
              if int(valor) <= float(usuario[0][3]):
                if int(valor) <= Total:
                    print('Este valor esta disponivel para saque nesta maquina.')
                    break
                else:
                    print('Este valor nao esta disponivel para saque nesta maquina.')
              else:
                print("Este valor nao pode ser sacado")
          else:
            cancelar_saque = True
            break
      if cancelar_saque:
        encerrar("SAQUE")
        break

      valor = int(valor)
      valorR = valor

      nota100 = 0
      nota50 = 0
      nota20 = 0
      nota10 = 0
      nota5 = 0
      nota2 = 0
      
      if valor % 100 >= 0 and valor % 100 != 3 and valor % 100 != 1 and valor >= 100:
            nota100 = valor // 100
            valor = valor % 100
            print('{} nota(s) de R$ 100,00'.format(nota100))

      if valor % 50 >= 0 and valor % 50 != 3 and valor % 50 != 1 and valor >= 50:
            nota50 = valor // 50
            valor = valor % 50
            print('{} nota(s) de R$ 50,00'.format(nota50))

      if valor % 20 >= 0 and valor % 20 != 3 and valor % 20 != 1 and valor >= 20:
            nota20 = valor // 20
            valor = valor % 20
            print('{} nota(s) de R$ 20,00'.format(nota20))

      if valor % 10 >= 0 and valor % 10 != 3 and valor % 10 != 1 and valor >= 10:
            nota10 = valor // 10
            valor = valor % 10
            print('{} nota(s) de R$ 10,00'.format(nota10))

      if valor % 5 >= 0 and valor % 5 != 3 and valor % 5 != 1 and valor >= 5:
            nota5 = valor // 5
            valor = valor % 5
            print('{} nota(s) de R$ 5,00'.format(nota5))

      elif valor % 2 != 0:
            nota5 = (valor - (valor % 10) - 5) // 5
            valor = (valor % 10 + 5)
            print('{} nota(s) de R$ 5,00'.format(nota5))

      if valor % 2 >= 0 and valor % 2 != 3 and valor % 2 != 1 and valor >= 2:
            nota2 = valor // 2
            valor = valor % 2
            print('{} nota(s) de R$ 2,00'.format(nota2))

      print('TOTAL = R$ {}'.format(valorR))
      RE = input('\nCONFIRMAR SAQUE(S/N)? ').strip().upper()
      if RE == 'N':
          RE = input('CANCELAR(S/N)? ').strip().upper()
          if RE == 'S':
              break
      else:
          acessar_contas.modificar_saldo(usuario,False,valorR)
          print('Processando notas', end='')
          Total -= valorR
          for v in range(1, 4):
              sleep(0.8)
              print('.', end='')
          print('\nRetire suas notas.')
          sleep(2.3)
          print('\nImprimindo extrato',end='')
          for v in range(1, 4):
              sleep(0.8)
              print('.', end='')
          print('\n')
          print('EXTRATO BANCO PYTHON')
          print('Data: {}/{}/{} \nHorário: {}h e {}min' 
  '\nTotal: R$ {},00'.format(datetime.date.today().day,
                    datetime.date.today().month, datetime.date.today().year,
                    datetime.datetime.today().hour,datetime.datetime.today().minute, valorR))
          break

# interface para criar a conta no banco
def interface_criar_conta():
  sair = "S"
  while (True):
    nome_banco()
    sair = str(input("Deseja criar uma conta[S/N]? ")).strip().upper()
    if (sair == 'N'):
      break

    nome_completo = str(input("Informe seu nome completo: "))
    nome_completo = nome_completo.strip().lower().title()
    if (len(nome_completo) >0):
      break
    else:
      print("Informe o nome corretamente")
      continue
  if (sair == 'N'):
    encerrar("CRIACAO DE CONTA")
    return

  while (True):
    sair = str(input("Continuar com a criacao da conta[S/N]? ")).strip().upper()
    if (sair == 'N'):
      break

    senha1 = str(input("Crie uma senha de 8 digitos: "))
    senha1 = senha1.strip()
    senha2 = str(input("Repita a senha criada: "))
    senha2 = senha2.strip()
    if ((senha1 == senha2) and (len(senha1) > 0) and (len(senha2) > 0) and (len(senha1) == 8)):
      break
    else:
      print("Informe a senha corretamente")
      continue

  if (sair == 'N'):
    encerrar("CRIACAO DE CONTA")
    return

  print(acessar_contas.criar_conta(nome_completo,senha2))
  conta_criada_com_sucesso()

#interface para acessar a conta no banco
def interface_acessar_conta():
  sair = "S"
  dados_conta = None
  while (True):
    nome_banco()
    sair = str(input("Deseja acessar sua conta[S/N]? ")).strip().upper()
    if (sair == 'N'):
      break

    conta = str(input("Informe o numero da sua conta: "))
    conta = conta.strip().lower().title()

    senha = str(input("Informe sua senha de 8 digitos: "))
    senha = senha.strip()

    if ((len(conta) >0) and (len(senha) == 8)):
      dados_conta = acessar_contas.retornar_conta(conta,senha)
      if (len(dados_conta) != 0):
        return dados_conta
      else:
        continue
    else:
      print("Informe os dados corretos")
      continue

  if (sair == 'N'):
    return []
    

def interface_principal():
  while True:
    dados_usuario = None
    
    opcoes_conta()
    opcao = str(input("Opcao escolhida: ")).strip()
    if (opcao == '0'):
      interface_criar_conta()
    elif (opcao == '1'):
      resposta_encerrar2 = False
      escolha_mostrar = False
      dados_usuario = interface_acessar_conta()
      while True:
        opcoes_acesso(dados_usuario[0][0],dados_usuario[0][1],dados_usuario[0][3],escolha_mostrar)
        opcao2 = str(input("Opcao escolhida: ")).strip()
        linha_estetica(False,False)
        if (opcao2 == '0'):
          escolha_mostrar = True
        elif (opcao2 == '1'):
          acessar_caixa(dados_usuario)
          break
        elif (opcao2 == '2'):
          acessar_deposito(dados_usuario)
          break
        elif (opcao2 == '3'):
          acessar_transferencia(dados_usuario)
          break
        elif (opcao2 == '4'):
          break
        elif (opcao2 == '5'):
          resposta_encerrar2 = True
          break
        else:
          continue
      if resposta_encerrar2:
        encerrar()
        break
    else:
      resposta_encerrar = str(input("Encerrar Sessao[S/N]?")).strip().upper()
      if (resposta_encerrar == 'S'):
        encerrar("BANCO")
        break
      else:
        continue



interface_principal()
