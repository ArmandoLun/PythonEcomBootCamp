#las tuplas son inmutables
frutas = ("manzana", "banana", "naranja")
#"manzana", "banana", "naranja"
#   0           1          2
print(frutas)
print(frutas[1])

frutas = ("manzana", "banana", "naranja", "mango", "melon")
print(frutas)
print(frutas[1])
print(frutas[2:4])
print(frutas[-1])
print(frutas[:3]) #obtengo los primeros 3 elementos
print(frutas[3:]) #ignoro los 3 primeros elementos

#actualizar una tupla, es una trampa
frutas_act = list(frutas)
print("ahora soy una",frutas.__class__.__name__)
print("ahora soy una",frutas_act.__class__.__name__)
frutas_act[1] = "superBanana"
frutas = tuple(frutas_act)
print(frutas)

#algunas operaciones con tuplas
tupla1 = ("a", "b", "c")
tupla2 = (10, 36, 34)
tupla3 = tupla1 + tupla2
print(tupla3)