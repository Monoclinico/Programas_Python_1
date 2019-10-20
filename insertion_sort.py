#algoritmo de insertion sort

def insertion_sort(l):
    for i in range(1,len(l)):
        j=i-1
        key=l[i] 
        while (l[j]>key) and (j>=0):
            l[j+1]=l[j]
            j-=1
        l[j+1]=key
    return l

lista = []
print("Entre com 10 numeros reais e tenha eles organizados em ordem crescente")

for n in range(0,10):
  while True:
    try:
      elemento = float(input("Digite o numero: "))
      break
    except:
      continue
  lista.append(elemento)

lista = insertion_sort(lista)
print(lista)