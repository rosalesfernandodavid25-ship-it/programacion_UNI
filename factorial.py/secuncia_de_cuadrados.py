n = int(input("numero positivo: "))
i = 1
while True:
    print(i * 2)
    i += 1
    if i > n:
        break
print("secuencia de cuadrados hasta",n)