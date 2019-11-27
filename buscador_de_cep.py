"""
-> Buscador de CEPs 1.0
-> Utiliza a api da ViaCep: https://viacep.com.br/
-> Informe um cep da regiao do Brasil com argumento do programa
"""


def obter_cep(cep: str="99999999") -> dict:
  import requests
  dados_cep: dict = {}
  try:
    cep = str(cep).strip()
    if ((cep.isdecimal()) and (len(cep) == 8)):
      nova_requisicao = requests.get("https://viacep.com.br/ws/{0}/json/".format(cep))
      if nova_requisicao.status_code == 200:
        dados_cep = nova_requisicao.json()
        if "erro" in list(dados_cep.keys()):
          dados_cep.clear()
          dados_cep["erro"] = "Cep nao encontrado."
          return dict(dados_cep)
        else:
          return dict(dados_cep)
      else:
        dados_cep["erro"] = nova_requisicao.status_code
        return dados_cep
    else:
      dados_cep["erro"] = "Formato de cep invalido."
      return dados_cep
  except BaseException:
    dados_cep.clear()
    dados_cep["erro"] = "Um erro ocorreu no programa."
    return dados_cep
  
def mostrar_dados(dados_json: dict = {}) -> str:
  dados_dict = list(dados_json.items())
  print()
  for c in range(0,len(dados_dict)):
    if len(dados_dict[c][1]) == 0:
      print("{0}: {1}".format(dados_dict[c][0], "nenhum"))
    else:
      print("{0}: {1}".format(dados_dict[c][0], dados_dict[c][1]))
  print()

if __name__ == "__main__":

  import sys
  from time import sleep
  try:
    argumentos = sys.argv
    if len(argumentos) > 1:
      cep = argumentos[1:2]
      cep = str(cep[0])
    else:
      cep = str(input("Informe um CEP da regiao do Brasil (so numeros): ")).strip()
    mostrar_dados(obter_cep(cep))
    sleep(60)
    print("Programa Encerrado")
  except BaseException:
    print("erro: Um erro ocorreu no programa.")
    print("Programa Encerrado")