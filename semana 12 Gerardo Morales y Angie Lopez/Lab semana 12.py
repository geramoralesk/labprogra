
class Datos: 
    nombres = ""
    apellidos = ""
    apellidodecasada = ""
    fechadenacimiento = ""

    def __init__(self):
        self.nombres = ""
        self.apellidos = ""
        self.apellidodecasada = ""
        self.fechadenacimiento = ""
    
    def mostrar_nombres(self, nombres):
        return self.nombres

    def mostrar_apellidos(self,apellidos):
        return self.apellidos
    
    def mostrar_apellidosdecasada(self, apellidodecasada):
        return self.apellidodecasada
    
    def mostrar_fechadenacimiento(self, fechadenacimiento):
        return self.fechadenacimiento

    def ingresar_nombres(self, nombres):

        self.nombres = nombres 

    def ingresar_apellidos(self, apellidos):

        self.apellidos = apellidos 

    def ingresar_apellidodecasada(self, apellidodecasada):

        self.apellidodecasada = apellidodecasada

    def ingresar_fechadenacimiento(self, fechadenacimiento):

        self.fechadenacimiento = fechadenacimiento

persona1 = Datos()
persona1.nombres = "Maria Alejandra"
persona1.apellidos = "Gonzalez Vargas"
persona1.apellidodecasada = "Paz"
persona1.fechadenacimiento = "1995/10/04"

persona2 = Datos()
persona2.nombres = "Valeria Sofia"
persona2.apellidos = "Sandoval Perez"
persona2.apellidodecasada = "Molina"
persona2.fechadenacimiento = "1990/05/28"

print(persona1.mostrar_nombres(""))
print(persona1.mostrar_apellidos(""))
print(persona1.mostrar_apellidosdecasada(""))
print(persona1.mostrar_fechadenacimiento(""))


print(persona2.mostrar_nombres(""))
print(persona2.mostrar_apellidos(""))
print(persona2.mostrar_apellidosdecasada(""))
print(persona2.mostrar_fechadenacimiento(""))