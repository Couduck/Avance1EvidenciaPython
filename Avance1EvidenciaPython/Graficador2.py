import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import ProcesosArchivo as ArchivoDriver

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
    plt.title("Variacion de promedios del costo por cada tipo de tarifa durante el periodo de 2016-2017")
    plt.xlabel("Trimestres")
    plt.ylabel("Pesos*Gigajoule")
    plt.legend()

    # Se muestra la gráfica
    plt.show()

# Metodo para crear la grafica de barras
def graficoBarras():
    cursorPandas = ArchivoDriver.extraerCSVPuntos()
    cursorPandas['fecha_inicio'] = pd.to_datetime(cursorPandas['fecha_inicio'], dayfirst=True)
    cursorPandas['fecha_fin'] = pd.to_datetime(cursorPandas['fecha_fin'], dayfirst=True)
    cursorPandas['base_firme_total'] = cursorPandas['capacidad_base_firme'] + cursorPandas['uso_base_firme']
    cursorPandas['base_firme_temporal_total'] = cursorPandas['capacidad_base_firme_temporal'] + cursorPandas[
        'uso_base_firme_temporal']
    cursorPandas['base_interrumpible_total'] = cursorPandas['capacidad_base_interrumpible'] + cursorPandas[
        'uso_base_interrumpible']

    #Debido a que solo nos interesan los maximos y minimos, solamente se utilizaran registros cuyo resultado de la suma de columnas anterior sea mayor a 0, esto evita que los valores minimos a buscar no sean iguales a 0
    cursorPandas = cursorPandas[(cursorPandas['base_firme_total'] > 0) &
                                (cursorPandas['base_firme_temporal_total'] > 0) &
                                (cursorPandas['base_interrumpible_total'] > 0) &
                                (cursorPandas['volumetrica'] > 0) ]

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

    # Se obtienen los maximos y minimos de cada tarifa por cada trimestre
    MaximosTrimestre1_2016 = [registrosTrimestre1_2016['base_firme_total'].max(),
                                registrosTrimestre1_2016['base_firme_temporal_total'].max(),
                                registrosTrimestre1_2016['base_interrumpible_total'].max(),
                                registrosTrimestre1_2016['volumetrica'].max()]

    MaximosTrimestre2_2016 = [registrosTrimestre2_2016['base_firme_total'].max(),
                                registrosTrimestre2_2016['base_firme_temporal_total'].max(),
                                registrosTrimestre2_2016['base_interrumpible_total'].max(),
                                registrosTrimestre2_2016['volumetrica'].max()]

    MaximosTrimestre3_2016 = [registrosTrimestre3_2016['base_firme_total'].max(),
                                registrosTrimestre3_2016['base_firme_temporal_total'].max(),
                                registrosTrimestre3_2016['base_interrumpible_total'].max(),
                                registrosTrimestre3_2016['volumetrica'].max()]

    MaximosTrimestre4_2016 = [registrosTrimestre4_2016['base_firme_total'].max(),
                                registrosTrimestre4_2016['base_firme_temporal_total'].max(),
                                registrosTrimestre4_2016['base_interrumpible_total'].max(),
                                registrosTrimestre4_2016['volumetrica'].max()]

    MaximosTrimestre1_2017 = [registrosTrimestre1_2017['base_firme_total'].max(),
                                registrosTrimestre1_2017['base_firme_temporal_total'].max(),
                                registrosTrimestre1_2017['base_interrumpible_total'].max(),
                                registrosTrimestre1_2017['volumetrica'].max()]

    MaximosTrimestre2_2017 = [registrosTrimestre2_2017['base_firme_total'].max(),
                                registrosTrimestre2_2017['base_firme_temporal_total'].max(),
                                registrosTrimestre2_2017['base_interrumpible_total'].max(),
                                registrosTrimestre2_2017['volumetrica'].max()]

    MaximosTrimestre3_2017 = [registrosTrimestre3_2017['base_firme_total'].max(),
                                registrosTrimestre3_2017['base_firme_temporal_total'].max(),
                                registrosTrimestre3_2017['base_interrumpible_total'].max(),
                                registrosTrimestre3_2017['volumetrica'].max()]

    MaximosTrimestre4_2017 = [registrosTrimestre4_2017['base_firme_total'].max(),
                                registrosTrimestre4_2017['base_firme_temporal_total'].max(),
                                registrosTrimestre4_2017['base_interrumpible_total'].max(),
                                registrosTrimestre4_2017['volumetrica'].max()]



    MinimosTrimestre1_2016 = [registrosTrimestre1_2016['base_firme_total'].min(),
                              registrosTrimestre1_2016['base_firme_temporal_total'].min(),
                              registrosTrimestre1_2016['base_interrumpible_total'].min(),
                              registrosTrimestre1_2016['volumetrica'].min()]

    MinimosTrimestre2_2016 = [registrosTrimestre2_2016['base_firme_total'].min(),
                              registrosTrimestre2_2016['base_firme_temporal_total'].min(),
                              registrosTrimestre2_2016['base_interrumpible_total'].min(),
                              registrosTrimestre2_2016['volumetrica'].min()]

    MinimosTrimestre3_2016 = [registrosTrimestre3_2016['base_firme_total'].min(),
                              registrosTrimestre3_2016['base_firme_temporal_total'].min(),
                              registrosTrimestre3_2016['base_interrumpible_total'].min(),
                              registrosTrimestre3_2016['volumetrica'].min()]

    MinimosTrimestre4_2016 = [registrosTrimestre4_2016['base_firme_total'].min(),
                              registrosTrimestre4_2016['base_firme_temporal_total'].min(),
                              registrosTrimestre4_2016['base_interrumpible_total'].min(),
                              registrosTrimestre4_2016['volumetrica'].min()]

    MinimosTrimestre1_2017 = [registrosTrimestre1_2017['base_firme_total'].min(),
                              registrosTrimestre1_2017['base_firme_temporal_total'].min(),
                              registrosTrimestre1_2017['base_interrumpible_total'].min(),
                              registrosTrimestre1_2017['volumetrica'].min()]

    MinimosTrimestre2_2017 = [registrosTrimestre2_2017['base_firme_total'].min(),
                              registrosTrimestre2_2017['base_firme_temporal_total'].min(),
                              registrosTrimestre2_2017['base_interrumpible_total'].min(),
                              registrosTrimestre2_2017['volumetrica'].min()]

    MinimosTrimestre3_2017 = [registrosTrimestre3_2017['base_firme_total'].min(),
                              registrosTrimestre3_2017['base_firme_temporal_total'].min(),
                              registrosTrimestre3_2017['base_interrumpible_total'].min(),
                              registrosTrimestre3_2017['volumetrica'].min()]

    MinimosTrimestre4_2017 = [registrosTrimestre4_2017['base_firme_total'].min(),
                              registrosTrimestre4_2017['base_firme_temporal_total'].min(),
                              registrosTrimestre4_2017['base_interrumpible_total'].min(),
                              registrosTrimestre4_2017['volumetrica'].min()]

    # Valores del eje X, representan cada trimestre
    fechas = ["Ene-Mar 2016", "Abr-Jun 2016", "Jul-Sep 2016", "Oct-Dic 2016", "Ene-Mar 2017", "Abr-Jun 2017",
             "Jul-Sep 2017", "Oct-Dic 2017"]
    xAxis = np.arange(len(fechas))

    # Valores del eje Y, cada uno representa el avance del maximo y minimo de cada tarifa a lo largo de los 2 años
    yAxisFirmeMax = [MaximosTrimestre1_2016[0], MaximosTrimestre2_2016[0], MaximosTrimestre3_2016[0],
                  MaximosTrimestre4_2016[0], MaximosTrimestre1_2017[0], MaximosTrimestre2_2017[0],
                  MaximosTrimestre3_2017[0], MaximosTrimestre4_2017[0]]

    yAxisTemporalMax = [MaximosTrimestre1_2016[1], MaximosTrimestre2_2016[1], MaximosTrimestre3_2016[1],
                  MaximosTrimestre4_2016[1], MaximosTrimestre1_2017[1], MaximosTrimestre2_2017[1],
                  MaximosTrimestre3_2017[1], MaximosTrimestre4_2017[1]]

    yAxisInterrMax = [MaximosTrimestre1_2016[2], MaximosTrimestre2_2016[2], MaximosTrimestre3_2016[2],
                  MaximosTrimestre4_2016[2], MaximosTrimestre1_2017[2], MaximosTrimestre2_2017[2],
                  MaximosTrimestre3_2017[2], MaximosTrimestre4_2017[2]]

    yAxisVolumetricaMax = [MaximosTrimestre1_2016[3], MaximosTrimestre2_2016[3], MaximosTrimestre3_2016[3],
                  MaximosTrimestre4_2016[3], MaximosTrimestre1_2017[3], MaximosTrimestre2_2017[3],
                  MaximosTrimestre3_2017[3], MaximosTrimestre4_2017[3]]



    yAxisFirmeMin = [MinimosTrimestre1_2016[0], MinimosTrimestre2_2016[0], MinimosTrimestre3_2016[0],
                     MinimosTrimestre4_2016[0], MinimosTrimestre1_2017[0], MinimosTrimestre2_2017[0],
                     MinimosTrimestre3_2017[0], MinimosTrimestre4_2017[0]]

    yAxisTemporalMin = [MinimosTrimestre1_2016[1], MinimosTrimestre2_2016[1], MinimosTrimestre3_2016[1],
                     MinimosTrimestre4_2016[1], MinimosTrimestre1_2017[1], MinimosTrimestre2_2017[1],
                     MinimosTrimestre3_2017[1], MinimosTrimestre4_2017[1]]

    yAxisInterrMin = [MinimosTrimestre1_2016[2], MinimosTrimestre2_2016[2], MinimosTrimestre3_2016[2],
                     MinimosTrimestre4_2016[2], MinimosTrimestre1_2017[2], MinimosTrimestre2_2017[2],
                     MinimosTrimestre3_2017[2], MinimosTrimestre4_2017[2]]

    yAxisVolumetricaMin = [MinimosTrimestre1_2016[3], MinimosTrimestre2_2016[3], MinimosTrimestre3_2016[3],
                     MinimosTrimestre4_2016[3], MinimosTrimestre1_2017[3], MinimosTrimestre2_2017[3],
                     MinimosTrimestre3_2017[3], MinimosTrimestre4_2017[3]]

    # Se construye la grafica y se muestra
    barWidth = 0.3
    fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(1,4)

    ax1.bar(xAxis, yAxisFirmeMax, color='r', width=barWidth, label="Tarifa Maxima")
    ax1.bar(xAxis+0.3, yAxisFirmeMin, color='b', width=barWidth, label="Tarifa Minima")
    ax1.set_xticks(np.arange(len(fechas)))
    ax1.set_xticklabels(["Ene-Mar 2016", "Abr-Jun 2016", "Jul-Sep 2016", "Oct-Dic 2016", "Ene-Mar 2017", "Abr-Jun 2017",
             "Jul-Sep 2017", "Oct-Dic 2017"], rotation=45)
    ax1.set_title('Valores Minimos y Maximos \nen la tarifa firme \ndurante los años 2016-2017')
    ax1.set(xlabel='Zonas', ylabel='Pesos*Gigajoule')
    ax1.legend()

    ax2.bar(xAxis, yAxisTemporalMax, color='r', width=barWidth, label="Tarifa Maxima")
    ax2.bar(xAxis + 0.3, yAxisTemporalMin, color='b', width=barWidth, label="Tarifa Minima")
    ax2.set_xticks(np.arange(len(fechas)))
    ax2.set_xticklabels(["Ene-Mar 2016", "Abr-Jun 2016", "Jul-Sep 2016", "Oct-Dic 2016", "Ene-Mar 2017", "Abr-Jun 2017",
                         "Jul-Sep 2017", "Oct-Dic 2017"], rotation=45)
    ax2.set_title('Valores Minimos y Maximos \nen la tarifa temporal \ndurante los años 2016-2017')
    ax2.set(xlabel='Zonas', ylabel='Pesos*Gigajoule')
    ax2.legend()

    ax3.bar(xAxis, yAxisInterrMax, color='r', width=barWidth, label="Tarifa Maxima")
    ax3.bar(xAxis + 0.3, yAxisInterrMin, color='b', width=barWidth, label="Tarifa Minima")
    ax3.set_xticks(np.arange(len(fechas)))
    ax3.set_xticklabels(["Ene-Mar 2016", "Abr-Jun 2016", "Jul-Sep 2016", "Oct-Dic 2016", "Ene-Mar 2017", "Abr-Jun 2017",
                         "Jul-Sep 2017", "Oct-Dic 2017"], rotation=45)
    ax3.set_title('Valores Minimos y Maximos \nen la tarifa interrumpible \ndurante los años 2016-2017')
    ax3.set(xlabel='Zonas', ylabel='Pesos*Gigajoule')
    ax3.legend()

    ax4.bar(xAxis, yAxisVolumetricaMax, color='r', width=barWidth, label="Tarifa Maxima")
    ax4.bar(xAxis + 0.3, yAxisVolumetricaMin, color='b', width=barWidth, label="Tarifa Minima")
    ax4.set_xticks(np.arange(len(fechas)))
    ax4.set_xticklabels(["Ene-Mar 2016", "Abr-Jun 2016", "Jul-Sep 2016", "Oct-Dic 2016", "Ene-Mar 2017", "Abr-Jun 2017",
                         "Jul-Sep 2017", "Oct-Dic 2017"], rotation=45)
    ax4.set_title('Valores Minimos y Maximos \nen la tarifa volumetrica \ndurante los años 2016-2017')
    ax4.set(xlabel='Zonas', ylabel='Pesos*Gigajoule')
    ax4.legend()

    plt.show()

ejecucion()