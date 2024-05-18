N = int(input("Digite um número para que seja calculado seu fatorial: "))
produto = 1
print(f"{N}! = ", end="")
for i in range(N, 0, -1):
    produto *= i
    print(i, end="")
    if i != 1:
        print(" * ", end="")
print(" =", produto)
