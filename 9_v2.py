a = 1
b = 1
contador = 2
somaT = a + b
print(f"Esses são os 100 primeiros termos da série de Fibonacci: {a} {b}", end=" ")

while contador < 100:
    prox_n = a + b
    somaT += prox_n
    print(prox_n, end=" ")
    a = b
    b = prox_n
    contador += 1
print(f"\nEsta é a soma de todos esses 100 primeiros termos: {somaT}")