from tkinter import *
from tkinter import messagebox
import sqlite3
from conexionBBDD import *


root = Tk()

root.title("CRUD para gestión de BBDD")
icono = "C:\DESARROLLO\gallo.ico"
root.iconbitmap(icono)

#---------------FUNCIONES------------#


def salirAplicacion():

    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if valor == "yes":
        root.destroy()


def limpiarCampos():

    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    textoComentario.delete(1.0, END)


def crear():

    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    datos = miNombre.get(), miPass.get(), miApellido.get(
    ), miDireccion.get(), textoComentario.get("1.0", END)
    """
    miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, '" + miNombre.get() +
                     "','" + miPass.get() +
                     "','" + miApellido.get() +
                     "','" + miDireccion.get() +
                     "','" + textoComentario.get("1.0", END)+"')")
    """
    miCursor.execute(
        "INSERT INTO DATOS_USUARIOS VALUES(NULL,?,?,?,?,?)", (datos))

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro realizado correctamente")


def leer():

    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID=" + miId.get())

    el_usuario = miCursor.fetchall()

    for usuario in el_usuario:

        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miPass.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5])

    miConexion.commit()


def actualizar():

    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    datos = miNombre.get(), miPass.get(), miApellido.get(
    ), miDireccion.get(), textoComentario.get("1.0", END)
    """
    miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO ='" + miNombre.get() +
                     "', PASSWORD='" + miPass.get() +
                     "', APELLIDO='" + miApellido.get() +
                     "', DIRECCION='" + miDireccion.get() +
                     "', COMENTARIO='" + textoComentario.get("1.0", END) +
                     "' WHERE ID=" + miId.get())
    """
    miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO =?, PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIO=? " +
                     "WHERE ID=" + miId.get(), (datos))
    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado correctamente")


def eliminar():

    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro borrado correctamente")


#----------MENÚ SUPERIOR------------#

barraMenu = Menu(root)
root.config(menu=barraMenu, width=500, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(bbddMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos", command=limpiarCampos)


crudMenu = Menu(bbddMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#---------ZONA DE CAMPOS DE DATOS---------#

miFrame = Frame(root)
miFrame.pack()

idLabel = Label(miFrame, text="Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidosLabel = Label(miFrame, text="Apellidos: ")
apellidosLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)


passwordLabel = Label(miFrame, text="Password: ")
passwordLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

textoLabel = Label(miFrame, text="Texto: ")
textoLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

miId = StringVar()
miApellido = StringVar()
miNombre = StringVar()
miPass = StringVar()
miDireccion = StringVar()

cuadroID = Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red")

cuadroApellidos = Entry(miFrame, textvariable=miApellido)
cuadroApellidos.grid(row=2, column=1, padx=10, pady=10)

cuadroPassword = Entry(miFrame, textvariable=miPass)
cuadroPassword.grid(row=3, column=1, padx=10, pady=10)
cuadroPassword.config(show="*")

cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)


#---------ZONA DE BOTONES----------#

botonesFrame = Frame(root)
botonesFrame.pack()

botonCrear = Button(botonesFrame, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer = Button(botonesFrame, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar = Button(botonesFrame, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar = Button(botonesFrame, text="Borrar", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()
