import sqlite3
from tkinter import messagebox


def conexionBBDD():

    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    try:

        miCursor.execute('''
            CREATE TABLE DATOS_USUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                PASSWORD VARCHAR(50),
                APELLIDO VARCHAR(50),
                DIRECCION VARCHAR(50),
                COMENTARIO VARCHAR(50)
            )
        ''')

        messagebox.showinfo("BBDD","BBDD creada con exito")

    except:

        messagebox.showwarning("Atención", "La BBDD ya existe")
