def insercao(a):
    n = len(a)
    for i in range(1,n):
      x = a[i]
      j = i - 1
      a[0] = x
      while (x < a[j]):
         a[j+1] = a[j]
         j = j - 1
      a[j] = x

from array import array
Valores = array('i')
import random
for y in range(0,10):
  Valores.append(random.randint(1, 100))

print(Valores)
insercao(Valores)
print(Valores)


