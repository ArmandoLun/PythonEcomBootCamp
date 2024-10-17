# IMPORTS
# Librerias
# Librerias propias
from parametros import LISTA_DOCUMENTOS
from funcionesPropias.core import validarDocumentos

"""
longitud: (rango entre 7 y 8)
si tiene caracteres especiales ( tambien .), son invalidos
todos los caracteres deben ser un digito
otras considreaciones por ustedes
"""

lista_documentos_validos, lista_documentos_invalidos = validarDocumentos(LISTA_DOCUMENTOS)

print("Documentos Validos:", lista_documentos_validos)
print("Documentos Invalidos:", lista_documentos_invalidos)

   
