#---DECLARACION DE VARIABLES INICIALES---
nombreArchivoATratar = "datos_nomivac_parte1.csv" #Nombre del archivo del cual se obtendran los datos
nombreArchivoResultado = "LunaArmando_42202512_resultadoModeloMuestra.csv" # Nombre del archivo donde se guardara el analisis solicitado

CantidadPersonasVacunadasPorGenero = { #Diccionario para almacenar la cantidad de personas de cada genero que se aplico la vacuna
    "M": 0,
    "F": 0}
CantidadTipoVacunasAplicadas = {} #Diccionario para almacenar la cantidad de vacunas aplicadas separado por tipo de vacuna
CantidadDosisPorJurisdiccion = {} #Diccionario para almacenar la cantidad de dosis aplicadas por jurisdiccion
CantidadDeSegundasDosisPorJurisdiccion = {} #Diccionario para almacenar la cantidad de segundas dosis aplicadas por jurisdiccion

#---LECTURA Y TRATAMIENTO DE DATOS---

with open(nombreArchivoATratar, 'r', encoding='utf-8') as archivoATratar: #Abrir el archivo csv a tratar en Modo lectura

    NombreCampos = archivoATratar.readline() # Salteamos la fila con los nombres de cada campo.

    for fila in archivoATratar: #por cada fila o registro del archivo tratamos los datos
        #datos = fila.split(',') #Transformo la fila en una lista de datos separando con coma los valores.
        #print(datos)
        datos = fila.strip().split(',') # El strip es necesario para eliminar espacios en blanco y el caracter de nueva linea al final de cada linea.
        #print(datos)
        #Lista de la posicion de cada dato para su tratamiento - se puede ver a simple vista que todas las filas siguen el mismo patron
        #por lo cual era lo más conveniente tratarlos de esta forma.
        """De esta forma tenemos
        0 sexo,
        1 grupo_etario,
        2 jurisdiccion_residencia,
        3 jurisdiccion_residencia_id,
        4 depto_residencia,
        5 depto_residencia_id,
        6 jurisdiccion_aplicacion,
        7 jurisdiccion_aplicacion_id,
        8 depto_aplicacion,
        9 depto_aplicacion_id,
        10 fecha_aplicacion,
        11 vacuna,
        12 cod_dosis_generica,
        13 nombre_dosis_generica,
        14 condicion_aplicacion,
        15 orden_dosis,
        16 lote_vacuna,
        17 id_persona_dw
        """
        #Definicion de variables para tratamiento de Dato de una persona
        sexo = datos[0] #Obtengo el Sexo "M" o "F"
        tipoVacuna = datos[11] #Obtengo el Tipo de vacuna
        jurisdiccionResidencia = datos[2] #Obtengo el nombre de la Jurisdiccion de Residencia
        NroDosis = datos[13] #Obtengo que dosis se aplico una persona

        if sexo in CantidadPersonasVacunadasPorGenero: # Conteo de Sexo, si el sexo esta en el diccionario entonces sumo 1 al valor de la clave.
            CantidadPersonasVacunadasPorGenero[sexo] = CantidadPersonasVacunadasPorGenero[sexo] + 1

        if tipoVacuna in CantidadTipoVacunasAplicadas: #Conteo de Vacunas por tipo
            CantidadTipoVacunasAplicadas[tipoVacuna] = CantidadTipoVacunasAplicadas[tipoVacuna] + 1
        else: #Si no esta el valor, se lo agrega al diccionario
            CantidadTipoVacunasAplicadas[tipoVacuna] = 1

        if jurisdiccionResidencia in CantidadDosisPorJurisdiccion: #conteo de Vacunas aplicadas por jurisdiccion
            CantidadDosisPorJurisdiccion[jurisdiccionResidencia] = CantidadDosisPorJurisdiccion[jurisdiccionResidencia] + 1
        else:
            CantidadDosisPorJurisdiccion[jurisdiccionResidencia] = 1

        if NroDosis == '2da': #Conteo de Segundas dosis aplicadas por jurisdiccion
            if jurisdiccionResidencia in CantidadDeSegundasDosisPorJurisdiccion: #conteo de Vacunas aplicadas por jurisdiccion
                CantidadDeSegundasDosisPorJurisdiccion[jurisdiccionResidencia] = CantidadDeSegundasDosisPorJurisdiccion[jurisdiccionResidencia] + 1
            else:
                CantidadDeSegundasDosisPorJurisdiccion[jurisdiccionResidencia] = 1
        

        

        


#---ESCRITURA DE RESULTADOS OBTENIDOS EN UN NUEVO ARCHIVO---

with open(nombreArchivoResultado, 'w', encoding='utf-8-sig') as archivoResultado: #Modificar/Crear un archivo en modo escritura para guardar el analisis
    
    archivoResultado.write('Total de Campos Tratados:{}\n'.format((sum(CantidadPersonasVacunadasPorGenero.values()))))
    archivoResultado.write("\n")

    #Escritura de la cantidad de personas vacunadas por sexo
    archivoResultado.write('Distribución por Género:\n')
    for sexo, cantidad in CantidadPersonasVacunadasPorGenero.items():
        if sexo == "M":
            archivoResultado.write("Masculino: {} \n".format(cantidad))
        else:
            archivoResultado.write("Femenino: {} \n".format(cantidad))
    archivoResultado.write("\n")

    #Escritura de la cantidad de vacunas aplicadas por tipo de vacuna
    totalVacunas = sum(CantidadTipoVacunasAplicadas.values())
    archivoResultado.write('Vacunas Aplicadas por Tipo de Vacuna _ Total vacunas Aplicadas: {}\n'.format(totalVacunas))
    for tipoVacuna, cantidad in CantidadTipoVacunasAplicadas.items():
        porcentaje = (cantidad / totalVacunas) * 100
        archivoResultado.write("{}. Cantidad aplicada: {} Porcentaje: {}%\n".format(tipoVacuna,cantidad,round(porcentaje,2)))
    archivoResultado.write("\n")

    #Escitura de la cantidad de vacunas por Jurisdiccion de Residencia.
    archivoResultado.write('Dosis por Jurisdicción de Dependencia\n')
    for Jurisdiccion, cantidad in CantidadDosisPorJurisdiccion.items():
        archivoResultado.write("{}: {} dosis.\n".format(Jurisdiccion,cantidad))
    archivoResultado.write("\n")
    
    #Escitura de la cantidad de vacunas por Jurisdiccion de Residencia.
    archivoResultado.write('Cantidad de Segundas Dosis aplicadas por Jurisdicción de Dependencia\n')
    for Jurisdiccion, cantidad in CantidadDeSegundasDosisPorJurisdiccion.items():
        archivoResultado.write("{}: {} dosis.\n".format(Jurisdiccion,cantidad))
    archivoResultado.write("\n")