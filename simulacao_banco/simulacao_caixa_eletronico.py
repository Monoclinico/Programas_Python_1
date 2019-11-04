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
def encerrar(sessao="BANCO"):
  print()
  print(format("SESSAO DE "+sessao+" ENCERRADA","=^60"))

#imprime um painel de opcoes de acesso ao banco 
def opcoes_conta():
  nome_banco()
  print(format("CRIAR CONTA [0] ---- [1] ACESSAR CONTA"," ^60"))
  print(format("       SAIR [2] ----                  "," ^60"))
  linha_estetica(False,False)

#imprime um painel de opcoes da conta
def opcoes_acesso(numero_conta, nome_pessoa,saldo_pessoa=0,mostrar=False):
  nome_banco()
  print("NOME: "+nome_pessoa)
  print("CONTA: "+ numero_conta)
  if (mostrar):
    print("SALDO: R$ {:.2f}".format(saldo_pessoa))
  else:
    print("SALDO: R$ ######")
  print(format("MOSTRAR SALDO [0] ---- [1] SACAR     "," ^60"))
  print(format("    DEPOSITAR [2] ---- [3] TRANSFERIR"," ^60"))
  print(format("       VOLTAR [4] ---- [5] SAIR      "," ^60"))
  linha_estetica(False,False)

#imprime as informacoes de uma conta criada
def informacoes_conta(numero_conta,nome_pessoa):
  print("NOME: "+nome_pessoa)
  print("CONTA: "+numero_conta)
  linha_estetica(False,False)

#imprime uma mensagem quando alguma rotina for feita sem problemas
def rotina_realizada_com_sucesso(rotina="ROTINA"):
  print()
  if (rotina[-1] == "O"):
    print(format(rotina+" REALIZADO COM SUCESSO","=^60"))
  elif (rotina[-1] == "E"):
    print(format(rotina+" REALIZADO COM SUCESSO","=^60"))
  else:
    print(format(rotina+" REALIZADA COM SUCESSO","=^60"))

#funcao para validar o formato da senha
def validar_formato_senha(senha):
  senha_temporaria = str(senha)
  if (len(senha_temporaria) == 8) and (senha_temporaria.count(" ") < 1):
    for c in range(0,len(senha_temporaria)):
      if not(senha_temporaria[c].isnumeric()):
        return False
    return True
  else:
    return False

#funcao para validar o formato da conta
def validar_formato_conta(conta):
  conta_temporaria = str(conta)
  if (len(conta_temporaria) == 4) and (conta_temporaria.count(" ") < 1):
    for c in range(0,len(conta_temporaria)):
      if not(conta_temporaria[c].isnumeric()):
        return False
    return True
  else:
    return False

#interface para acessar o deposito na conta
def acessar_deposito(usuario):
  VALOR_MAX = 50000
  VALOR_MIN = 5
  valor = 0
  while (True):
    nome_banco()
    valor = 0
    print("-> Valor minimo para depositar: R$ {0},00.".format(VALOR_MIN))
    print("-> Valor maximo para depositar: R$ {0},00.".format(VALOR_MAX))
    print("-> Nao possivel depositar moedas.")
    valor = str(input("VALOR PARA DEPOSITAR: R$")).strip()
    if ((valor.isnumeric()) and (valor.count(" ") <1)):
      if valor.count(",") >= 1:
          print("-> Digite o valor sem virgula ou ponto, por favor.")
          resposta_deposito_cancelar1 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
          if (resposta_deposito_cancelar1 == "S"):
            continue
          else:  
            break
      elif valor.count(".") >= 1:
          print("-> Digite o valor sem virgula ou ponto, por favor.")
          resposta_deposito_cancelar2 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
          if (resposta_deposito_cancelar2 == "S"):
            continue
          else:  
            break
      elif int(valor) < VALOR_MIN:
          print("-> O minimo para deposito e R$ {0},00.".format(VALOR_MIN))
          resposta_deposito_cancelar3 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
          if (resposta_deposito_cancelar3 == "S"):
            continue
          else:  
            break
      else:
        if (int(valor) <= VALOR_MAX):
            print("-> Este valor pode ser depositado nesta maquina.")
            resposta_deposito = str(input("CONFIRMAR DEPOSITO[S/N]? ")).strip().upper()
            if (resposta_deposito == "S"):
              acessar_contas.modificar_saldo(usuario,True,valor)  
              rotina_realizada_com_sucesso("DEPOSITO")
              break
            else:
              resposta_deposito_cancelar4 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
              if (resposta_deposito_cancelar4 == "S"):
                continue
              else:  
                break
        else:
            print("-> Este valor nao pode ser depositado nesta maquina.")
            resposta_deposito_cancelar5 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
            if (resposta_deposito_cancelar5 == "S"):
              continue
            else:  
              break
    else:
      print("-> Valor invalido.")
      resposta_deposito_cancelar6 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
      if (resposta_deposito_cancelar6 == "S"):
        continue
      else:  
        break
  encerrar("DEPOSITO")    


