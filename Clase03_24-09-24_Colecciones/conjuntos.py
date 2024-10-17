#conjunto, son inmutables pero se puede agregar o quitar
frutas = {"manzana", "banana", "naranja", "mango", "melon","mango"}
print(frutas.__class__.__name__)
print(frutas)

frutas = {"manzana", "banana", "naranja", "mango", "melon","mango", 1, 34.5, True}
print(frutas)

for fruta in frutas:
    print(fruta)

frutas.add("agregado")
print(frutas)

frutas_tropicales = {"mango", "papaya"}
frutas.update(frutas_tropicales)
print(frutas)

frutas.remove("melon")
print(frutas)

#no genera error al intentar borrar un elemento del conjuto
frutas.discard("melonn")