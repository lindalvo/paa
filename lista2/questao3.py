def proc(n):
    if (n <= 1):
        return 2
    else:
        return (proc(n/2) + proc(n/2))

resultado = proc(4)
print(f"Resultado: {resultado}")
