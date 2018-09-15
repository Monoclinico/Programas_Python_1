#!/usr/bin/python
#_*_coding:utf-8_*_
def fatorial(n):
    """Retorna o fatorial de um número natural."""
    assert ((n>=0) and (float(n).is_integer())),'Só números naturais!'
    if n == 1 or n == 0: return 1
    return n * fatorial(n-1)