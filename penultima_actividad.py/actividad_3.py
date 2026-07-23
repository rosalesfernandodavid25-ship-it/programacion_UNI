def es_palindromo(texto):
    texto = texto.lower()
    limpio = ""
    for caracter in texto:
        if caracter != " ":
            limpio += caracter
    return limpio == limpio[::-1], limpio

entrada = input ("ingrese una frase: ")
resultado, cadena_limpia = es_palindromo(entrada)
if  resultado:
    print("es un palindromo")
else:
    print("no es palindromo")
print("longitud de la cadena limpia:", len(cadena_limpia))