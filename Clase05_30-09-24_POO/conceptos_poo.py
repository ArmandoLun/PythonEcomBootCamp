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
#---ABSTRACCION---
class coche:
    """
    coche: marca, modelo
    """

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        print(f"conduciendo el {self.marca} {self.modelo}")
        return f"conduciendo el {self.marca} {self.modelo}"

cocheUno = coche(marca="Ford",modelo="Focus")
print(cocheUno.marca)
print(cocheUno.modelo)
cocheUno.conducir()
print(cocheUno.conducir())

coche2= coche(marca="Ferrari",modelo="F1")
print(coche2.marca)
print(coche2.modelo)

#---ENCAPSULAMIENTO---
#limitar el acceso a un atributo a metodo.
class CuentaBancaria:
    def __init__(self,saldo):
        self.__saldo = saldo
    
    def depositar(self,monto):
        self.__saldo += monto

    def mostrar_saldo(self):
        print(f"Saldo actual:{self.__saldo}")

#cuenta = CuentaBancaria(2000)
#print(f"Tengo:{cuenta.saldo}")
#cuenta.depositar(500)
#print(f"Tengo ahora:{cuenta.saldo}")
#cuenta.mostrar_saldo()
#cuenta.saldo = 0 #muestra de que puedo cambiar el valor porque es publico
#cuenta.mostrar_saldo()
#cuenta.__saldo = 1000
#cuenta.mostrar_saldo()


#--HERENCIA--
class animal:
    def grito(self): #metodo abstracto
        return NotImplementedError("Este metodo debe ser sobreescrito por sus clases hijas")
    def mensaje(self):
        return "soy animal"

class perro(animal):
    def grito(self):
        return "guau!"
    
    def mensaje(self):
        return "soy perro"

class gato(animal):
    def grito(self):
        return  "miau!"

class animalMutante(animal):
    def come(self):
        return "Humanos"


animalejo = animal()
animalejo.grito()

perrito = perro()
print(perrito.grito(),perrito.__class__.__name__, perrito.mensaje())

gatito = gato()
print(gatito.grito(), gatito.__class__.__name__,gatito.mensaje())

animalmutageneo = animalMutante()
animalmutageneo.come()
animalmutageneo.grito()


#MULTI - HERENCIA - como python hace herencia multiple ? 


#POLIMORFISMO
#permite que un mismo metodo pueda tener distintos compartamientos
#dependiendo que el objeto que lo llame
#esto se da entre diferentes clases

#Sobrecarga, usar un metodo con el mismo nombre en la misma clase, se sobrecarga la cantidad de parametros que tiene un metodo.

class Ave:
    def volar(self):
        print("vuelo")

class Pinguino(Ave):
    def volar(self):
        print("no vuela")

ave = Ave()
pinguino = Pinguino()
ave.volar()
pinguino.volar()