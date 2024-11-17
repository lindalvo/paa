import matplotlib.pyplot as plt
import pandas as pd
import time

def Soma_Quadrados_A (n):
  x=0
  for j in range(1,n+1):
       x=x+(j*j)
  return x

def Soma_Quadrados_B (n):
  x=n*(n+1)*((2*n)+1)
  x=x/6
  return int(x)

start_time = time.perf_counter()
resultado1 = Soma_Quadrados_A(7)
end_time = time.perf_counter()
execution_time1 = end_time - start_time

start_time = time.perf_counter()
resultado2 = Soma_Quadrados_B(7)
end_time = time.perf_counter()
execution_time2 = end_time - start_time

print(f"{resultado1} temp de execução: {execution_time1}")
print(f"{resultado2} temp de execução: {execution_time2}")