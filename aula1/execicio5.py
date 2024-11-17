from array import array

def Selecao (A):
  n = len(A)
  for i in range(0,n-1):
    minimo = i
    for j in range(i+1,n):
      if A[j] < A[minimo]:
        minimo = j
    temp = A[i]
    A[i] = A[minimo]
    A[minimo] = temp
  return A
    
def Bolha (A):
  n = len(A)
  for i in range(0,n-1):
    for j in range(0,n-i-1):
      if A[j] > A[j+1]:
        temp = A[j]
        A[j] = A[j+1]
        A[j+1] = temp
  return A

def Insercao(A):
  n = len(A)
  for j in range(1,n):
    chave = A[j]
    i = j-1
    while ((i>=0) & (A[i]>chave)):
      A[i+1] = A[i]
      i=i-1
    A[i+1]=chave
  return A

Minimo = 10
Maximo = 1001
entradas = range(Minimo,Maximo)
import random

#Coletando os tempos
temposInsercao = []
temposBolha = []
temposSelecao = []

import timeit, functools
for x in entradas:
  #gerando os Arrays desordenados com valores de 1 até 100
  Valores = array('i')
  for y in range(1,x+1):
    Valores.append(random.randint(1, 100))
  t = timeit.Timer(functools.partial(Insercao, Valores))
  temposInsercao.append(t.timeit(5))
  t = timeit.Timer(functools.partial(Bolha, Valores))
  temposBolha.append(t.timeit(5))
  t = timeit.Timer(functools.partial(Selecao, Valores))
  temposSelecao.append(t.timeit(5))

#Mostrando o gráfico
import matplotlib.pyplot as plt
plt.plot(entradas, temposBolha, label="Bolha")
plt.plot(entradas, temposSelecao, label="Selecao")
plt.plot(entradas, temposInsercao, label="Insercao")
plt.title("Tempo de execução de algoritmos de Ordenação em função da quantidade de Elementos no array")
plt.xlabel("Quantidade de Elementos no Vetor")
plt.ylabel("Tempo de execução (segundos)")
plt.legend()
plt.grid(True)
plt.show()