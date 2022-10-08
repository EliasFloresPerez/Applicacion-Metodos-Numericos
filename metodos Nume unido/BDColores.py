"""
    Este archivo se encarga de administrar la base de datos de los temas de la aplicacion
    ya sea para guardarlo o para cargar un tema.

"""

#Se uso sqlite porque es muy pequeña la base de datos
import sqlite3


db = "Colores.db"

#Coneccion a la base de datos
def db_connect(db_path = db):
    conexion=sqlite3.connect(db,check_same_thread=False)
    return conexion


#Guardar temas en la base
def Insertar_Color(nom,tri):
    
    try :
        sql = """
            INSERT INTO Lista ("Nombre","TrioColor")
            VALUES (?,?)"""
        cur.execute(sql, (nom,tri))
        con.commit()
        print("Guardado")
    except:
        print("Error ya existe")
        return -1
    
    return cur.lastrowid

#Borra temas de la base de datos
def Eliminar_Color(nom):
    
    try :
        sql = """
            Delete  from Lista Where Nombre = '{0}'""".format(nom)
        cur.execute(sql)
        con.commit()
        print("Eliminado")
    except:
        print("Error ")
        return -1
    
    return cur.lastrowid

#Para retornar los temas disponibles al combobox
def Retornar_Todo(orden = ""):
    cur.execute("SELECT * From Lista {0}".format(orden))
    resultados = cur.fetchall()
    
    if len(resultados) > 0:
            return resultados
    else:
        return []

#Para gurdar el tema cuando inicia la app
def Guardar_Color(numero,fondo):
    cur.execute("Update Ultimo set Numero = '{0}', Fondo = '{1}' ".format(numero,fondo))
    con.commit()

#Cuando se consulta un tema en el combobox de configuracion
#Esta funcion devolvera los colores de este tema
def Devolver_Color():
    try:
        cur.execute("SELECT * From Ultimo")
        resultados = cur.fetchall()
        return resultados
    except:
        print("Error en la ultima base")
        sql = """
            INSERT INTO Ultimo ("Numero","Fondo")
            VALUES (?,?)"""
        cur.execute(sql, ("#2B4352-#00876E-#00B488","#EBEBEB"))
        con.commit()
        return 0

con = db_connect()
cur = con.cursor()


