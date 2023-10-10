def decimal_a_hexadecimal(numero):
    return hex(numero)
numero_decimal = int(input("Ingrese un número decimal: "))
numero_hexadecimal = decimal_a_hexadecimal(numero_decimal)
print("El valor en hexadecimal es: " + numero_hexadecimal)