cultura = 0
sbt = 0
globo = 0
record = 0
mtv = 0
maior_A = 0
menor_A = 999999999999
maior_AA = ""
menor_AA = ""
while True:
    T = input("Digite (comecar) para começar as entrevistas e (fim) para terminar as entrevistas. ")
    if T.lower() == 'comecar':
        tTV = input("A TV está ligada? (sim ou nao) ")
        if tTV.lower() == 'sim':
            canal = input("Qual canal está sendo assistido (Cultura, SBT, Globo, Record e MTV): ")
            numero_p = int(input("Qual a quantidade de pessoas assistindo: "))
            if canal == 'cultura':
                cultura += numero_p
            elif canal == 'sbt':
                sbt += numero_p
            elif canal == 'globo':
                globo += numero_p
            elif canal == 'record':
                record += numero_p
            elif canal == 'mtv':
                mtv += numero_p

            tot_audi = cultura + sbt + globo + record + mtv

            if cultura > maior_A:
                maior_A = cultura
                maior_AA = "Cultura"
            if sbt > maior_A:
                maior_A = sbt
                maior_AA = "SBT"
            if globo > maior_A:
                maior_A = globo
                maior_AA = "Globo"
            if record > maior_A:
                maior_A = record
                maior_AA = "Record"
            if mtv > maior_A:
                maior_A = mtv
                maior_AA = "MTV"
            if cultura < menor_A and cultura > 0:
                menor_A = cultura
                menor_AA = "Cultura"
            if sbt < menor_A and sbt > 0:
                menor_A = sbt
                menor_AA = "SBT"
            if globo < menor_A and globo > 0:
                menor_A = globo
                menor_AA = "Globo"
            if record < menor_A and record > 0:
                menor_A = record
                menor_AA = "Record"
            if mtv < menor_A and mtv > 0:
                menor_A = mtv
                menor_AA = "MTV"

    elif T.lower() == 'fim':
            if tot_audi > 0:
                print(f"A Cultura tem {(cultura / tot_audi) * 100:.2f}% de audiência")
                print(f"A SBT tem {(sbt / tot_audi) * 100:.2f}% de audiência")
                print(f"A Globo tem {(globo / tot_audi) * 100:.2f}% de audiência")
                print(f"A Record tem {(record / tot_audi) * 100:.2f}% de audiência")
                print(f"A MTV tem {(mtv / tot_audi) * 100:.2f}% de audiência")
                print(f"{maior_AA} tem a maior audiência.")
                print(f"{menor_AA} tem a menor audiência.")
            else:
                print("Nenhuma audiência foi registrada.")
            break