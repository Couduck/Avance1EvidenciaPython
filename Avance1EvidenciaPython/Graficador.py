import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import ProcesosArchivo as ArchivoDriver

# Metodo principal del programa
def ejecucion():
    graficoLineal()
    graficoBarras()

# Metodo para crear la grafica lineal
def graficoLineal():

    # Se obtienen los datos del CSV de la tabla de Tarifas por Puntos
    # Se crean columnas adicionales que representan la suma de las columnas de capacidad y uso de las tarifas correpondientes,
    # esto es para obtener el promedio del costo total de cada tarifa

    cursorPandas = ArchivoDriver.extraerCSVPuntos()
    cursorPandas['fecha_inicio'] = pd.to_datetime(cursorPandas['fecha_inicio'], dayfirst=True)
    cursorPandas['fecha_fin'] = pd.to_datetime(cursorPandas['fecha_fin'], dayfirst=True)
    cursorPandas['base_firme_total'] = cursorPandas['capacidad_base_firme'] + cursorPandas['uso_base_firme']
    cursorPandas['base_firme_temporal_total'] = cursorPandas['capacidad_base_firme_temporal'] + cursorPandas[
        'uso_base_firme_temporal']
    cursorPandas['base_interrumpible_total'] = cursorPandas['capacidad_base_interrumpible'] + cursorPandas[
        'uso_base_interrumpible']

    # Se crean Dataframes separados por trimestres para ambos años
    registrosTrimestre1_2016 = cursorPandas[
        (cursorPandas['fecha_inicio'] >= "2016-01-01") & (cursorPandas['fecha_inicio'] <= "2016-03-31")]
    registrosTrimestre2_2016 = cursorPandas[
        (cursorPandas['fecha_inicio'] >= "2016-04-01") & (cursorPandas['fecha_inicio'] <= "2016-06-30")]
    registrosTrimestre3_2016 = cursorPandas[
        (cursorPandas['fecha_inicio'] >= "2016-07-01") & (cursorPandas['fecha_inicio'] <= "2016-09-30")]
    registrosTrimestre4_2016 = cursorPandas[
        (cursorPandas['fecha_inicio'] >= "2016-10-01") & (cursorPandas['fecha_inicio'] <= "2016-12-31")]
    registrosTrimestre1_2017 = cursorPandas[
        (cursorPandas['fecha_inicio'] >= "2017-01-01") & (cursorPandas['fecha_inicio'] <= "2017-03-31")]
    registrosTrimestre2_2017 = cursorPandas[
        (cursorPandas['fecha_inicio'] >= "2017-04-01") & (cursorPandas['fecha_inicio'] <= "2017-06-30")]
    registrosTrimestre3_2017 = cursorPandas[
        (cursorPandas['fecha_inicio'] >= "2017-07-01") & (cursorPandas['fecha_inicio'] <= "2017-09-30")]
    registrosTrimestre4_2017 = cursorPandas[
        (cursorPandas['fecha_inicio'] >= "2017-10-01") & (cursorPandas['fecha_inicio'] <= "2017-12-31")]

    # Se obtienen los promedios de cada tarifa por cada trimestre
    PromediosTrimestre1_2016 = [registrosTrimestre1_2016['base_firme_total'].mean(),
                                registrosTrimestre1_2016['base_firme_temporal_total'].mean(),
                                registrosTrimestre1_2016['base_interrumpible_total'].mean(),
                                registrosTrimestre1_2016['volumetrica'].mean()]

    PromediosTrimestre2_2016 = [registrosTrimestre2_2016['base_firme_total'].mean(),
                                registrosTrimestre2_2016['base_firme_temporal_total'].mean(),
                                registrosTrimestre2_2016['base_interrumpible_total'].mean(),
                                registrosTrimestre2_2016['volumetrica'].mean()]

    PromediosTrimestre3_2016 = [registrosTrimestre3_2016['base_firme_total'].mean(),
                                registrosTrimestre3_2016['base_firme_temporal_total'].mean(),
                                registrosTrimestre3_2016['base_interrumpible_total'].mean(),
                                registrosTrimestre3_2016['volumetrica'].mean()]

    PromediosTrimestre4_2016 = [registrosTrimestre4_2016['base_firme_total'].mean(),
                                registrosTrimestre4_2016['base_firme_temporal_total'].mean(),
                                registrosTrimestre4_2016['base_interrumpible_total'].mean(),
                                registrosTrimestre4_2016['volumetrica'].mean()]

    PromediosTrimestre1_2017 = [registrosTrimestre1_2017['base_firme_total'].mean(),
                                registrosTrimestre1_2017['base_firme_temporal_total'].mean(),
                                registrosTrimestre1_2017['base_interrumpible_total'].mean(),
                                registrosTrimestre1_2017['volumetrica'].mean()]

    PromediosTrimestre2_2017 = [registrosTrimestre2_2017['base_firme_total'].mean(),
                                registrosTrimestre2_2017['base_firme_temporal_total'].mean(),
                                registrosTrimestre2_2017['base_interrumpible_total'].mean(),
                                registrosTrimestre2_2017['volumetrica'].mean()]

    PromediosTrimestre3_2017 = [registrosTrimestre3_2017['base_firme_total'].mean(),
                                registrosTrimestre3_2017['base_firme_temporal_total'].mean(),
                                registrosTrimestre3_2017['base_interrumpible_total'].mean(),
                                registrosTrimestre3_2017['volumetrica'].mean()]

    PromediosTrimestre4_2017 = [registrosTrimestre4_2017['base_firme_total'].mean(),
                                registrosTrimestre4_2017['base_firme_temporal_total'].mean(),
                                registrosTrimestre4_2017['base_interrumpible_total'].mean(),
                                registrosTrimestre4_2017['volumetrica'].mean()]

    # Valores del eje X, representan cada trimestre
    xAxis = ["Ene-Mar 2016", "Abr-Jun 2016", "Jul-Sep 2016", "Oct-Dic 2016", "Ene-Mar 2017", "Abr-Jun 2017",
             "Jul-Sep 2017", "Oct-Dic 2017"]

    # Valores del eje Y, cada uno representa el avance del promedio de cada tarifa a lo largo de los 2 años
    yAxisFirme = [PromediosTrimestre1_2016[0], PromediosTrimestre2_2016[0], PromediosTrimestre3_2016[0],
                  PromediosTrimestre4_2016[0], PromediosTrimestre1_2017[0], PromediosTrimestre2_2017[0],
                  PromediosTrimestre3_2017[0], PromediosTrimestre4_2017[0]]

    yAxisTemporal = [PromediosTrimestre1_2016[1], PromediosTrimestre2_2016[1], PromediosTrimestre3_2016[1],
                     PromediosTrimestre4_2016[1], PromediosTrimestre1_2017[1], PromediosTrimestre2_2017[1],
                     PromediosTrimestre3_2017[1], PromediosTrimestre4_2017[1]]

    yAxisInterr = [PromediosTrimestre1_2016[2], PromediosTrimestre2_2016[2], PromediosTrimestre3_2016[2],
                   PromediosTrimestre4_2016[2], PromediosTrimestre1_2017[2], PromediosTrimestre2_2017[2],
                   PromediosTrimestre3_2017[2], PromediosTrimestre4_2017[2]]

    yAxisVolumetrica = [PromediosTrimestre1_2016[3], PromediosTrimestre2_2016[3], PromediosTrimestre3_2016[3],
                        PromediosTrimestre4_2016[3], PromediosTrimestre1_2017[3], PromediosTrimestre2_2017[3],
                        PromediosTrimestre3_2017[3], PromediosTrimestre4_2017[3]]

    # Se crea la gráfica lineal
    plt.plot(xAxis, yAxisFirme, marker="o", color="r", label="Base Firme")
    plt.plot(xAxis, yAxisTemporal, marker="o", color="b", label="Base Temporal")
    plt.plot(xAxis, yAxisInterr, marker="o", color="g", label="Base Interrumpible")
    plt.plot(xAxis, yAxisVolumetrica, marker="o", color="y", label="Base Volumetrica")

    # Se personaliza la gráfica
    plt.title("Variacion de promedios del costo por cada tipo de tarifa durante 2016")
    plt.xlabel("Trimestres")
    plt.ylabel("Pesos*Gigajoule")
    plt.legend()

    # Se muestra la gráfica
    plt.show()