#interface para acessar a transferencia para outra conta
def acessar_transferencia(usuario):
  VALOR_MAX = 50000
  VALOR_MIN = 10
  while (True):
    nome_banco()
    valor = 0
    valor_sem_ponto = ""
    conta_pessoa = 0
    print("-> Valor minimo para transferir: R$ {0},00.".format(VALOR_MIN))
    print("-> Valor maximo para transferir: R$ {0},00.".format(VALOR_MAX))
    conta_pessoa = str(input("NUMERO DA CONTA QUE RECEBE O VALOR: ")).strip()
    if validar_formato_conta(conta_pessoa):
      dados_destino = acessar_contas.retornar_conta_e_nome(conta_pessoa)
      if (len(dados_destino[0]) > 0):
        informacoes_conta(dados_destino[0][0],dados_destino[0][1])
        valor = str(input("VALOR PARA TRANSFERIR: R$ ")).strip()
        if (valor.count(".") > 0):
          valor_sem_ponto = valor.replace(".","")
        else:
          valor_sem_ponto = valor
        if (valor_sem_ponto.isnumeric()):
          if valor.count(",") >= 1:
              print("-> Digite o valor sem virgula, por favor.")
              resposta_deposito_cancelar1 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
              if (resposta_deposito_cancelar1 == "S"):
                continue
              else:  
                break
          elif valor.count(".") > 1:
              print("-> Digite o valor so com um ponto, por favor.")
              resposta_deposito_cancelar2 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
              if (resposta_deposito_cancelar2 == "S"):
                continue
              else:  
                break
          elif float(valor) < VALOR_MIN:
              print("-> O minimo para transferir e R$ {},00.".format(VALOR_MIN))
              resposta_deposito_cancelar3 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
              if (resposta_deposito_cancelar3 == "S"):
                continue
              else:  
                break
          else:
            if (float(valor) <= VALOR_MAX):
                print("-> Este valor pode ser transferido.")
                resposta_transferencia = str(input("CONFIRMAR TRANSFERENCIA[S/N]? ")).strip().upper()
                if (resposta_transferencia == "S"):
                  acessar_contas.modificar_saldo(usuario,False,valor)  
                  acessar_contas.modificar_saldo(dados_destino,True,valor)
                  rotina_realizada_com_sucesso("TRANSFERENCIA")
                  break
                else:  
                  resposta_deposito_cancelar4 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
                  if (resposta_deposito_cancelar4 == "S"):
                    continue
                  else:  
                    break
            else:
                print("-> Este valor nao pode ser transferido.")
                resposta_deposito_cancelar5 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
                if (resposta_deposito_cancelar5 == "S"):
                  continue
                else:  
                  break
        else:
          print("-> Valor invalido.")
          resposta_deposito_cancelar6 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
          if (resposta_deposito_cancelar6 == "S"):
            continue
          else:  
            break
      else:
        print("-> A conta nao foi encontrada.")
        resposta_deposito_cancelar7 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
        if (resposta_deposito_cancelar7 == "S"):
          continue
        else:  
          break
    else:
      print("-> O numero da conta esta incorreto.")
      resposta_deposito_cancelar8 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
      if (resposta_deposito_cancelar8 == "S"):
        continue
      else:  
        break
  encerrar("TRANSFERENCIA")


