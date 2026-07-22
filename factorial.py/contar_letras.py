palabra = input ("ingresa una palabra: ").lower()
contador = 0
for letras in palabra:
    if letras == 'a':
        contador += 1
print ("la palabra 'a' aparece", contador, "veces")