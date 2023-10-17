# Crear una lista para almacenar la información de las dos líneas de producción
lineas_de_produccion = []

# Pedir información para la primera línea
numero_linea1 = 1
precio_metro_cuadrado1 = float(input("Precio de venta por metro cuadrado en la línea 1: "))
metros_vendidos1 = float(input("Cantidad de metros cuadrados vendidos al mes en la línea 1: "))
num_empleados1 = int(input("Número de empleados en la línea 1: "))

# Crear una lista para almacenar la información de empleados de la línea 1
empleados1 = []
for i in range(num_empleados1):
    print("Costo de hora del empleado "+ str(i + 1) + " en la línea 1: ")
    costo_hora = float(input())
    print("Cantidad de horas trabajadas por el empleado " + str(i+1)+ " en la línea 1: ")
    horas_trabajadas = float(input())
    empleados1.append((costo_hora, horas_trabajadas))

# Pedir información para la segunda línea
numero_linea2 = 2
precio_metro_cuadrado2 = float(input("Precio de venta por metro cuadrado en la línea 2: "))
metros_vendidos2 = float(input("Cantidad de metros cuadrados vendidos al mes en la línea 2: "))
num_empleados2 = int(input("Número de empleados en la línea 2: "))

# Crear una lista para almacenar la información de empleados de la línea 2
empleados2 = []
for i in range(num_empleados2):
    print("Costo de hora del empleado "+ str(i + 1) + " en la línea 1: ")
    costo_hora = float(input())
    print("Cantidad de horas trabajadas por el empleado " + str(i+1)+ " en la línea 1: ")
    horas_trabajadas = float(input())
    empleados2.append((costo_hora, horas_trabajadas))

# Almacenar la información en la lista de líneas de producción
linea1 = {
    "numero": numero_linea1,
    "precio_metro_cuadrado": precio_metro_cuadrado1,
    "metros_vendidos": metros_vendidos1,
    "empleados": empleados1,
}
linea2 = {
    "numero": numero_linea2,
    "precio_metro_cuadrado": precio_metro_cuadrado2,
    "metros_vendidos": metros_vendidos2,
    "empleados": empleados2,
}
lineas_de_produccion.append(linea1)
lineas_de_produccion.append(linea2)

print()
# Mostrar todos los datos de cada línea
#linea 1
print("Datos para la línea 1")
print("Número de línea: 1")
print("Precio de venta por metro cuadrado: " +str(precio_metro_cuadrado1))
print("Cantidad de metros cuadrados vendidos al mes: " +str(metros_vendidos1))
print("Empleados:")
for i in range (num_empleados1):
    print("Empleado" + str(i + 1)+ ":")
    print("Costo de hora: " +str(empleados1[i][0]))
    print("Horas trabajadas: "+ str(empleados1[i][1]))
print()
#Calcular Ganancias linea 1
print("Calculos linea 1")
ganancia_total1=precio_metro_cuadrado1*metros_vendidos1
costo_total1=sum(empleados1[i][0]*empleados1[i][1] for i in range(num_empleados1))
ganancia_neta1=ganancia_total1-costo_total1
eficiencia1=ganancia_neta1/num_empleados1
print("ganancia total: "+str(ganancia_neta1))
print("costo total: " + str(costo_total1))
print("Ganancia Neta: "+str(ganancia_neta1))
print("Eficiencia: " + str(eficiencia1))
print()
#mostrar datos linea 2
print("Datos para la línea 2")
print("Número de línea: 2")
print("Precio de venta por metro cuadrado: " +str(precio_metro_cuadrado2))
print("Cantidad de metros cuadrados vendidos al mes: " +str(metros_vendidos2))
print("Empleados:")
for i in range (num_empleados2):
    print("Empleado" + str(i + 1)+ ":")
    print("Costo de hora: " +str(empleados2[i][0]))
    print("Horas trabajadas: "+ str(empleados2[i][1]))
print()
#Calculo de ganancia linea 2
print("Calculos linea 2")
ganancia_total2=precio_metro_cuadrado2*metros_vendidos2
costo_total2=sum(empleados2[i][0]*empleados2[i][1] for i in range(num_empleados2))
ganancia_neta2=ganancia_total2-costo_total2
eficiencia2=ganancia_neta2/num_empleados2
print("ganancia total: "+str(ganancia_neta2))
print("costo total: " + str(costo_total2))
print("Ganancia Neta: "+str(ganancia_neta2))
print("Eficiencia: " + str(eficiencia2))
print()
# Calcular las métricas para ambas líneas de producción


# Encontrar la línea con el mayor índice de eficiencia
if eficiencia1>eficiencia2:
    print("La linea 1 tuvo mayor indice de eficiencia con:"+str(eficiencia1))

else:
    print("La linea 2 tuvo mayor indice de eficiencia con:"+str(eficiencia2))
