from time import sleep
import datetime
import acessar_contas

def nome_banco():
  print()
  print("="*15+"BANCO PYTHON"+"="*15)

def linha_estetica():
  print()
  print("="*30)

def encerrar(sessao=""):
  print()
  print("="*15+"SESSAO DE "+sessao+" ENCERRADA"+"="*15)

def opcoes_conta():
  print()
  print("CRIAR CONTA [0] ================= [1] ACESSAR CONTA")
  print("       SAIR [2] ================= ")
  print()
def opcoes_acesso(numero_conta, nome_pessoa):
  print()
  print("NOME: "+nome_pessoa)
  print("CONTA: "+ numero_conta)
  print("MOSTRAR SALDO [0] =============== [1] SACAR")
  print("    DEPOSITAR [2] =============== [3] TRANSFERIR PARA OUTRA CONTA")
  print("       VOLTAR [4] =============== [5] SAIR")
  print()

def conta_criada_com_sucesso():
  print()
  print("=========CONTA CRIADA COM SUCESSO=========")

def acessar_caixa(usuario):
  Total = 5000
  while True:
      cancelar_saque = False
      if Total < 5:
          print('\nAcabaram as cedulas desta maquina')
          break
      while True:
          nome_banco()
          # while True:
          #     senha = str(input('Digite a senha de 8 dígitos: ')).strip()
          #     if len(senha) == 8:
          #         break
          #     print('Senha incorreta')
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
              print('PROCESSO FINALIZADO.')
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
          print('PROCESSO FINALIZADO.')
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
    nome_banco()
    opcoes_conta()
    opcao = str(input("Opcao escolhida: ")).strip()
    if (opcao == '0'):
      interface_criar_conta()
    elif (opcao == '1'):
      resposta_encerrar2 = False
      dados_usuario = interface_acessar_conta()
      while True:
        opcoes_acesso(dados_usuario[0][0],dados_usuario[0][1])
        opcao2 = str(input("Opcao escolhida: ")).strip()
        if (opcao2 == '0'):
          print()
          print("SALDO ATUAL: R${:.2f}".format(dados_usuario[0][3]))
        elif (opcao2 == '1'):
          acessar_caixa(dados_usuario)
          break
        elif (opcao2 == '2'):
          break
        elif (opcao2 == '3'):
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
