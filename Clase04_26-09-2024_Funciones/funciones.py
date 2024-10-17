#funciones retornan un valor /
#procedimiento no retornan un valor

print("def saludar 1")
def saludar():
    print("Holaaaa")

x = saludar()
print(x)

print("def saludar 2")
def saludar2():
    print("Holaaaa")
    return True

x = saludar2()
print(x)

print("def saludar 3")
def saludar3(nombre, apellido):
    print(f"Holaaaa {nombre}, {apellido}")
    return True

x = saludar3("Armando","Luna")
print(x)

x = saludar3(apellido="luna", nombre="Armando")
print(x)

#x = saludar3("Armando")
#print(x)

print("def saludar 4")
def saludar4(nombre, apellido, domicilio=None):
    print(f"Holaaaa {nombre}, {apellido}")
    if domicilio:
        print(f"{domicilio}")
    return True

x = saludar4("Armando","Luna")
print(x)

x = saludar4("Armando","Luna", "micasa")
print(x)

print("def suma con tupla")

#funcion con argumentos posicionales _ esto genera una tupla
def sumar(*muchosElementos):
    print(muchosElementos)
    print(muchosElementos.__class__.__name__)
    suma = 0
    for num in muchosElementos:
        suma+=num
    return suma

suma = sumar(1,2,3,4,5)
print(f"suma {suma}")


#funcion con argumentos con clave _ esto genera un diccionario
def saludar5(**kwargs):
    #print(f"nombre {kwargs["nombre"]}")
    #print(f"apellido: {kwargs["apellido"]}")
    print(f"nombre {kwargs.get("nombre","-------")}")
    print(f"apellido {kwargs.get("apellido","-------")}")

saludar5(nombre="Armando",apellido="Luna")
saludar5(nombre="probando")
