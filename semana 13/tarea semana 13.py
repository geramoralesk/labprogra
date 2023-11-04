import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def ObtenerPerimetro(self):
        return 2 * math.pi * self.radio

    def ObtenerArea(self):
        return math.pi * self.radio ** 2

    def ObtenerVolumen(self):
        return (4/3) * math.pi * self.radio ** 3

def crear_circulo():
    radio = float(input("Ingresa el radio del círculo: "))
    return Circulo(radio)

num_circulos = int(input("Cuántos círculos deseas crear? "))

circulos = []

for i in range(num_circulos):
    circulo = crear_circulo()
    circulos.append(circulo)

for i, circulo in enumerate(circulos, start=1):
    print(f"\nCírculo {i}:")
    print(f"Radio: {circulo.radio}")
    print(f"Perímetro: {circulo.ObtenerPerimetro():.2f}")
    print(f"Área: {circulo.ObtenerArea():.2f}")
    print(f"Volumen: {circulo.ObtenerVolumen():.2f}")
