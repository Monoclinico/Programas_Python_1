
# Mostra quanto tempo levara para a proxima data de aniversario especificada

import time
from datetime import date
today = date.today()

mes = int(input("Informe o mes de aniversario[1-12]: "))
dia = int(input("Informe o dia de aniversario[1-31]: "))

my_birthday = date(today.year, mes, dia)
if my_birthday < today:
  my_birthday = my_birthday.replace(year=today.year + 1)
print("Seu aniversario sera em: "+str(my_birthday))

time_to_birthday = abs(my_birthday - today)
print("Faltam: "+str(time_to_birthday.days)+" dias para seu aniversario.")
