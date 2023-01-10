# Le pedimos al usuario los valores para operar con el ejercicio
num1 = int(input("Introduce el primer numero"))
num2 = int(input("Introduce el segundo numero"))

# Calculamos su suma
suma = num1+num2

# Calulamos su producto
mult = num1*num2

# Usamos if y else para sacar una cosa o otra dependiendo de el producto de los valores introducidos
if mult > 1000:
    print("La multiplicacion de ambos numeros es "+str(mult))
else:
    print("La suma de ambos numeros es "+str(suma))