#funcao que cria a interface para sacar o valor
def acessar_caixa(usuario):
  Total = 10000
  VALOR_MIN = 5
  while (True):
      cancelar_saque = False
      if Total < 5:
          print("-> Acabaram as cedulas desta maquina.")
          break
      while True:
          cancelar_saque = False
          nome_banco()
          print("-> Valor minimo para sacar: R$ {},00".format(VALOR_MIN))
          print("-> Nao e possivel sacar moedas.")
          valor = str(input("VALOR PARA SACAR: R$ ")).strip()
          if (valor.isnumeric()):
            if int(valor) < VALOR_MIN:
                print("-> O minimo para saque e R$ {},00.".format(VALOR_MIN))
                resposta_saque_cancelar1 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
                if (resposta_saque_cancelar1 == "S"):
                  continue
                else:  
                  cancelar_saque = True
                  break
            else:
              if int(valor) <= float(usuario[0][3]):
                if int(valor) <= Total:
                    print("-> Este valor esta disponivel para saque nesta maquina.")
                    linha_estetica(False,False)
                    break
                else:
                    print("-> Este valor nao esta disponivel para saque nesta maquina.")
                    resposta_saque_cancelar2 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
                    if (resposta_saque_cancelar2 == "S"):
                      continue
                    else:  
                      cancelar_saque = True
                      break
              else:
                print("-> Este valor nao pode ser sacado.")
                resposta_saque_cancelar3 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
                if (resposta_saque_cancelar3 == "S"):
                  continue
                else:  
                  cancelar_saque = True
                  break
          else:
            print("-> Valor e invalido para sacar.")
            resposta_saque_cancelar4 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
            if (resposta_saque_cancelar4 == "S"):
              continue
            else:  
              cancelar_saque = True
              break
      if cancelar_saque:
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
            print("{} nota(s) de R$ 100,00".format(nota100))

      if valor % 50 >= 0 and valor % 50 != 3 and valor % 50 != 1 and valor >= 50:
            nota50 = valor // 50
            valor = valor % 50
            print("{} nota(s) de R$ 50,00".format(nota50))

      if valor % 20 >= 0 and valor % 20 != 3 and valor % 20 != 1 and valor >= 20:
            nota20 = valor // 20
            valor = valor % 20
            print("{} nota(s) de R$ 20,00".format(nota20))

      if valor % 10 >= 0 and valor % 10 != 3 and valor % 10 != 1 and valor >= 10:
            nota10 = valor // 10
            valor = valor % 10
            print("{} nota(s) de R$ 10,00".format(nota10))

      if valor % 5 >= 0 and valor % 5 != 3 and valor % 5 != 1 and valor >= 5:
            nota5 = valor // 5
            valor = valor % 5
            print("{} nota(s) de R$ 5,00".format(nota5))

      elif valor % 2 != 0:
            nota5 = (valor - (valor % 10) - 5) // 5
            valor = (valor % 10 + 5)
            print("{} nota(s) de R$ 5,00".format(nota5))

      if valor % 2 >= 0 and valor % 2 != 3 and valor % 2 != 1 and valor >= 2:
            nota2 = valor // 2
            valor = valor % 2
            print("{} nota(s) de R$ 2,00".format(nota2))

      print("TOTAL = R$ {},00".format(valorR))
      linha_estetica(False,False)
      confirmar_saque = input("CONFIRMAR SAQUE(S/N)? ").strip().upper()
      if confirmar_saque == "S":
        acessar_contas.modificar_saldo(usuario,False,valorR)
        print("Processando notas", end="")
        Total -= valorR
        for v in range(1, 4):
            sleep(0.8)
            print(".", end="")
        print("\nRetire suas notas.")
        sleep(2.3)
        print("\nImprimindo extrato",end="")
        for v in range(1, 4):
            sleep(0.8)
            print(".", end="")
        print("\n")
        print("EXTRATO BANCO PYTHON")
        print("Data: {}/{}/{} \nHorário: {}h e {}min" 
          "\nTotal: R$ {},00".format(datetime.date.today().day,
                  datetime.date.today().month, datetime.date.today().year,
                  datetime.datetime.today().hour,datetime.datetime.today().minute, valorR))
        rotina_realizada_com_sucesso("SAQUE")
        break
      else:
        resposta_saque_cancelar5 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
        if (resposta_saque_cancelar5 == "S"):
          continue
        else:  
          break

  encerrar("SAQUE")

