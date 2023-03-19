# import de Pandas y numpy para arreglos 2D
import numpy as np
import pandas as pd

# Se abre el archivo para poder registrar los resultados
file = open('Avance2_Evidencia1.txt','w')

# Titulo del archivo de resultados
file.write("-----------------------------------------------------------------------------\n")
file.write("RESULTADOS DE PROCEDIMIENTOS SOLICITADOS POR PARTE DE LA EVIDENCIA 1 AVANCE 2\n")
file.write("-----------------------------------------------------------------------------\n\n\n")

# Metodo que extrae los datos del CSV de las tarifas por puntos y las coloca en una variable
def extraerCSVPuntos():
    return pd.read_csv('Archivos con Datos\\Tarifas por puntos 2016-2017.csv', header = 0)

# Metodo que extrae los datos del CSV de las tarifas por zonas y las coloca en una variable
def extraerCSVZonas():
    return pd.read_csv('Archivos con Datos\\Tarifas por zonas 2016-2017.csv', header = 0)

# Metodo que calcula el promedio general de todas las tarifas de ambos CSVs por año
def promedioPorAnios():

    # Se obtienen los valores de los CSVs
    datosTablaPuntos = extraerCSVPuntos()
    datosTablaZonas = extraerCSVZonas()

    # Se crean columnas en las que se suman las tarifas de capacidad y de uso por cada tipo de contrato por cada renglon de la tabla de tarifas por puntos
    datosTablaPuntos['base_firme_total'] = datosTablaPuntos['capacidad_base_firme'] + datosTablaPuntos['uso_base_firme']
    datosTablaPuntos['base_firme_temporal_total'] = datosTablaPuntos['capacidad_base_firme_temporal'] + datosTablaPuntos['uso_base_firme_temporal']
    datosTablaPuntos['base_interrumpible_total'] = datosTablaPuntos['capacidad_base_interrumpible'] + datosTablaPuntos['uso_base_interrumpible']
    datosTablaPuntos['fecha_inicio'] = pd.to_datetime(datosTablaPuntos['fecha_inicio'], dayfirst=True)

    # Se crean columnas en las que se suman las tarifas de capacidad y de uso por cada tipo de contrato por cada renglon de la tabla de tarifas por zonas
    datosTablaZonas['base_firme_total'] = datosTablaZonas['capacidad_base_firme'] + datosTablaZonas['uso_base_firme']
    datosTablaZonas['base_temporal_total'] = datosTablaZonas['capacidad_base_temporal'] + datosTablaZonas['uso_base_temporal']
    datosTablaZonas['base_interrumpible_total'] = datosTablaZonas['maxima_base_interrumpible'] + datosTablaZonas['minima_base_interrumpible']
    datosTablaZonas['fecha_inicio'] = pd.to_datetime(datosTablaZonas['fecha_inicio'], dayfirst=True)

    # Se separan los registros de ambas tablas por el año al que pertenecen
    datosTablaPuntos2016 = datosTablaPuntos[(datosTablaPuntos['fecha_inicio'] >= "2016-01-01") & (datosTablaPuntos['fecha_inicio'] <= "2016-12-31")]
    datosTablaPuntos2017 = datosTablaPuntos[(datosTablaPuntos['fecha_inicio'] >= "2017-01-01") & (datosTablaPuntos['fecha_inicio'] <= "2017-12-31")]
    datosTablaZonas2016 = datosTablaZonas[(datosTablaZonas['fecha_inicio'] >= "2016-01-01") & (datosTablaZonas['fecha_inicio'] <= "2016-12-31")]
    datosTablaZonas2017 = datosTablaZonas[(datosTablaZonas['fecha_inicio'] >= "2017-01-01") & (datosTablaZonas['fecha_inicio'] <= "2017-12-31")]

    # Se obtienen los promedios de los totales de tarifas al igual que la de volumetrica del año 2016 de la tabla de tarifas por puntos y se calcula el promedio general de la tabla
    promedioBaseFirmeTablaPuntos2016 = datosTablaPuntos2016['base_firme_total'].mean()
    promedioBaseFirmeTemporalTablaPuntos2016 = datosTablaPuntos2016['base_firme_temporal_total'].mean()
    promedioBaseInterrumpibleTablaPuntos2016 = datosTablaPuntos2016['base_interrumpible_total'].mean()
    promedioVolumetricaTablaPuntos2016 = datosTablaPuntos2016['volumetrica'].mean()

    promedioGeneralTablaPuntos2016 = round((promedioBaseFirmeTablaPuntos2016 + promedioBaseFirmeTemporalTablaPuntos2016 + promedioBaseInterrumpibleTablaPuntos2016 + promedioVolumetricaTablaPuntos2016) / 4,4)

    # Se obtienen los promedios de los totales de tarifas al igual que la de volumetrica del año 2017 de la tabla de tarifas por puntos
    promedioBaseFirmeTablaPuntos2017 = datosTablaPuntos2017['base_firme_total'].mean()
    promedioBaseFirmeTemporalTablaPuntos2017 = datosTablaPuntos2017['base_firme_temporal_total'].mean()
    promedioBaseInterrumpibleTablaPuntos2017 = datosTablaPuntos2017['base_interrumpible_total'].mean()
    promedioVolumetricaTablaPuntos2017 = datosTablaPuntos2017['volumetrica'].mean()

    promedioGeneralTablaPuntos2017 = round((promedioBaseFirmeTablaPuntos2017 + promedioBaseFirmeTemporalTablaPuntos2017 + promedioBaseInterrumpibleTablaPuntos2017 + promedioVolumetricaTablaPuntos2017) / 4,4)

    # Se obtienen los promedios de los totales de tarifas al igual que la de volumetrica del año 2016 de la tabla de tarifas por zonas
    promedioBaseFirmeTablaZonas2016 = datosTablaZonas2016['base_firme_total'].mean()
    promedioBaseFirmeTemporalTablaZonas2016 = datosTablaZonas2016['base_temporal_total'].mean()
    promedioBaseInterrumpibleTablaZonas2016 = datosTablaZonas2016['base_interrumpible_total'].mean()
    promedioVolumetricaTablaZonas2016 = datosTablaZonas2016['volumetrica'].mean()

    promedioGeneralTablaZonas2016 = round((promedioBaseFirmeTablaZonas2016 + promedioBaseFirmeTemporalTablaZonas2016 + promedioBaseInterrumpibleTablaZonas2016 + promedioVolumetricaTablaZonas2016) / 4, 4)

    # Se obtienen los promedios de los totales de tarifas al igual que la de volumetrica del año 2017 de la tabla de tarifas por zonas
    promedioBaseFirmeTablaZonas2017 = datosTablaZonas2017['base_firme_total'].mean()
    promedioBaseFirmeTemporalTablaZonas2017 = datosTablaZonas2017['base_temporal_total'].mean()
    promedioBaseInterrumpibleTablaZonas2017 = datosTablaZonas2017['base_interrumpible_total'].mean()
    promedioVolumetricaTablaZonas2017 = datosTablaZonas2017['volumetrica'].mean()

    promedioGeneralTablaZonas2017 = round((promedioBaseFirmeTablaZonas2017 + promedioBaseFirmeTemporalTablaZonas2017 + promedioBaseInterrumpibleTablaZonas2017 + promedioVolumetricaTablaZonas2017) / 4, 4)

    # Se coloca en el archivo los resultados
    file.write("---------------------------------------------------------------------------------------------------\n")
    file.write("OBTENCION DEL PROMEDIO ANUAL DE TODAS LAS TARIFAS EN AMBAS TABLAS (ZONAS y PUNTOS) PARA 2016 Y 2017\n")
    file.write("---------------------------------------------------------------------------------------------------\n\n\n")
    file.write("Resultados\n\n")
    file.write(f"Promedio general de las tarifas de gas segun la tabla de puntos de 2016: {promedioGeneralTablaPuntos2016}\n")
    file.write(f"Promedio general de las tarifas de gas segun la tabla de puntos de 2017: {promedioGeneralTablaPuntos2017}\n")
    file.write(f"Promedio general de las tarifas de gas segun la tabla de zonas de 2016: {promedioGeneralTablaZonas2016}\n")
    file.write(f"Promedio general de las tarifas de gas segun la tabla de zonas de 2017: {promedioGeneralTablaZonas2017}\n\n")
    file.write("---------------------------------------------------------------------------------------------------\n")
    file.write("---------------------------------------------------------------------------------------------------\n")
    file.write("---------------------------------------------------------------------------------------------------\n\n\n")

