class Automovil:
    def __init__(self, modelo=0, precio=0.0, marca="", disponible=True, tipoCambioDolar=7.82, descuentoAplicado=0.0):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.disponible = disponible
        self.tipoCambioDolar = tipoCambioDolar
        self.descuentoAplicado = descuentoAplicado

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def MostrarInformacion(self):
        precio_en_dolares = self.precio / self.tipoCambioDolar
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares: ${precio_en_dolares}. {self.MostrarDisponibilidad()}"

    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        self.DefinirPrecio(self.precio - miDescuento)

automovil1 = Automovil()
automovil1.DefinirModelo(2024)
automovil1.DefinirPrecio(490059.33)
automovil1.DefinirMarca("Mercedes-Benz GLE")
automovil1.DefinirTipoCambio(7.82)
automovil1.CambiarDisponibilidad()
automovil1.AplicarDescuento(1500.0)

print(automovil1.MostrarInformacion())
