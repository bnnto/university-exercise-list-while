nA = int(input("Digite o número de alunos: "))
i = 0
tN = []
while nA > i:
    notas = float(input("Digite a nota de cada aluno: "))
    tN.append(notas)
    i += 1
print(f"Média das notas dos alunos na primeira prova do semestre: {sum(tN) / nA:.1f}")