# Se encarga de obtener el promedio de cada tipo de tarifa por cada trimestre que hubo de entre 2016 a 2017
def variacionPrecioGas():

    # Se establecen los limites que componen a cada trimestre
    limitesTrimestres2016 = ['2016-01-01', '2016-03-31', '2016-04-01', '2016-06-30', '2016-07-01', '2016-09-30', '2016-10-01', '2016-12-31']
    limitesTrimestres2017 = ['2017-01-01', '2017-03-31', '2017-04-01', '2017-06-30', '2017-07-01', '2017-09-30', '2017-10-01', '2017-12-31']

    # Arreglos para guardar los promedios de cada año
    datos2016 = np.ndarray([4,4])
    datos2017 = np.ndarray([4,4])

    datosTablaPuntos = extraerCSVPuntos()

    # Se crean columnas en las que se suman las tarifas de capacidad y de uso por cada tipo de contrato por cada renglon de la tabla de tarifas por puntos
    datosTablaPuntos['base_firme_total'] = datosTablaPuntos['capacidad_base_firme'] + datosTablaPuntos['uso_base_firme']
    datosTablaPuntos['base_firme_temporal_total'] = datosTablaPuntos['capacidad_base_firme_temporal'] + datosTablaPuntos['uso_base_firme_temporal']
    datosTablaPuntos['base_interrumpible_total'] = datosTablaPuntos['capacidad_base_interrumpible'] + datosTablaPuntos['uso_base_interrumpible']
    datosTablaPuntos['fecha_inicio'] = pd.to_datetime(datosTablaPuntos['fecha_inicio'], dayfirst=True)

    # Se obtiene el promedio de cada tipo de tarifa por cada trimestre de 2016
    j = 0
    for i in range(0,8,2):
        trimestreActual = datosTablaPuntos[(datosTablaPuntos['fecha_inicio'] >= limitesTrimestres2016[i]) & (datosTablaPuntos['fecha_inicio'] <= limitesTrimestres2016[i+1])]
        datos2016[j, 0] = round(trimestreActual['base_firme_total'].mean(),4)
        datos2016[j, 1] = round(trimestreActual['base_firme_temporal_total'].mean(),4)
        datos2016[j, 2] = round(trimestreActual['base_interrumpible_total'].mean(),4)
        datos2016[j, 3] = round(trimestreActual['volumetrica'].mean(),4)
        j += 1

    # Se obtiene el promedio de cada tipo de tarifa por cada trimestre de 2017
    j = 0
    for i in range(0,8,2):
        trimestreActual = datosTablaPuntos[(datosTablaPuntos['fecha_inicio'] >= limitesTrimestres2017[i]) & (datosTablaPuntos['fecha_inicio'] <= limitesTrimestres2017[i + 1])]
        datos2017[j, 0] = round(trimestreActual['base_firme_total'].mean(),4)
        datos2017[j, 1] = round(trimestreActual['base_firme_temporal_total'].mean(),4)
        datos2017[j, 2] = round(trimestreActual['base_interrumpible_total'].mean(),4)
        datos2017[j, 3] = round(trimestreActual['volumetrica'].mean(),4)
        j += 1

    # Arreglos para lograr ejecutar un ciclo y escribir en el archivo los valores
    tipoTarifa = ['BASE FIRME', 'BASE FIRME TEMPORAL', 'BASE INTERRUMPIBLE', 'VOLUMETRICA']
    numTrimestre = ['trimestre 1 (Enero - Marzo)', 'trimestre 2 (Abril - Junio)', 'trimestre 3 (Julio - Septiembre)', 'trimestre 4 (Octubre - Diciembre)']

    file.write("-----------------------------------------------------------------------------------------------\n")
    file.write("OBTENCION DE LA VARIACION DEL PROMEDIO TRIMESTRAL POR CADA TIPO DE TARIFA DESDE 2016 HASTA 2017\n")
    file.write("-----------------------------------------------------------------------------------------------\n\n\n")
    file.write("Resultados\n\n")

    for x in range(0, 4):
        for j in range(0, 4):
            file.write(f"Promedio de la tarifa {tipoTarifa[x]} durante el {numTrimestre[j]} de 2016: {datos2016[j,x]}\n")

        for j in range(0, 4):
            file.write(f"Promedio de la tarifa {tipoTarifa[x]} durante el {numTrimestre[j]} de 2017: {datos2017[j,x]}\n")
        file.write("----------------------------------------------------------------------------------------------\n")
    file.write("----------------------------------------------------------------------------------------------\n")
    file.write("----------------------------------------------------------------------------------------------\n")
    file.write("----------------------------------------------------------------------------------------------\n\n\n")

