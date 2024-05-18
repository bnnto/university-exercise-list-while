print("Os clientes que comprarem mais de 200 açaís, terão desconto de 15%.")
mt = {}
qAA = []
for i in range(300):
    nome = input("Digite o seu nome: ")
    q_acai = int(input(f"{nome}, digite a quantidade de açaís que você comprou: "))
    mt[nome] = q_acai
    qAA.append(q_acai)
print(f"\nA quantidade de açaís comprados foi de {sum(qAA)} açaís.")
print(f"A média de açaís comprados foi de {int(sum(qAA) / 3)} açaís.")
print(f"{max(mt, key=mt.get)} comprou mais açaí.")
if q_acai > 100:
    print("Os seguintes clientes compraram mais de 100 açaís: ")
    [print(nome, end=" ") for nome, q_acai in mt.items() if q_acai > 100]
else:
    print("Nenhuma pessoa comprou mais de 100 açaís.")