frutas = ["manzana", "banana", "naranja", "mango", "melon"]

print(frutas)
print(frutas[1])
print(frutas[2:4]) #obtengo una lista
print(frutas[-1])
print(frutas[:3]) #obtengo los primeros 3 elementos
print(frutas[3:]) #ignoro los 3 primeros elementos

for fruta in frutas:
    print(fruta)


frutas.append("ciruelas")
print(frutas)
frutas.insert(1,50)
print(frutas)