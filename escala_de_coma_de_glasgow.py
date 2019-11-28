"""
A Escala de Glasgow foi criada em 1974 por dois professores de neurologia da Universidade de Glasgow (Escocia) 
para medir o nivel de consciencia após uma lesao cerebral. 

Sao avaliados tres parâmetros: abertura ocular, resposta verbal e resposta motora
Como e a pontuacao?

Em cada uma das tres categorias (abertura ocular, resposta verbal e resposta motora) 
os medicos atribuem uma pontuacao dentro dos valores possiveis da categoria para cada nivel de resposta.

Abertura Ocular

    Espontanea: 4
    Ao estimulo sonoro: 3
    Ao estimulo de pressao: 2
    Sem resposta: 1

Resposta Verbal

    Fala orientada: 5
    Fala confusa: 4
    Verbaliza palavras soltas: 3
    Verbaliza sons (gemidos): 2
    Sem resposta: 1

Resposta Motora

    Obedece comandos: 6
    Localizacao estimulo de pressao: 5
    Flexao normal: 4
    Flexao anormal: 3
    Extensao anormal: 2
    Sem resposta: 1

A soma dos pontos da escala vai de 3 (minimo) a 15 (maximo). 
Quanto menor a pontuacao ao fim da avaliacao, mais grave e a lesao. 
"""

#Inicio
ESCALA = {
	"Abertura Ocular":{    
    "Espontanea": 4,
    "Ao estimulo sonoro": 3,
    "Ao estimulo de pressao": 2,
    "Sem resposta": 1
	},
  "Resposta Verbal":{
    "Fala orientada": 5,
    "Fala confusa": 4,
    "Verbaliza palavras soltas": 3,
    "Verbaliza sons (gemidos)": 2,
    "Sem resposta": 1
  },
  "Resposta Motora":{
		"Obedece comandos": 6,
    "Localizacao estimulo de pressao": 5,
    "Flexao normal": 4,
    "Flexao anormal": 3,
    "Extensao anormal": 2,
    "Sem resposta": 1
  }}
RESULTADO = {"Trauma leve":{13,14,15},"Truma moderado":{9,10,11,12},"Trauma grave":{3,4,5,6,7,8}}

soma: int = 0
print()
print(" Escala de Glasgow ".center(50,"="))
for categoria in ESCALA.keys():
	print()
	print((" "+categoria+" ").center(50,"="))
	for resposta in ESCALA[categoria]:
		print(" -> {}: {}".format(resposta,ESCALA[categoria][resposta]))
	limite = max((ESCALA[categoria].values()))
	print("-"*50)
	while True:
		try:
			pontuacao = str(input("Informe a pontuacao de {}: ".format(categoria))).strip()
			if (pontuacao.isdecimal() and (int(pontuacao) <= limite) and (int(pontuacao) > 0)):
				pontuacao = int(pontuacao)
				break
			else:
				print("Informe corretamente.")
				continue
		except:
			print("Informe corretamente.")

	soma+= pontuacao
print()
print(" Resultado ".center(50,"="))
for trauma in RESULTADO.keys():
	if soma in RESULTADO[trauma]:
		print(" -> Trauma leve: de 13 a 15")
		print(" -> Trauma moderado: de 9 a 12")
		print(" -> Trauma grave: de 3 a 8")
		print("="*50)
		print(" => SOMA = {}".format(soma))
		print(" => CORRESPONDE A: {}".format(trauma))
		break
#Fim