persona = {
    "nombre": "armando",
    "apellido": "luna",
    "direccion": "mi casa"
}
#esto da error
#print(persona["estadoCivil"])
direccion = None
try:
    x = 10 / 0
    direccion = persona["estadoCivil"]
except ZeroDivisionError:
    print("no se puede dividir por 0")
except:
    print("ocurrio un error")

if direccion is not None:
    print(f"la direccion de la persona es {direccion}")

try:
    direccion = persona["estadoCivil"]
except Exception as laExepcion:
    print("ocurrio un error",laExepcion)
