while True:
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")
    
    opcion = input("Ingrese el número de opción que desea ejecutar: ")

    if opcion == "1":
        numero = int(input("Ingrese un número: "))
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        print(f"{numero} =", " * ".join(map(str, range(numero, 0, -1))), "=", resultado)
    elif opcion == "2":
        numero = int(input("Ingrese un número para generar la secuencia de Fibonacci: "))
        fib_sequence = [0, 1]
        while len(fib_sequence) < numero:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        print("Fibonacci(", numero, ") =", ", ".join(map(str, fib_sequence)))
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")
