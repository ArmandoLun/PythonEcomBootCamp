"""
Pilares POO
Abstraccion
encapsulamiento
herencia
polimorfismo

Clase y Objeto
Clase es un "molde", una estructura base para crear diferentes objetos.
Objeto, una instancia unica de una clase.

Componentes de un objeto
atributos, caracteristicas
metodos, funciones, servicios
identificador

"""

class coche:
    """
    coche: marca, modelo
    """

    def __init__(self, marca, modelo):
        self.marca = "ford"
        self.modelo = "Focus"

    def conducir(self):
        print(f"conduciendo el {self.marca} {self.modelo}")

cocheUno = coche(marca="Ford",modelo="Focus")
print(cocheUno.marca)
print(cocheUno.modelo)
cocheUno.conducir()