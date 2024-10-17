"""
longitud: (rango entre 7 y 8)
si tiene caracteres especiales ( tambien .), son invalidos
todos los caracteres deben ser un digito
otras considreaciones por ustedes
"""

LISTA_DOCUMENTOS = [
    "123",
    "2223123",
    "24.142.523", #este esta bien
    "3333333333333333",
    "0",
    "0000000"
]

LISTA_DOCUMENTOS_VALIDOS = []
LISTA_DOCUMENTOS_INVALIDOS = []

for doc in LISTA_DOCUMENTOS:
    doc = doc.replace(".", "")

    if not doc.isnumeric():
        LISTA_DOCUMENTOS_INVALIDOS.append({
            "value":doc,
            "error": "Tiene caracteres especiales"
        })
        continue

    doc = int(doc)
    if not 999999 < doc < 100000000:
        LISTA_DOCUMENTOS_INVALIDOS.append({
            "value":doc,
            "error":"Se supera la longitud"
        })
        continue

    LISTA_DOCUMENTOS_VALIDOS.append(doc)

print("Documentos Validos:", LISTA_DOCUMENTOS_VALIDOS)
print("Documentos Invalidos:", LISTA_DOCUMENTOS_INVALIDOS)

   
