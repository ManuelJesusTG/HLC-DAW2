# Usamos las variables que nos da el ejercicio
totalMoney = 1000
quantity = 3
price = 450

# Creamos un texto similar al del ejercicio dejando el hueco para introducir posteriormente nuestras variable
Salida = "Tengo {} euros para comprar {} tarjetas gráficas por {} dólares."

# Sacamos el texto anterior juntando con el metodo str.format() las variables que nos proporciona el ejercicio
print(Salida.format(totalMoney,quantity,price))