#Validador de e-mail 1.0

def validae(email):
    """Verifica se um e-mail é válido, se for retorna True, se não retorna False"""
    # Lista de caracteres que não podem ir no e-mail
    car_espec = ['á', 'à', 'é', 'ó', 'í', 'ã', 'õ', 'ç', 'ú', 'ê', 'â', 'ô',
                 'è', '+', '-', '/', '*', ':', '?', '!', ';', ',', 'ª', 'º',
                 '°', '>', '<', '=', '"', "'", '#', '&', '(', ')',
                 '¬', '\\', '|', '^', '~', '´', '`', '..']
    email1 = str(email).strip()
    especial =  False
    resposta = True
    for c_a_r in car_espec:
        if c_a_r in email1:
            especial = True
    if especial:
        resposta = False
    if ' ' in email1:
        resposta = False
    if '@' in email1:
        endereco = email1.split('@')
        if '.' in endereco[1]:
            endereco2 = endereco[1].split('.')
            if '' in endereco2:
                resposta = False
        else:
            resposta = False
    else:
        resposta = False
    return  resposta

def npt(email):
    if validae(email):
        lista = email.split('@')
        lista = [lista[0]] + lista[1].split('.')
        return lista
    else:
        return 'Invalid E-mail'