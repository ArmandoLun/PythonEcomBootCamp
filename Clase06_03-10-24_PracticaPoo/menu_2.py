def opcion1():
    print("Esta es la opcion1")
    print("presione enter para continuar")
    input()

def opcion2():
    print("Esta es la opcion2")
    print("presione enter para continuar")
    input()

def salir():
    print("chau")

MenuPrincipal = {
    1: {
        "nombre": "Opcion 1",
        "metodo": opcion1
    },
    2: {
        "nombre": "Opcion 2",
        "metodo": opcion2
    },
    3: {
        "nombre": "Salir",
        "metodo": salir
    }
}

while True:
    print("Ingrese una de las siguientes opciones:")

    for indice, opcion_dict in MenuPrincipal.items():
        print(f"{indice} - {opcion_dict["nombre"]}")
    
    print("---------------------")
    

    
    opcion = input(">")
    if not opcion.isnumeric():
        print("Solo valores numericos")
        continue

    MenuPrincipal.get(int(opcion))["metodo"]()
    """
    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        break
    else:
        print("Error, dato incorrecto")
    """