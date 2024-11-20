def F(n):
    if (n < 3):
        return n-1
    else:
        return (F(n-1) + F(n-2))


Minimo = 5
Maximo = 20
entradas = range(Minimo,Maximo)
tempos = []
import timeit, functools
for n in entradas:
  print(f"Posicao {n} tem o valor {F(n)}")
  t = timeit.Timer(functools.partial(F, n))
  tempos.append(t.timeit(5))  # Armazena o tempo

# Criar o gráfico
import matplotlib.pyplot as plt
entradas = range(Minimo,Maximo)
plt.plot(entradas, tempos)
plt.title("Tempo de execução da função 'Fibonacci' em função de n")
plt.xlabel("Valor de n")
plt.ylabel("Tempo de execução (segundos)")
plt.grid(True)
plt.show()