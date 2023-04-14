import tkinter as tk
from tkinter import ttk
from functions.fileseeder import fileseeder

options = ["               ", "organismo", "molécula", "átomo"]
tipo = {"               ": None, "organismo": "org", "molécula": "mol", "átomo": "atom"}

# Generar archivos
def submit():
    if name_entry.get() == "":
        name = None
    else:
        name = name_entry.get()
    fileseeder(tipo[select.get()], name)
    

# Crear ventana
root = tk.Tk()
root.title("Generador de archivos")
root.geometry("400x200+475+500")

# Crear menú de opciones
option_label = ttk.Label(root, text="Selecciona una opción:")
option_label.pack(pady=(10, 0))
select = tk.StringVar(root)
select.set(options[0])
option_menu = ttk.OptionMenu(root, select, *options)
option_menu.pack(pady=(0, 10))

# Crear campo de nombre
name_label = ttk.Label(root, text="Ingresa un nombre (en CamelCase):")
name_label.pack(pady=(10, 0))
name_entry = ttk.Entry(root, width=30)
name_entry.pack()

# Función para pulsar el botón Generar
def enter_key(event):
    if event.keysym == 'Return':
        submit()

# Vincular la tecla Enter con la función de pulsar el botón Generar
root.bind('<Key>', enter_key)

# Crear botón de Generar
submit_button = ttk.Button(root, text="Generar", command=submit)
submit_button.pack(pady=(10, 0))

# Función para cerrar la ventana
def close_window(event):
    root.destroy()

# Vincular la tecla Esc con la función de cerrar la ventana
root.bind('<Escape>', close_window)

# Ejecutar ventana
root.mainloop()
