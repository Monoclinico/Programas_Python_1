#Função Validadora de formato de e-mail V1.1
#+Função que divide o email e cria uma lista
#Sem usar Regex

def validae(email):
    """Verifica se um e-mail é válido, se for retorna True, se não retorna False"""
    # Lista de caracteres que não podem ir no e-mail
    car_espec = ['á', 'à', 'é', 'ó', 'í', 'ã', 'õ', 'ç', 'ú', 'ê', 'â', 'ô',
                 'è', '+', '-', '/', '*', ':', '?', '!', ';', ',', 'ª', 'º',
                 '°', '>', '<', '=', '"', "'", '#', '&', '(', ')',
                 '¬', '\\', '|', '^', '~', '´', '`', '..',' ']
    email1 = str(email).strip()  #remove os espaços antes e depois da string
    especial =  False
    resposta = True
    for c_a_r in car_espec:  #verifica se algum símbolo da lista 'car_espec' está na string 'email1' 
        if c_a_r in email1:
            especial = True
    if especial:  #falseia 'resposta' se 'especial' for verdadeiro 
        resposta = False
    if '@' in email1: #verifica se o símbolo '@' está em 'email1'
        endereco = email1.split('@') #reparte a string 'email1' onde está '@' criando uma lista X
        if '.' in endereco[1]: #verifica se o símbolo '.' está na segunda string da lista X
            endereco2 = endereco[1].split('.') #reparte a segunda string da lista X onde está '.' criando uma lista Y
            if '' in endereco2: #verifica se a lista Y está com letras
                resposta = False
        else:
            resposta = False
    else:
        resposta = False
    return  resposta #retorna um valor Booleano

def npt(email): #divide o email em três partes, como: contato.servicos@hotmail.com ==> 'contato.servicos', 'hotmail', 'com'
    if validae(email):
        lista = email.split('@')
        lista = [lista[0]] + lista[1].split('.')
        return lista #retorna uma lista do email dividido se validae('email qualquer') == True
    else:
        return 'Invalid E-mail' #retorna 'Invalid E-mail' se validae('email qualquer') == False