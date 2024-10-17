vehiculo = {
    "marca": "Ford",
    "modelo": "Mustang",
    "anio": 1964,
    1: "otro tipo de indice"
}

print(vehiculo)
print(len(vehiculo))

print(vehiculo["marca"])
print(vehiculo.get("marca"))
print(vehiculo.keys())
print(vehiculo.items())
print(vehiculo.values())


vehiculo.update({"anio":1954})
print(vehiculo)
vehiculo["anio"] = 1432
print(vehiculo)

vehiculo["tipo"] = "sedan"
print(vehiculo)

vehiculo.update({"tipo": "sedan"})
print(vehiculo)