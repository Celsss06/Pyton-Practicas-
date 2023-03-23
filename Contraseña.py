import tkinter as tk
def iniciar_sesion():
    usuario = nombre_usuario.get()
    password = contrasena_usuario.get()
    matricula = matricula_usuario.get ()
    if usuario == "celss03" and password == "06062023" and matricula== "04220012":
        resultado.config(text="Inicio de sesión exitoso")
    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos, intente de nuevo")

ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.configure(bg= "orchid1", padx=20)

# Crear campos de entrada para el nombre de usuario y la contraseña
nombre_usuario = tk.Entry(ventana)
label= tk.Label (text="Usuario")
label.config (fg= "Black", bg= "orchid1", font= ("Snow Bright", 13))
label.pack (padx=0)
nombre_usuario.pack(pady=10)

matricula_usuario = tk.Entry (ventana)
label= tk.Label ( text= "Matricula")
label.config (fg= "Black", bg= "orchid1", font= ("Snow Bright", 13))
label.pack (pady=0)
matricula_usuario.pack (pady=10)

contrasena_usuario = tk.Entry(ventana, show="★")
label= tk.Label ( text= "Contraseña")
label.config (fg= "Black", bg= "orchid1", font= ("Snow Bright", 13))
label.pack (pady=0)
contrasena_usuario.pack(pady=10)


# Crear botones para iniciar sesión y salir
iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
iniciar_sesion.pack(padx=10, pady=10)
salir = tk.Button(ventana, text="Salir", command=ventana.quit)
salir.pack()

# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, bg= "orchid1")
resultado.pack(pady=10)

ventana.mainloop()