# Obtiene el promedio por zona de cada tipo de tarifa por año
def promedioPorZona(fechaInicio, fechaFin, anio):

    # Zonas disponibles
    Zonas = ["Norte", "Sur", "Occidente", "Centro", "Golfo", "Istmo", "Nacional", "Nacional con AB"]
    datos = np.ndarray([4, 8])

    # Se filtra la tabla en base al año a revisar
    datosTablaZonas = extraerCSVZonas()
    datosTablaZonas['fecha_inicio'] = pd.to_datetime(datosTablaZonas['fecha_inicio'], dayfirst=True)
    datosTablaZonas = datosTablaZonas[(datosTablaZonas['fecha_inicio'] >= fechaInicio) & (datosTablaZonas['fecha_inicio'] <= fechaFin)]

    # Se crean columnas en las que se suman las tarifas de capacidad y de uso por cada tipo de contrato por cada renglon de la tabla de tarifas por zonas
    datosTablaZonas['base_firme_total'] = datosTablaZonas['capacidad_base_firme'] + datosTablaZonas['uso_base_firme']
    datosTablaZonas['base_temporal_total'] = datosTablaZonas['capacidad_base_temporal'] + datosTablaZonas['uso_base_temporal']
    datosTablaZonas['base_interrumpible_total'] = datosTablaZonas['maxima_base_interrumpible'] + datosTablaZonas['minima_base_interrumpible']

    # Se obtienen los promedios de cada tipo de tarifa por cada zona
    for i in range(0, 8):
        zonaActual  = datosTablaZonas[datosTablaZonas['zona'] == Zonas[i]]
        datos[0, i] = round(zonaActual['base_firme_total'].mean(), 4)
        datos[1, i] = round(zonaActual['base_temporal_total'].mean(), 4)
        datos[2, i] = round(zonaActual['base_interrumpible_total'].mean(), 4)
        datos[3, i] = round(zonaActual['volumetrica'].mean(), 4)

    tipoTarifa = ['BASE FIRME', 'BASE FIRME TEMPORAL', 'BASE INTERRUMPIBLE', 'VOLUMETRICA']

    # Se escribe en el archivo
    file.write("-----------------------------------------------------------------------------\n")
    file.write(f"CALCULO DEL PROMEDIO POR CADA TIPO DE TARIFA EN CADA ZONA EXISTENTE ({anio})\n")
    file.write("-----------------------------------------------------------------------------\n\n\n")
    file.write("Resultados\n\n")
    for x in range(0, 8):
        for j in range(0, 4):
            file.write(f"Promedio en la zona {Zonas[x].upper()} con la tarifa {tipoTarifa[j]} del {anio}: {datos[j,x]}\n")
        file.write("------------------------------------------------------------------------------\n")
    file.write("------------------------------------------------------------------------------\n")
    file.write("------------------------------------------------------------------------------\n")
    file.write("------------------------------------------------------------------------------\n\n\n")

