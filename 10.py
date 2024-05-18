v = []
v2 = []
v3 = []
n_criancas_n = int(input("Digite o número de crianças nascidas no período: "))

while True:
    sexo = input("Digite o sexo da criança morta (M ou F), ou 'vazio' para parar: ")
    if sexo == "vazio":
        print(f"A porcentagem de crianças mortas no período é de {(len(v3) / n_criancas_n) * 100:.2f} %")
        print(f"A porcentagem de crianças do sexo feminino mortas no período é de {(len(v2) / n_criancas_n) * 100:.2f} %")
        print(f"A porcentagem de crianças que viveram 24 meses ou menos no período é de {(len(v) / n_criancas_n) * 100:.2f} %")
        break
    else:
        n_meses = int(input("Digite o número de meses de vida da criança morta: "))
        if n_meses <= 24:
            v.append(n_meses)
        if sexo == "F":
            v2.append(n_meses)
        v3.append(n_meses)
