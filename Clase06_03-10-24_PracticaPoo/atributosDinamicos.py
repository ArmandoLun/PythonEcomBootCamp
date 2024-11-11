from triangulo import Triangulo

t = Triangulo(2,2,3)


ladoTres = "lado3"
lado3 = getattr(t, ladoTres)
print("lado3:",lado3)
setattr(t, ladoTres, 55)
lado3 = getattr(t, ladoTres)
print("lado3:",lado3)

ladoNoExiste = "lado4"
lado3 = getattr(t, ladoNoExiste, "No se encuentra este lado")
print (lado3)