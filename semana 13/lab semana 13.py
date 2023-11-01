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

# Ejemplo de uso:
radio_circulo = 5.0
mi_circulo = Circulo(radio_circulo)

print(f"Radio del círculo: {radio_circulo}")
print(f"Perímetro del círculo: {mi_circulo.ObtenerPerimetro():.2f}")
print(f"Área del círculo: {mi_circulo.ObtenerArea():.2f}")
print(f"Volumen de la esfera con este radio: {mi_circulo.ObtenerVolumen():.2f}")
