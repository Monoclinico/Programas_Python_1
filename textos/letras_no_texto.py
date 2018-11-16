
arquivo = open('texto_analisar.txt','rt')
texto = arquivo.read()
arquivo.close()

arquivo = open('texto_analisar.txt', 'rt')
texto_original = arquivo.read()
arquivo.close()

texto = texto.strip()
texto = texto.split()
texto = ''.join(texto)
texto = texto.lower()

lista_exclusiva = ['á','à','é','ó','í','ã','õ','ç','ú','ê','â','ô','è']
lista_substitut = ['a','a','e','o','i','a','o','c','u','e','a','o','e']

for x in range(len(lista_exclusiva)):
    k = texto.count(lista_exclusiva[x])
    for c in range(k):
        texto = texto.replace(lista_exclusiva[x], lista_substitut[x])

lista_abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z',
             '0','1','2','3','4','5','6','7','8','9','?','!','"',
             "'",'.',',','-','_','/','*','+','=','$','@','#','%',
             '&','(',')','[',']','{','}',';',':','>','<']

texto_p = ''
for x in range(len(lista_abc)):
    n = texto.count(lista_abc[x])
    p = (n / len(texto)) * 100
    if p > 0:
        texto_p += '\n({}) = {:.2f}%'.format(lista_abc[x], p)

arquivo2 = open('char_porcentagem.txt','w')
arquivo2.write(texto_original + texto_p)
arquivo2.close()

