i = 0
while i < 500:
    salario = float(input("Digite seu salário: "))

    if salario <= 1600.00:
        print("Isento")
    elif salario <= 3000.00:
        salario = salario - 1600.00
        imposto = 0.1 * salario
        print(f"O imposto que você vai pagar é de R$ {imposto:.2f}")
    elif salario <= 7000.00:
        salario = salario - 1600.00
        imposto = (salario - 1400) * 0.15 + 1400 * 0.1
        print(f"O imposto que você vai pagar é de R$ {imposto:.2f}")
    elif salario > 7000.00:
        salario = salario - 1600.00
        imposto = (salario - 5400) * 0.20 + 4000 * 0.15 + 1400 * 0.1
        print(f"O imposto que você vai pagar é de R$ {imposto:.2f}")
    i += 1