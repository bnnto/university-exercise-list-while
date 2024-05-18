d = {}
h_m_A = None
a_MAX = -1
m_m_G = None
p_MAX = -1
for i in range(2):
    nome = input("Digite o seu nome: ")
    sexo = input(f"{nome}, digite o seu sexo (M ou F): ")
    idade = int(input(f"{nome}, digite a sua idade: "))
    altura = float(input(f"{nome}, digite a sua altura: "))
    peso = float(input(f"{nome}, digite o seu peso: "))
    d[nome] = sexo, idade, altura, peso
menores = [nome for nome, (sexo, idade, _, _) in d.items() if sexo == "F" and idade < 18]
h_p_i = [nome for nome, (sexo, idade, _, peso) in d.items() if sexo == "M" and idade > 50 and peso > 90]
a_H = [altura for nome, (sexo, _, altura, _) in d.items() if sexo == "M"]
p_M = [peso for nome, (sexo, _, _, peso) in d.items() if sexo == "F"]
for nome, (sexo, _, altura, _) in d.items():
    if sexo == "M" and altura > a_MAX:
        h_m_A = nome
        a_MAX = altura
for nome, (sexo, _, _, peso) in d.items():
    if sexo == "F" and peso > p_MAX:
        m_m_G = nome
        p_MAX = peso
if p_M:
    m_p_M = sum(p_M) / len(p_M)
    print(f"\nA média do peso das mulheres é: {m_p_M:.2f} Kg.")
else:
    print("Não há mulheres para calcular a média do peso.")
if a_H:
    m_a_H = sum(a_H) / len(a_H)
    print(f"A média da altura dos homens é: {m_a_H:.2f} cm.")
else:
    print("Não há homens para calcular a média da altura.")
if m_m_G:
    print(f"A mulher mais gorda é: {m_m_G}")
else:
    print("Não há mulheres para determinar a mais gorda.")
if h_m_A:
    print(f"O homem mais alto é: {h_m_A}")
else:
    print("Não há homens para determinar o mais alto.")
if h_p_i:
    print("Esses homens tem peso maior que 90 e idade maior que 50: ")
    for nome in h_p_i:
        print(nome, end=" ")
else:
    print("Nenhum homem tem peso maior que 90 e idade maior que 50.")
if menores:
    print("Essas mulheres são menores de idade: ")
    for nome in menores:
        print(nome, end=" ")
else:
    print("Nenhuma mulher é menor de idade.")