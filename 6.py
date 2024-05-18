i = 0
lA = []
while i < 3:
    altura = float(input("Digite a altura da candidata (em cm): "))
    lA.append(altura)
    i += 1
lA.sort(reverse=True)
maior_a = lA[0]
segunda_maior_a = lA[1]
print(f"A candidata mais alta tem altura de: {maior_a:.2f} cm")
print(f"A segunda candidata mais alta tem altura de: {segunda_maior_a:.2f} cm")
