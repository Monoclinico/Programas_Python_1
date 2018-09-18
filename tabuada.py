while True:
    print("+"*40)
    num = int(input('CRIAR A TABUADA DO: '))
    if num < 0:
        break
    for tab in range(0, 11):
        print('{:2} x {} = {}'.format(tab, num, num * tab))