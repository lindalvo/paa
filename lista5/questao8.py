import time
import matplotlib.pyplot as plt
import random
from array import array

class AlgoritmosOrdenacao:
    def __init__(self):
        self.comparacoes = 0
        self.trocas = 0
        self.tempo_execucao = 0

    def zera_contadores(self):
        self.comparacoes = 0
        self.trocas = 0
        self.tempo_execucao = 0

    def quicksort(self, arr):
        self.zera_contadores()
        tempo_inicio = time.time()

        def _quicksort(arr, low, high):
            if low < high:
                indice_pivo = self.partition(arr, low, high)
                _quicksort(arr, low, indice_pivo - 1)
                _quicksort(arr, indice_pivo + 1, high)

        _quicksort(arr, 0, len(arr) - 1)
        self.tempo_execucao = time.time() - tempo_inicio

    def partition(self, arr, low, high):
        pivo = arr[high]
        i = low - 1
        for j in range(low, high):
            self.comparacoes += 1
            if arr[j] < pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.trocas += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.trocas += 1
        return i + 1

    def heapsort(self, arr):
        self.zera_contadores()
        tempo_inicio = time.time()

        def heapify(arr, n, i):
            maior = i
            esquerda = 2 * i + 1
            direita = 2 * i + 2

            if esquerda < n:
                self.comparacoes += 1
                if arr[esquerda] > arr[maior]:
                    maior = esquerda

            if direita < n:
                self.comparacoes += 1
                if arr[direita] > arr[maior]:
                    maior = direita

            if maior != i:
                arr[i], arr[maior] = arr[maior], arr[i]
                self.trocas += 1
                heapify(arr, n, maior)

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.trocas += 1
            heapify(arr, i, 0)
        
        self.tempo_execucao = time.time() - tempo_inicio

    def shellsort(self, arr):
        self.zera_contadores()
        tempo_inicio = time.time()
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap:
                    self.comparacoes += 1
                    if arr[j - gap] > temp:
                        arr[j] = arr[j - gap]
                        self.trocas += 1
                        j -= gap
                    else:
                        break
                arr[j] = temp
            gap //= 2
        
        self.tempo_execucao = time.time() - tempo_inicio

# Teste dos algoritmos
if __name__ == "__main__":
    Minimo = 10
    Maximo = 10000
    entradas = range(Minimo,Maximo,10)

    #Coletando os tempos
    temposQuick = []
    temposHeap = []
    temposShell = []

    trocasQuick = []
    trocasHeap = []
    trocasShell = []

    comparacoesQuick = []
    comparacoesHeap = []
    comparacoesShell = []

    import timeit, functools
    for x in entradas:
    #gerando os Arrays desordenados com valores de 1 até 100
        print("Tamanho do array:", x)
        valores = array('i')
        for y in range(1,x+1):
            valores.append(random.randint(1, 100))

        algoritmos = AlgoritmosOrdenacao()

        #print("Array desordenado:", valores)

        # Quicksort
        quicksort_array = valores.__copy__()
        algoritmos.quicksort(quicksort_array)
        #print("Ordenado pelo Quicksort:", quicksort_array)
        #print(f"comparacoes: {algoritmos.comparacoes}, trocas: {algoritmos.trocas}, Tempo de execução: {algoritmos.tempo_execucao}")
        temposQuick.append(algoritmos.tempo_execucao)
        trocasQuick.append(algoritmos.trocas)
        comparacoesQuick.append(algoritmos.comparacoes)
        # Heapsort
        heapsort_array = valores.__copy__()
        algoritmos.heapsort(heapsort_array)
        #print("Ordenado pelo Heapsort:", heapsort_array)
        #print(f"comparacoes: {algoritmos.comparacoes}, trocas: {algoritmos.trocas}, Tempo de execução: {algoritmos.tempo_execucao}")
        temposHeap.append(algoritmos.tempo_execucao)
        trocasHeap.append(algoritmos.trocas)
        comparacoesHeap.append(algoritmos.comparacoes)
        # Shellsort
        shellsort_array = valores.__copy__()
        algoritmos.shellsort(shellsort_array)
        #print("Ordenador pelo Shellsort:", shellsort_array)
        #print(f"comparacoes: {algoritmos.comparacoes}, trocas: {algoritmos.trocas}, Tempo de execução: {algoritmos.tempo_execucao}")
        temposShell.append(algoritmos.tempo_execucao)
        trocasShell.append(algoritmos.trocas)
        comparacoesShell.append(algoritmos.comparacoes)

    #Mostrando o gráfico
    plt.plot(entradas, temposQuick, label="QuickSort")
    plt.plot(entradas, temposHeap, label="HeapSort")
    plt.plot(entradas, temposShell, label="ShellSort")
    plt.title("Tempo de execução de algoritmos de Ordenação em função da quantidade de Elementos no array")
    plt.xlabel("Quantidade de Elementos no Vetor")
    plt.ylabel("Tempo de execução (segundos)")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    plt.plot(entradas, trocasQuick, label="QuickSort")
    plt.plot(entradas, trocasHeap, label="HeapSort")
    plt.plot(entradas, trocasShell, label="ShellSort")
    plt.title("Trocas de elementos nos algoritmos de Ordenação em função da quantidade de Elementos no array")
    plt.xlabel("Quantidade de Elementos no Vetor")
    plt.ylabel("Quantidade de trocas")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.plot(entradas, comparacoesQuick, label="QuickSort")
    plt.plot(entradas, comparacoesHeap, label="HeapSort")
    plt.plot(entradas, comparacoesShell, label="ShellSort")
    plt.title("Comparações efetuadas nos algoritmos de Ordenação em função da quantidade de Elementos no array")
    plt.xlabel("Quantidade de Elementos no Vetor")
    plt.ylabel("Quantidade de comparações")
    plt.legend()
    plt.grid(True)
    plt.show()
