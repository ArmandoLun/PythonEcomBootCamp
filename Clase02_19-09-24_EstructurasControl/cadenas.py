nombre = "Lucas"
apellido = "ibañez"
formato1 = nombre + " " + apellido

#f-string
formato2 = f"{nombre} {apellido}"
formato3 = "---> %s %s" % (nombre, apellido)
formato4 = "Hola, mi nombre es {}, {}.".format(nombre, apellido)
print("Formato1: ", formato1)
print("Formato2: ", formato2)
print("Formato3:", formato3)
print("formato4:",formato4)

"""
comentario multi linea
"""

texto = """
probando un texto muy largo
"""