# Obtiene las tarifas mas altas por cada columna de un año especifico
def mayorDelAnio(fechaInicio, fechaFin, anio):

    #Se obtienen y se filtran los datos
    datosTablaPuntos = extraerCSVPuntos()
    datosTablaPuntos['fecha_inicio'] = pd.to_datetime(datosTablaPuntos['fecha_inicio'], dayfirst=True)
    datosTablaPuntos = datosTablaPuntos[(datosTablaPuntos['fecha_inicio'] >= fechaInicio) & (datosTablaPuntos['fecha_inicio'] <= fechaFin)]

    #Se obtiene de cada columna el valor máximo
    maxValorCapacidadBaseFirme = datosTablaPuntos['capacidad_base_firme'].max()
    maxValorUsoBaseFirme = datosTablaPuntos['uso_base_firme'].max()
    maxValorCapacidadTemp = datosTablaPuntos['capacidad_base_firme_temporal'].max()
    maxValorUsoTemp = datosTablaPuntos['uso_base_firme_temporal'].max()
    maxValorCapacidadInterrumpible = datosTablaPuntos['capacidad_base_interrumpible'].max()
    maxValorCapacidadBaseFirmeInterr = datosTablaPuntos['uso_base_interrumpible'].max()
    maxValorVolumetrica = datosTablaPuntos['volumetrica'].max()

    # Se escribe en el archivo de resultados
    file.write("------------------------------------------------------\n")
    file.write(f"OBTENCION DE LAS TARIFAS MAS GRANDES DEL ANIO ({anio})\n")
    file.write("------------------------------------------------------\n\n\n")
    file.write("Resultados\n\n")
    file.write(f'Mayor tarifa de capacidad base firme: {maxValorCapacidadBaseFirme}\n')
    file.write(f'Mayor tarifa de uso base firme: {maxValorUsoBaseFirme}\n')
    file.write(f'Mayor tarifa de capacidad base temporal: {maxValorCapacidadTemp}\n')
    file.write(f'Mayor tarifa de uso base temporal: {maxValorUsoTemp}\n')
    file.write(f'Mayor tarifa de capacidad base interrumpible: {maxValorCapacidadInterrumpible}\n')
    file.write(f'Mayor tarifa de uso base interrumpible: {maxValorCapacidadBaseFirmeInterr}\n')
    file.write(f'Mayor tarifa volumetrica: {maxValorVolumetrica}\n')
    file.write("---------------------------------------------------\n")
    file.write("---------------------------------------------------\n")
    file.write("---------------------------------------------------\n\n\n")

# Se ejecutan los metodos
promedioPorAnios()
variacionPrecioGas()
promedioPorZona("2016-01-01", "2016-12-31", "2016")
promedioPorZona("2017-01-01", "2017-12-31", "2017")
mayorDelAnio("2016-01-01", "2016-12-31", "2016")
mayorDelAnio("2017-01-01", "2017-12-31", "2017")

# Se cierra el archivo y se guardan los cambios
file.close()