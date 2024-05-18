d = {}
v = []
while True:
    T = input("Digite (comecar) para começar as entrevistas e (fim) para terminar as entrevistas. ")
    if T == 'comecar':
        tTV = input("A TV está ligada? (sim ou nao) ")
        if tTV == 'sim':
            canal = input("Qual canal está sendo assistido (Cultura, SBT, Globo, Record e MTV): ")
            numero_p = int(input("Qual a quantidade de pessoas assistindo: "))
            d[canal] = d.get(canal, 0) + numero_p
            v.append(numero_p)
    elif T == 'fim':
        total_pessoas = sum(v)
        if total_pessoas > 0:
            for canal in ['Cultura', 'SBT', 'Globo', 'Record', 'MTV']:
                audiencia = (d.get(canal, 0) / total_pessoas) * 100
                print(f"A {canal} tem {audiencia:.2f}% de audiência")
            print(f"{max(d, key=d.get)} tem a maior audiência.")
            print(f"{min(d, key=d.get)} tem a menor audiência.")
        else:
            print("Nenhuma audiência foi registrada.")
        break