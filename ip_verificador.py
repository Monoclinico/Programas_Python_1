#!/usr/bin/python
#_*_coding:utf-8_*_
print('Verificador de Sintaxe de IP 1.0')
while True:
    c = 0
    ip = str(input('Digite o endereço de IP(ex: 198.168.0.7):')).strip()
    ip_lista = ip.split('.')
    if len(ip_lista) == 4:
        for x in range(4):
            try:
                if (int(ip_lista[x]) <= 255) and (int(ip_lista[x]) >= 0):
                    ip_lista[x] = int(ip_lista[x])
                    c += 1
                else:
                    break
            except (ValueError, TypeError):
                break
        if c == 4:
            break
    print('Endereço de IP inválido')
    continue
for x in range(4):
    ip_lista[x] = str(ip_lista[x])
ip = '.'.join(ip_lista)
print('Endereço de IP válido: {}'.format(ip))


