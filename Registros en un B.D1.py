import tkinter as tk
from tkinter import messagebox
import sqlite3


def conectar_db():
    Co= sqlite3.connect("ESCUELA.db")
    Co.execute(""" create table if not exists alumnos( id integer primary key AUTOINCREMENT, nombre varchar, edad integer)""")
    Co.close()


def guardar_alumno():
    Co = sqlite3.connect("ESCUELA.db")
    if name.get() == "" or age.get() == "":
        messagebox.showerror("Error, va de nuevo")
        return
    int_age = int(age.get())
    print(int_age)
    print(name.get())
    Co.execute("insert into ALUMNOS(nombre, edad) values (?,?)", (name.get(), int_age))
    Co.commit()
    Co.close()
    ventana_nuevo.destroy()
    actualiza_listado()


def get_alumnos():
    conexion = sqlite3.connect("ESCUELA.db")
    cursor = conexion.cursor()
    registros_raw = cursor.execute("select * from ALUMNOS")
    registros_fetch = registros_raw.fetchall()
    print(registros_fetch)
    global registros
    registros = registros_fetch
    cursor.close()


def actualiza_listado():
    registros_lb.delete(0, tk.END)
    get_alumnos()
    for registro in registros:
        registros_lb.insert(tk.END, registro)



def nuevo_alumno(event=None):
    ventana_nuevoA = tk.Toplevel(ventana)
    ventana_nuevoA.title("ALUMNO NUEVO")
    # Crear la etiqueta y el campo para el nombre
    name_label = tk.Label(ventana_nuevoA, text="Nombre:", bg =  "dark turquoise")
    name_label.grid(row=0, column=0, padx=(10, 0))

    name_entry = tk.Entry(ventana_nuevoA)
    name_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))

    # Crear la etiqueta y el campo de entrada para la edad
    age_label = tk.Label(ventana_nuevoA, text="Edad:", bg= "medium turquoise")
    age_label.grid(row=1, column=0, padx=(10,0))

    age_entry = tk.Entry(ventana_nuevoA)
    age_entry.grid(row=1, column=1, padx=(0, 10))

    # Crear la etiqueta y el campo de entrada para la matricula
    age_label = tk.Label(ventana_nuevoA, text="Matricula:", bg="turquoise")
    age_label.grid(row=2, column=0, padx=(10, 0))

    age_entry = tk.Entry(ventana_nuevoA)
    age_entry.grid(row=2, column=1, padx=(0, 10))

    global name
    name = name_entry
    global age
    age = age_entry
    global ventana_nuevo
    ventana_nuevo = ventana_nuevoA

    # Crear el botón para enviar los datos
    submit_button = tk.Button(ventana_nuevoA, text="Guardar", command=guardar_alumno)
    submit_button.grid(row=4, column= 4, columnspan=2, pady=20, padx=20)


conectar_db()
get_alumnos()
ventana = tk.Tk()
ventana.title("Registro de Alumnos")
ventana.config(width=400, height=300, bg= "cyan")
barra_menus = tk.Menu()
# Crear el primer menú.
menu_alumnos = tk.Menu(barra_menus, tearoff=False)
# Agregarlo a la barra.
barra_menus.add_cascade(menu=menu_alumnos, label="Alumnos")
menu_alumnos.add_command(label="Agregar Alumno", command=nuevo_alumno)
ventana.config(menu=barra_menus)
registros_lb = tk.Listbox(ventana)
for registro in registros:
    registros_lb.insert(tk.END, registro)

registros_lb.pack(pady=20, padx=20)
ventana.mainloop()