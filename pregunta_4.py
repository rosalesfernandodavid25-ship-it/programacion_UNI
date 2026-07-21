#programar para calcular salario neto
salario_bruto = float(input("Ingrese su salario bruto: "))
porcentaje = float(input("% inpuestos: "))
deducciones = float(input("Ingrese el monto de deducciones: "))
inpuestos = salario_bruto * (porcentaje / 100)  
salario_neto = salario_bruto - inpuestos - deducciones
print("Su salario neto :", salario_neto)
