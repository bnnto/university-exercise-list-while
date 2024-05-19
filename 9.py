fs = []

fs.append(1)
fs.append(1)
for x in range(2, 100):
    prox_n = fs[-1] + fs[-2]
    fs.append(prox_n)
    somaT = sum(fs)

print("Esses são os 100 primeiros termos da série de Fibonacci:", " ".join(map(str, fs)))
print(f"Esta é a soma de todos esses 100 primeiros termos: {somaT}")