# Metodo para crear la grafica de barras
def graficoBarras():

    # Se genera el Dataframe origina en base al CSV de las tarifas por zona
    cursorPandas = ArchivoDriver.extraerCSVZonas()
    cursorPandas['fecha_inicio'] = pd.to_datetime(cursorPandas['fecha_inicio'], dayfirst=True)
    cursorPandas['fecha_fin'] = pd.to_datetime(cursorPandas['fecha_fin'], dayfirst=True)

    # Se crea un nuevo Dataframe por cada zona que existe
    registrosZonaSur = cursorPandas[cursorPandas['zona'] == 'Sur']
    registrosZonaCentro = cursorPandas[cursorPandas['zona'] == 'Centro']
    registrosZonaOccidente = cursorPandas[cursorPandas['zona'] == 'Occidente']
    registrosZonaGolfo = cursorPandas[cursorPandas['zona'] == 'Golfo']
    registrosZonaNorte = cursorPandas[cursorPandas['zona'] == 'Norte']
    registrosZonaIstmo = cursorPandas[cursorPandas['zona'] == 'Istmo']
    registrosZonaNacional = cursorPandas[cursorPandas['zona'] == 'Nacional']
    registrosZonaNacionalAB = cursorPandas[cursorPandas['zona'] == 'Nacional con AB']

    # Se guarda por cada zona el promedio de cada tipo de tarifa, tanto de capacidad como de uso
    PromediosZonaSur = [registrosZonaSur['capacidad_base_firme'].mean(),
                        registrosZonaSur['uso_base_firme'].mean(),
                        registrosZonaSur['capacidad_base_temporal'].mean(),
                        registrosZonaSur['uso_base_temporal'].mean(),
                        registrosZonaSur['maxima_base_interrumpible'].mean(),
                        registrosZonaSur['minima_base_interrumpible'].mean(),
                        registrosZonaSur['volumetrica'].mean()
                        ]

    PromediosZonaCentro = [registrosZonaCentro['capacidad_base_firme'].mean(),
                           registrosZonaCentro['uso_base_firme'].mean(),
                           registrosZonaCentro['capacidad_base_temporal'].mean(),
                           registrosZonaCentro['uso_base_temporal'].mean(),
                           registrosZonaCentro['maxima_base_interrumpible'].mean(),
                           registrosZonaCentro['minima_base_interrumpible'].mean(),
                           registrosZonaCentro['volumetrica'].mean()
                           ]

    PromediosZonaOccidente = [registrosZonaOccidente['capacidad_base_firme'].mean(),
                              registrosZonaOccidente['uso_base_firme'].mean(),
                              registrosZonaOccidente['capacidad_base_temporal'].mean(),
                              registrosZonaOccidente['uso_base_temporal'].mean(),
                              registrosZonaOccidente['maxima_base_interrumpible'].mean(),
                              registrosZonaOccidente['minima_base_interrumpible'].mean(),
                              registrosZonaOccidente['volumetrica'].mean()
                              ]

    PromediosZonaGolfo = [registrosZonaGolfo['capacidad_base_firme'].mean(),
                          registrosZonaGolfo['uso_base_firme'].mean(),
                          registrosZonaGolfo['capacidad_base_temporal'].mean(),
                          registrosZonaGolfo['uso_base_temporal'].mean(),
                          registrosZonaGolfo['maxima_base_interrumpible'].mean(),
                          registrosZonaGolfo['minima_base_interrumpible'].mean(),
                          registrosZonaGolfo['volumetrica'].mean()
                          ]

    PromediosZonaNorte = [registrosZonaNorte['capacidad_base_firme'].mean(),
                          registrosZonaNorte['uso_base_firme'].mean(),
                          registrosZonaNorte['capacidad_base_temporal'].mean(),
                          registrosZonaNorte['uso_base_temporal'].mean(),
                          registrosZonaNorte['maxima_base_interrumpible'].mean(),
                          registrosZonaNorte['minima_base_interrumpible'].mean(),
                          registrosZonaNorte['volumetrica'].mean()
                          ]

    PromediosZonaIstmo = [registrosZonaIstmo['capacidad_base_firme'].mean(),
                          registrosZonaIstmo['uso_base_firme'].mean(),
                          registrosZonaIstmo['capacidad_base_temporal'].mean(),
                          registrosZonaIstmo['uso_base_temporal'].mean(),
                          registrosZonaIstmo['maxima_base_interrumpible'].mean(),
                          registrosZonaIstmo['minima_base_interrumpible'].mean(),
                          registrosZonaIstmo['volumetrica'].mean()
                          ]

    PromediosZonaNacional = [registrosZonaNacional['capacidad_base_firme'].mean(),
                             registrosZonaNacional['uso_base_firme'].mean(),
                             registrosZonaNacional['capacidad_base_temporal'].mean(),
                             registrosZonaNacional['uso_base_temporal'].mean(),
                             registrosZonaNacional['maxima_base_interrumpible'].mean(),
                             registrosZonaNacional['minima_base_interrumpible'].mean(),
                             registrosZonaNacional['volumetrica'].mean()
                             ]

    PromediosZonaNacionalAB = [registrosZonaNacionalAB['capacidad_base_firme'].mean(),
                               registrosZonaNacionalAB['uso_base_firme'].mean(),
                               registrosZonaNacionalAB['capacidad_base_temporal'].mean(),
                               registrosZonaNacionalAB['uso_base_temporal'].mean(),
                               registrosZonaNacionalAB['maxima_base_interrumpible'].mean(),
                               registrosZonaNacionalAB['minima_base_interrumpible'].mean(),
                               registrosZonaNacionalAB['volumetrica'].mean()
                               ]

    # Se define el eje x
    zonasArr = ["Sur", "Centro", "Occidente", "Golfo", "Norte", "Istmo", "Nacional", "Nacional con AB"]
    xAxis = np.arange(len(zonasArr))

    # Se definen los ejes y, siendo los promedios de cada tipo de tarifa por cada zona
    yAxisCapacidadFirme = [PromediosZonaSur[0], PromediosZonaCentro[0], PromediosZonaOccidente[0],
                           PromediosZonaGolfo[0], PromediosZonaNorte[0], PromediosZonaIstmo[0],
                           PromediosZonaNacional[0], PromediosZonaNacionalAB[0]]

    yAxisUsoFirme = [PromediosZonaSur[1], PromediosZonaCentro[1], PromediosZonaOccidente[1],
                     PromediosZonaGolfo[1], PromediosZonaNorte[1], PromediosZonaIstmo[1],
                     PromediosZonaNacional[1], PromediosZonaNacionalAB[1]]

    yAxisCapacidadTemp = [PromediosZonaSur[2], PromediosZonaCentro[2], PromediosZonaOccidente[2],
                          PromediosZonaGolfo[2], PromediosZonaNorte[2], PromediosZonaIstmo[2],
                          PromediosZonaNacional[2], PromediosZonaNacionalAB[2]]

    yAxisUsoTemp = [PromediosZonaSur[3], PromediosZonaCentro[3], PromediosZonaOccidente[3],
                    PromediosZonaGolfo[3], PromediosZonaNorte[3], PromediosZonaIstmo[3],
                    PromediosZonaNacional[3], PromediosZonaNacionalAB[3]]

    yAxisMaxInterr = [PromediosZonaSur[4], PromediosZonaCentro[4], PromediosZonaOccidente[4],
                      PromediosZonaGolfo[4], PromediosZonaNorte[4], PromediosZonaIstmo[4],
                      PromediosZonaNacional[4], PromediosZonaNacionalAB[4]]

    yAxisMinInterr = [PromediosZonaSur[5], PromediosZonaCentro[5], PromediosZonaOccidente[5],
                      PromediosZonaGolfo[5], PromediosZonaNorte[5], PromediosZonaIstmo[5],
                      PromediosZonaNacional[5], PromediosZonaNacionalAB[5]]

    yAxisVolumetrica = [PromediosZonaSur[6], PromediosZonaCentro[6], PromediosZonaOccidente[6],
                        PromediosZonaGolfo[6], PromediosZonaNorte[6], PromediosZonaIstmo[6],
                        PromediosZonaNacional[6], PromediosZonaNacionalAB[6]]

    # Se contruye la grafica y se muestra
    barWidth = 0.3
    fig, ((ax1, ax2, ax3)) = plt.subplots(1,3)

    ax1.bar(xAxis, yAxisCapacidadFirme, color='b', width=barWidth, label="Base Firme")
    ax1.bar(xAxis+0.3, yAxisCapacidadTemp, color='r', width=barWidth, label="Base Temporal")
    ax1.bar(xAxis+0.6, yAxisMaxInterr, color='g', width=barWidth, label="Base Interrumpible")
    ax1.set_xticks(np.arange(len(zonasArr)))
    ax1.set_xticklabels(["Sur", "Centro", "Occidente", "Golfo", "Norte", "Istmo", "Nacional", "Nacional con AB"], rotation=45)
    ax1.set_title('Variacion de promedios del costo de capacidad \npor cada tipo de tarifa por zona')
    ax1.set(xlabel='Zonas', ylabel='Pesos*Gigajoule')
    ax1.legend()

    ax2.bar(xAxis, yAxisUsoFirme, color='b', width=barWidth, label="Base Firme")
    ax2.bar(xAxis + 0.3, yAxisUsoTemp, color='r', width=barWidth, label="Base Temporal")
    ax2.bar(xAxis + 0.6, yAxisMinInterr, color='g', width=barWidth, label="Base Interrumpible")
    ax2.set_xticks(np.arange(len(zonasArr)))
    ax2.set_xticklabels(["Sur", "Centro", "Occidente", "Golfo", "Norte", "Istmo", "Nacional", "Nacional con AB"], rotation=45)
    ax2.set_title('Variacion de promedios del costo de uso \npor cada tipo de tarifa por zona')
    ax2.set(xlabel='Zonas', ylabel='Pesos*Gigajoule')
    ax2.legend()

    ax3.bar(xAxis, yAxisVolumetrica, color='y', width=barWidth, label="Volumetrica")
    ax3.set_xticks(np.arange(len(zonasArr)))
    ax3.set_xticklabels(["Sur", "Centro", "Occidente", "Golfo", "Norte", "Istmo", "Nacional", "Nacional con AB"], rotation=45)
    ax3.set_title('Variacion de promedios del costo \nde la tarifa volumetrica por zona')
    ax3.set(xlabel='Zonas', ylabel='Pesos*Gigajoule')
    ax3.legend()

    plt.show()