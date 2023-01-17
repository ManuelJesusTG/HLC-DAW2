# Le pedimos las 2 cadenas al usuario

Cadena1 = input(str("Introduce la primera cadena"))
Cadena2 = input(str("Introduce la segunda cadena"))

# Calculamos la mitad de la cadena

Mitad = int(len(Cadena1)/2)


# Creamos una variable donde almacenar el resultado
Resultado = ""

# Hacemos un bucle para recorrer la primera cadena y introducir la segunda cadena cuando llegue a la mitad

for i,j in enumerate(Cadena1):
    if i == Mitad:
        Resultado = Resultado+Cadena2
    Resultado = Resultado+j

# Sacamos por pantalla el resultado
print(Resultado)