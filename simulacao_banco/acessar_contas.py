
import os
import sqlite3

"""Interface para interagir com o banco de dados"""

#funcao que define o caminho para o arquivo dos dados dos usuarios
def acesso_tabela_contas(nome_arquivo,nome_diretorio):
  try:
    arquivo = nome_arquivo.strip()
    pasta_projeto = nome_diretorio.strip()
    caminho_abs = os.getcwd()
    lista_arquivos = os.listdir(caminho_abs)
    if (arquivo in lista_arquivos):
      caminho_abs = os.path.abspath(arquivo)
      caminho_abs = os.path.normcase(caminho_abs)
      caminho_abs = os.path.normpath(caminho_abs)
      return caminho_abs
    else:
      if  pasta_projeto in lista_arquivos:
        caminho_abs += '\\' + pasta_projeto + '\\' + arquivo
        caminho_abs = os.path.normcase(caminho_abs)
        caminho_abs = os.path.normpath(caminho_abs)
        return caminho_abs
      else:
        raise FileNotFoundError
  except:
    return 0


#funcao que retorna os dados da conta e se a conta existe
def retornar_conta(conta,senha):
  conta_e_existencia = None
  conta_pessoa = str(conta).strip()
  senha_pessoa = str(senha)

  conexao = sqlite3.connect(acesso_tabela_contas("contas_bancarias.db","simulacao_banco"))
  navegar_manipular = conexao.cursor()
  navegar_manipular.execute("""SELECT conta, nome, senha, saldo FROM clientes WHERE conta = (?) AND senha = (?)""",(conta_pessoa, senha_pessoa))
  
  conta_e_existencia = navegar_manipular.fetchall()
  conexao.close()
  return conta_e_existencia

#funcao que cria a conta bancaria
def criar_conta(nome,senha):
  
  nome_pessoa = str(nome).strip()
  senha_pessoa = str(senha)
  saldo_pessoa = 0
  conta_pessoa = None

  conexao = sqlite3.connect(acesso_tabela_contas("contas_bancarias.db","simulacao_banco"))
  navegar_manipular = conexao.cursor()
  navegar_manipular.execute("""SELECT conta FROM clientes ORDER BY conta DESC LIMIT 1""")
  ultima_conta = navegar_manipular.fetchall()
  if (len(ultima_conta)) > 0:
    conta_pessoa = str(int(ultima_conta[0][0]) + 1)
  else:
    conta_pessoa = "1000"
  conta = (conta_pessoa,nome_pessoa,senha_pessoa,saldo_pessoa)
  navegar_manipular.execute("""INSERT INTO clientes (conta, nome, senha, saldo) VALUES (?,?,?,?)""",conta)
  conexao.commit()
  navegar_manipular.execute("""SELECT conta, nome, senha FROM clientes WHERE conta = (?) AND senha = (?)""",(conta_pessoa, senha_pessoa))
  dados_conta = navegar_manipular.fetchall()
  conexao.close()
  return dados_conta
    
#funcao para modificar saldo da conta
def modificar_saldo(dados,modo, valor):
 
  saldo_novo = float(dados[0][3])
  if modo:
    saldo_novo += float(valor)
  else:
    saldo_novo -= float(valor)
  dados_usuario = (saldo_novo,dados[0][0])
  conexao = sqlite3.connect(acesso_tabela_contas("contas_bancarias.db","simulacao_banco"))
  navegar_manipular = conexao.cursor()
  navegar_manipular.execute("""UPDATE clientes SET saldo = (?) WHERE conta=(?)""",dados_usuario)
  conexao.commit()
  conexao.close()


#funcao para criar a tabela para a base de dados
def criar_tabela(criar=True):

  conexao = sqlite3.connect(acesso_tabela_contas("contas_bancarias.db","simulacao_banco"))
  navegar_manipular = conexao.cursor()
  if (criar):
    navegar_manipular.execute("""
    CREATE TABLE clientes (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      conta TEXT NOT NULL UNIQUE,
      nome TEXT NOT NULL,
      senha TEXT NOT NULL,
      saldo REAL NOT NULL 

    );
    """)
  conexao.close()

#funcao para remover a tabela da base de dados
def remover_tabela(remover=True):
  conexao = sqlite3.connect(acesso_tabela_contas("contas_bancarias.db","simulacao_banco"))
  navegar_manipular = conexao.cursor()
  if (remover):
    navegar_manipular.execute("""DROP TABLE clientes;""")
  conexao.close()


