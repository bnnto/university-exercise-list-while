n_criancas_n = int(input("Digite o número de crianças nascidas no período: "))
mor_T = 0
mor_24 = 0
mor_F = 0
sexo = input("Digite o sexo da criança morta (M ou F), ou 'vazio' para parar: ")
while sexo != "vazio":
    n_meses = int(input("Digite o número de meses de vida da criança morta: "))
    if n_meses <= 24:
        mor_24 += 1
    if sexo == "F":
        mor_F += 1
    mor_T += 1
    sexo = input("Digite o sexo da criança morta (M ou F), ou 'vazio' para parar: ")
print(f"A porcentagem de crianças mortas no período é de {(mor_T / n_criancas_n) * 100:.2f} %")
print(f"A porcentagem de crianças do sexo feminino mortas no período é de {(mor_F / n_criancas_n) * 100:.2f} %")
print(f"A porcentagem de crianças que viveram 24 meses ou menos no período é de {(mor_24 / n_criancas_n) * 100:.2f} %")