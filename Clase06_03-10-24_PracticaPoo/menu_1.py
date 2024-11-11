def opcion1():
    print("Esta es la opcion1")
    print("presione enter para continuar")
    input()

def opcion2():
    print("Esta es la opcion2")
    print("presione enter para continuar")
    input()

MenuPrincipal = [
    {
        "nombre": "Opcion 1"
    },
    {
        "nombre": "Opcion 2"
    },
    {
        "nombre": "Salir"
    },
]

while True:
    print("Ingrese una de las siguientes opciones:")

    for indice, opcion_dict in enumerate(MenuPrincipal):
        print(f"{indice+1} - {opcion_dict["nombre"]}")
    
    print("---------------------")
    
    opcion = input(">")
    if not opcion.isnumeric():
        print("Solo valores numericos")
        continue
    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        break
    else:
        print("Error, dato incorrecto")


