import tkinter
import tkinter as tk


class MenuScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Ejemplo de menu de un videojuego ")

        # Creamos el menú superior
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar,bg= "rosy brown")


        # Creamos las opciones del menú
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Cuenta existente", command=self.open_file)
        self.file_menu.add_command(label="Crear cuenta", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.quit_program)
        self.menu_bar.add_cascade(label="Iniciar sesion", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Guia", command=self.copy)
        self.edit_menu.add_command(label="Opciones", command=self.paste)
        self.menu_bar.add_cascade(label="¿Cómo jugar?", menu=self.edit_menu)

        # Agregamos algunos widgets a la pantalla
        self.configure(bg= "rosy brown")
        self.label = tk.Label(self, text="¡Bienvenido al juego!", font= ("Britannic Bold", 20), bg= "rosy brown")
        self.label.pack(pady=100)
        self.button = tk.Button(self, text="Comenzar", command=self.press_button, font= ("Britannic Bold", 15), bg="indian red")
        self.button.pack()

        self.pack()


    def open_file(self):
        print("Cuenta existente")

    def save_file(self):
        print("Crear cuenta")

    def quit_program(self):
        self.master.quit()

    def copy(self):
        print("Guia")

    def paste(self):
        print("Opciones")

    def press_button(self):
        print("Botón presionado")


root = tk.Tk()
root.geometry("420x380")
app = MenuScreen(root)
app.mainloop()