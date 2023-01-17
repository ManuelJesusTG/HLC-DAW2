# Le pedimos a los usuarios la cadena con una longitud mayor a 7

Cadena = str(input("Introduce una cadena con una longitud igual o mayor a 7 y impar"))

# Guardamos en una variable la mitad de la longitud de la cadena y una variable resultado donde iremos concatenando un resultado

MitadCad = int(len(Cadena)/2)-1
Resultado = ""

# Comprobamos que la longitud de la cadena es mayor a 7 

if len(Cadena) < 7 or len(Cadena)%2 == 0:
    print("La cadena introducida es menor a 7 o es par")

# Hacemos un bucle donde recorreremos toda la cadena con sus posiciones y si estan en la posicion que nosotros queremos, guardamosel valor en "resultado"
else:
    
    for i , j in enumerate(Cadena):
        if i == MitadCad or i == MitadCad+1 or i == MitadCad +2:
            Resultado = Resultado+j
            

# Sacamos por pantalla el resultado final

print(Resultado)