# Solicitar una cadena al usuario
cadena = input("Ingrese una cadena de caracteres: ")

# Inicializar contadores
contador_0 = 0
contador_1 = 0
contador_otros = 0

# Recorrer la cadena
for caracter in cadena:
    if caracter == '0':
        contador_0 += 1
    elif caracter == '1':
        contador_1 += 1
    else:
        contador_otros += 1

# Mostrar los resultados
print("Cantidad 0:", contador_0)
print("Cantidad 1:", contador_1)
print("Otros caracteres:", contador_otros)
