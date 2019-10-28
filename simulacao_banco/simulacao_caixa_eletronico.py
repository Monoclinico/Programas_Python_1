from time import sleep
import datetime

Total = 50000
while True:
    if Total < 5:
        print('\nAcabaram as cédulas desta máquina')
        break
    while True:
        print('\n' + 'BANCO PYTHON')
        while True:
            senha = str(input('Digite a senha de 4 dígitos: ')).strip()
            if len(senha) == 4:
                break
            print('Senha incorreta')
        valor = str(input('\nMínimo: R$ 5,00.\nValor para sacar(Não é possível sacar moedas): R$ ')).strip()


        if valor.count(',') >= 1:
            print('Digite o valor sem vírgula ou ponto, por favor.')
        elif valor.count('.') >= 1:
            print('Digite o valor sem vírgula ou ponto, por favor.')
        elif int(valor) < 5:
            print('O mínimo para saque é R$ 5,00.')
        else:
            if int(valor) <= Total:
                print('Este valor está disponível para saque nesta máquina.')
                break
            else:
                print('Este valor não está disponível para saque nesta máquina.')

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


