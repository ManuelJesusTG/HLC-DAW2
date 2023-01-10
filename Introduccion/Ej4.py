# Le pedimos al usuario el numero decimal que queremos pasar a octal
num = int(input("Introduce un numero"))

# Creamos una variable para guardar el numero octal donde lo pasaremos a octal con el metodo oct()[2:]
octal = oct(num)[2:]

# Sacamos el resultado por pantala
print("El número octal del número decimal "+str(num)+" es "+octal)