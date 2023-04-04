# Importaciones del conector y random
import mysql.connector as mysql
import ProcesosArchivo as ArchivoDriver
import pandas as pd


def ejecucion():
    # Se crea la conexión
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="",
    )

    # Se extrae el CSV de puntos y se configuran las fechas
    cursorPandasPuntos = ArchivoDriver.extraerCSVPuntos()
    cursorPandasPuntos['fecha_inicio'] = pd.to_datetime(cursorPandasPuntos['fecha_inicio'], dayfirst=True)
    cursorPandasPuntos['fecha_inicio'] = cursorPandasPuntos['fecha_inicio'].dt.date
    cursorPandasPuntos['fecha_fin'] = pd.to_datetime(cursorPandasPuntos['fecha_fin'], dayfirst=True)
    cursorPandasPuntos['fecha_fin'] = cursorPandasPuntos['fecha_fin'].dt.date

    # Lo mismo pero con zonas
    cursorPandasZonas = ArchivoDriver.extraerCSVZonas()
    cursorPandasZonas['fecha_inicio'] = pd.to_datetime(cursorPandasZonas['fecha_inicio'], dayfirst=True)
    cursorPandasZonas['fecha_inicio'] = cursorPandasZonas['fecha_inicio'].dt.date
    cursorPandasZonas['fecha_fin'] = pd.to_datetime(cursorPandasZonas['fecha_fin'], dayfirst=True)
    cursorPandasZonas['fecha_fin'] = cursorPandasZonas['fecha_fin'].dt.date

    # Se crea el cursor
    cursorDB = db.cursor(buffered=True)

    # Definición del nombre de la base de datos
    nombre = "bigData_Evidencia1"

    # Base de Datos creada en caso de no existir
    cursorDB.execute(f"CREATE DATABASE IF NOT EXISTS {nombre}")
    db.database = nombre

    # Tablas creadas en caso de no existir
    cursorDB.execute("CREATE TABLE IF NOT EXISTS tabla_TarifasPuntos"
                     "(id int PRIMARY KEY NOT NULL AUTO_INCREMENT,"
                     " zona_inyeccion VARCHAR(15) NOT NULL,"
                     " zona_extraccion VARCHAR(15) NOT NULL,"
                     " capacidad_base_firme FLOAT(7,5) NOT NULL,"
                     " uso_base_firme FLOAT(7,5) NOT NULL,"
                     " capacidad_base_firme_temporal FLOAT(7,5) NOT NULL,"
                     " uso_base_firme_temporal FLOAT(7,5) NOT NULL,"
                     " capacidad_base_interrumpible FLOAT(7,5) NOT NULL,"
                     " uso_base_interrumpible FLOAT(7,5) NOT NULL, "
                     " volumetrica FLOAT(7,5) NOT NULL,"
                     " fecha_inicio DATE NOT NULL,"
                     " fecha_fin DATE NOT NULL)")

    # Se manda a llamar a todos los registros de la tabla, en caso de existir solo se imprimen, mientras que si no hay nada, se generan y se insertan en la tabla
    cursorDB.execute("SELECT * FROM tabla_TarifasPuntos")

    if cursorDB.rowcount == 0:

        for i, row in cursorPandasPuntos.iterrows():

            sql = "INSERT INTO tabla_TarifasPuntos (zona_inyeccion, zona_extraccion, capacidad_base_firme, uso_base_firme, capacidad_base_firme_temporal, uso_base_firme_temporal, capacidad_base_interrumpible, uso_base_interrumpible, volumetrica, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursorDB.execute(sql, (f'{tuple(row)[0]}', f'{tuple(row)[1]}', f'{tuple(row)[2]}', f'{tuple(row)[3]}', f'{tuple(row)[4]}', f'{tuple(row)[5]}', f'{tuple(row)[6]}', f'{tuple(row)[7]}', f'{tuple(row)[8]}', f'{tuple(row)[9]}', f'{tuple(row)[10]}') )

        db.commit()

    print("-----------------------------\nTabla de tarifas por puntos\n\n")
    cursorDB.execute("SELECT * FROM tabla_TarifasPuntos")
    for x in cursorDB:
        print(x)
    print("-----------------------------\n\n")

    # Tablas creadas en caso de no existir
    cursorDB.execute("CREATE TABLE IF NOT EXISTS tabla_TarifasZonas"
                     "(id int PRIMARY KEY NOT NULL AUTO_INCREMENT,"
                     " zona VARCHAR(15) NOT NULL,"
                     " capacidad_base_firme FLOAT(7,5) NOT NULL,"
                     " uso_base_firme FLOAT(7,5) NOT NULL,"
                     " capacidad_base_firme_temporal FLOAT(7,5) NOT NULL,"
                     " uso_base_firme_temporal FLOAT(7,5) NOT NULL,"
                     " maxima_base_interrumpible FLOAT(7,5) NOT NULL,"
                     " minima_base_interrumpible FLOAT(7,5) NOT NULL,"
                     " volumetrica FLOAT(7,5) NOT NULL,"
                     " fecha_inicio DATE NOT NULL,"
                     " fecha_fin DATE NOT NULL)")

    # Misma situación pero con la tabla de zonas
    cursorDB.execute("SELECT * FROM tabla_TarifasZonas")

    if cursorDB.rowcount == 0:

        for i, row in cursorPandasZonas.iterrows():
            sql = "INSERT INTO tabla_TarifasZonas (zona, capacidad_base_firme, uso_base_firme, capacidad_base_firme_temporal, uso_base_firme_temporal, maxima_base_interrumpible, minima_base_interrumpible, volumetrica, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursorDB.execute(sql, (
            f'{tuple(row)[0]}', f'{tuple(row)[1]}', f'{tuple(row)[2]}', f'{tuple(row)[3]}', f'{tuple(row)[4]}',
            f'{tuple(row)[5]}', f'{tuple(row)[6]}', f'{tuple(row)[7]}', f'{tuple(row)[8]}', f'{tuple(row)[9]}'))

        db.commit()

    print("-----------------------------\nTabla de tarifas por zonas\n\n")
    cursorDB.execute("SELECT * FROM tabla_TarifasZonas")
    for x in cursorDB:
        print(x)
    print("-----------------------------\n\n")

    db.close()