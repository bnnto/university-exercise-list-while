M_altura = 0.0
S_altura = 0.0
for i in range(200):
    nome = input("Digite seu nome: ")
    altura = float(input(f"{nome}, digite sua altura (em cm): "))
    if altura > M_altura:
        S_altura = M_altura
        M_altura = altura
    elif altura > S_altura:
        S_altura = altura
print(f"A candidata mais alta tem altura de: {M_altura:.2f} cm")
print(f"A segunda candidata mais alta tem altura de: {S_altura:.2f} cm")