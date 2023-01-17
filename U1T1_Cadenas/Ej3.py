# Le pedimos las 2 cadenas al usuario

Cadena1 = input(str("Introduce la primera cadena"))
Cadena2 = input(str("Introduce la segunda cadena"))

# Sacamos la posicion de la mitad de cada una de las cadenas
Mitad1 = int(len(Cadena1)/2)
Mitad2 = int(len(Cadena2)/2)

# Concatenamos el resultado para darle el formato que nos perdia el ejercicio
Resultado = Cadena1[0]+Cadena2[0]+Cadena1[Mitad1]+Cadena2[Mitad2]+Cadena1[int(len(Cadena1))-1]+Cadena2[int(len(Cadena2))-1]

# Lo sacamos por pantalla
print(Resultado)