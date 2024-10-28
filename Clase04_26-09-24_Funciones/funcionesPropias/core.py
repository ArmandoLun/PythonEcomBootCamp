from .validador import todoesnumerico, controlRango

def validarDocumentos(lista_documentos):
    
    lista_documentos_validos = []
    lista_documentos_invalidos = []

    for doc in lista_documentos:
        doc = doc.replace(".", "")

        if (todoesnumerico(doc)):
            lista_documentos_invalidos.append({
                "value":doc,
                "error": "Tiene caracteres especiales"
            })
            continue

        doc = int(doc)
        if not (controlRango(doc)):
            lista_documentos_invalidos.append({
                "value":doc,
                "error":"Se supera la longitud"
            })
            continue
        lista_documentos_validos.append(doc)
    
    return lista_documentos_validos, lista_documentos_invalidos