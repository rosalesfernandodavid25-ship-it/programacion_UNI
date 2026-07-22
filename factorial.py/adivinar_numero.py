import random
secreto = random.randint(1, 100)
while True:
    intentos = int(input("Adivina (1-100): "))
    if intentos < secreto:
        print("Demasiado bajo")
    elif intentos > secreto:
        print("Demasiado alto")
    else:
        print("¡correcto! Era", secreto)
        break
    print("juego terminado. El numero Era", secreto)