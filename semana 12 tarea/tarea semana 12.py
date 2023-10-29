class Calculadora:
    def __init__(self):
        self.num1 = 0.0
        self.num2 = 0.0

    def insertar_primer_numero(self, numero):
        self.num1 = numero

    def insertar_segundo_numero(self, numero):
        self.num2 = numero

    def obtener_suma(self):
        return self.num1 + self.num2

    def obtener_resta(self):
        return self.num1 - self.num2

    def obtener_multiplicacion(self):
        return self.num1 * self.num2

    def obtener_division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No es posible dividir por cero."

# Crear una instancia de la clase Calculadora
calculadora = Calculadora()

while True:
    print("Menú:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        calculadora.insertar_primer_numero(num1)
        calculadora.insertar_segundo_numero(num2)
        print("La suma es:", calculadora.obtener_suma())
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        calculadora.insertar_primer_numero(num1)
        calculadora.insertar_segundo_numero(num2)
        print("La resta es:", calculadora.obtener_resta())
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        calculadora.insertar_primer_numero(num1)
        calculadora.insertar_segundo_numero(num2)
        print("La multiplicación es:", calculadora.obtener_multiplicacion())
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        calculadora.insertar_primer_numero(num1)
        calculadora.insertar_segundo_numero(num2)
        resultado = calculadora.obtener_division()
        if isinstance(resultado, float):
            print("La división es:", resultado)
        else:
            print(resultado)
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
