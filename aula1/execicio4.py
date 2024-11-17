from array import array

def Lista_Primo (n):
  A = array('i')
  for i in range(2,n+1):
    j = 2
    while ((j < i) & ((i % j) != 0)):
        j=j+1
    if (j==i):
        A.append(j)
  return A

Minimo = 10
Maximo = 501
entradas = range(2,Maximo)
tempos = []
import timeit, functools
for n in entradas:
  t = timeit.Timer(functools.partial(Lista_Primo, n) )
  if (n >= Minimo):
    tempos.append(t.timeit(10))  # Armazena o tempo

# Criar o gráfico
import matplotlib.pyplot as plt
entradas = range(Minimo,Maximo)
plt.plot(entradas, tempos)
plt.title("Tempo de execução da função 'Lista Primos' em função de n")
plt.xlabel("Valor de n")
plt.ylabel("Tempo de execução (segundos)")
plt.grid(True)
plt.show()