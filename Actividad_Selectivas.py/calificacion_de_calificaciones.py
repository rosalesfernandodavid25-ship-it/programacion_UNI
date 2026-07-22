#calificacion de calificaciones
nota1 = float(input("Ingrese calificación:(0-100) "))
if nota1 >=  90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
else:
    letra = "F"
print(f"La letra correspondiente es: {letra}")