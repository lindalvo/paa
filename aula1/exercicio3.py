def Primo (n):
  j = 2
  while ((j < n) & ((n % j) != 0) ):
    j=j+1
  if (j == n):
    print(f"{n} e primo")
  else:
    print(f"{n} nao e primo")

Minimo = 5
Maximo = 3001
entradas = range(2,Maximo)
tempos = []
import timeit, functools
for n in entradas:
  t = timeit.Timer(functools.partial(Primo, n) )
  if (n >= Minimo):
    tempos.append(t.timeit(5))  # Armazena o tempo

# Criar o gráfico
import matplotlib.pyplot as plt
entradas = range(Minimo,Maximo)
plt.plot(entradas, tempos)
plt.title("Tempo de execução da função 'Primos' em função de n")
plt.xlabel("Valor de n")
plt.ylabel("Tempo de execução (segundos)")
plt.grid(True)
plt.show()