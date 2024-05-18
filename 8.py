N = int(input("Digite quantos números você vai querer verificar: "))
i = 0
while i < N:
    numero = int(input("Digite um número: "))
    if 0 <= numero < 25:
        print("O número está no intervalo [0,25].")
    elif 25 <= numero < 50:
        print("O número está no intervalo (25,50].")
    elif 50 <= numero < 75:
        print("O número está no intervalo (50,75].")
    elif 75 <= numero <= 100:
        print("O número está no intervalo (75,100].")
    else:
        print("O número está fora dos intervalos possíveis.")
    i += 1