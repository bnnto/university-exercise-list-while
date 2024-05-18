# Utilize 0 para parar de receber salário e mostrar e média em seguida.
vS = []
i = 0
while True:
    salario = float(input("Digite o seu salário: "))
    vS.append(salario)
    i += 1
    if salario == 0:
        media = sum(vS) / (i - 1)
        print(f"Média dos salários de certa cidade é de: R$ {media:.2f}")
        break