# interface para criar a conta no banco
def interface_criar_conta():
  
  while (True):
    nome_banco()
    nome_definido = ""
    senha_definida = ""
    sair1 = str(input("DESEJA CRIAR UMA CONTA[S/N]? ")).strip().upper()
    if (sair1 == "S"):
      nome = str(input("INFORME SEU NOME: "))
      nome = nome.strip()
      senha1 = str(input("CRIE UMA SENHA COM 8 DIGITOS: "))
      senha2 = str(input("REPITA A SENHA CRIADA: "))

      if (len(nome) >0):
        nome_definido = nome.lower().title()
        if (validar_formato_senha(senha1) and validar_formato_senha(senha2)):
          if (senha1 == senha2):
            senha_definida = senha2
            sair2 = str(input("CONFIRMAR A CRIACAO DA CONTA[S/N]? ")).strip().upper()
            if (sair2 == "S"):
              dados_temporarios = acessar_contas.criar_conta(nome_definido,senha_definida)
              rotina_realizada_com_sucesso("CRIACAO DA CONTA")
              informacoes_conta(dados_temporarios[0][0],dados_temporarios[0][1])
              break
            else:
              break
          else:
            print("-> As senhas nao sao iguais.")
            continue
        else:
          print("-> O formato da senha esta incorreto.")
          continue
      else:
        print("-> Informe o nome corretamente.")
        continue
    else:
      break
  encerrar("CRIACAO")
 

#interface para acessar a conta no banco
def interface_acessar_conta():
  dados_conta = []
  while (True):
    dados_conta = []
    nome_banco()
    sair = str(input("DESEJA ACESSAR A CONTA[S/N]? ")).strip().upper()
    if (sair == "S"):
      conta = str(input("INFORME O NUMERO DA CONTA: "))
      senha = str(input("INFORMA A SENHA DE 8 DIGITOS: "))
      if (validar_formato_conta(conta)) and (validar_formato_senha(senha)):
        dados_conta = acessar_contas.retornar_conta(conta,senha)
        if (len(dados_conta) > 0):
          break
        else:
          print("-> A conta ou a senha esta incorreta.")
          resposta_deposito_cancelar1 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
          if (resposta_deposito_cancelar1 == "S"):
            continue
          else:  
            break
      else:
        print("-> Formato da conta ou da senha invalido.")
        resposta_deposito_cancelar2 = str(input("TENTAR NOVAMENTE[S/N]? ")).strip().upper()
        if (resposta_deposito_cancelar2 == "S"):
          continue
        else:  
          break
    else:
      break
  return dados_conta
    
#funcao que cria a interface principal
def interface_principal():
  while (True):
    dados_usuario = []
    opcoes_conta()
    opcao1 = str(input("INFORME A OPCAO: ")).strip()
    if (opcao1 == "0"):
      interface_criar_conta()
    elif (opcao1 == "1"):
      encerrar_interface = False
      escolha_mostrar = False
      dados_usuario = interface_acessar_conta()
      if (len(dados_usuario) >0):
        while (True):
          encerrar_interface = False
          opcoes_acesso(dados_usuario[0][0],dados_usuario[0][1],dados_usuario[0][3],escolha_mostrar)
          opcao2 = str(input("INFORME A OPCAO: ")).strip()
          if (opcao2 == "0"):
            escolha_mostrar = True
          elif (opcao2 == "1"):
            acessar_caixa(dados_usuario)
            break
          elif (opcao2 == "2"):
            acessar_deposito(dados_usuario)
            break
          elif (opcao2 == "3"):
            acessar_transferencia(dados_usuario)
            break
          elif (opcao2 == "4"):
            break
          elif (opcao2 == "5"):
            resposta_encerrar1 = str(input("ENCERRAR SESSAO[S/N]?")).strip().upper()
            if (resposta_encerrar1 == "N"):
              continue
            else:
              encerrar_interface = True
              break
          else:
            resposta_encerrar2 = str(input("ENCERRAR SESSAO[S/N]?")).strip().upper()
            if (resposta_encerrar2 == "N"):
              continue
            else:
              encerrar_interface = True
              break
        if encerrar_interface:
          encerrar()
          break
      else:
        continue
    else:
      resposta_encerrar3 = str(input("ENCERRAR SESSAO[S/N]?")).strip().upper()
      if (resposta_encerrar3 == "N"):
        continue
      else:
        encerrar()
        break

if __name__ == "__main__":
  interface_principal()
