#conding:utf-8

#função que retorna o fatorial de um número (n), utilizando o método de recursão.
#limite de repetições recursivas configurada para fazer essa função foi de 1000.
def fatorial(n): 
    """Retorna o fatorial de um número natural."""
    assert ((n>=0) and (float(n).is_integer())),'Só números naturais!' #exceção é levantada se n for do tipo ponto flutuante ou negativo.
    if n == 1 or n == 0: return 1 # define a condição de parada da recursão, que é quando n for igual a 1 ou 0. 
    return n * fatorial(n-1) #retorna n * (n-1) * (n-2)... até 1 ou 0.

#exemplos
fatorial(0)#retorna 1
fatorial(1)#retorna 1
fatorial(5)#retorna 120
fatorial(1000)#pode retornar RecursionError