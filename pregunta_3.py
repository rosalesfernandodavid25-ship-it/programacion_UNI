#programa para calcular el IMC
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print("Su Índice de Masa Corporal (IMC) es:", imc)
