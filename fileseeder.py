import os
import tkinter as tk
from tkinter import ttk

options = ["               ", "organismo", "molécula", "átomo"]
scss_files = {"organismo": "./templates/Class-Organisms.scss",
              "molécula": "./templates/Class-Molecules.scss",
              "átomo": "./templates/Class-Atoms.scss"}
tsx_files = {"organismo": "./templates/React-Organism.tsx",
             "molécula": "./templates/React-Molecule.tsx",
             "átomo": ""}

def fileseeder(scss_file, tsx_file, name, className, translation):
    # Crear directorio
    dir_path = os.path.join(os.getcwd(), name)
    os.mkdir(dir_path)
    print(f'{dir_path} creado')

    # Crear archivo SCSS
    with open(scss_file, 'r') as reference_file:
        code = reference_file.read().replace('${NAME}', className)
    scss_path = os.path.join(dir_path, className + ".scss")
    with open(scss_path, 'w') as new_file:
        new_file.write(code)
    print(f'{scss_path} creado')

    # Omitir creación de archivo TSX si la opción es "átomo"
    if scss_file == scss_files["átomo"]:
        return

    # Crear archivo TSX
    with open(tsx_file, 'r') as reference_file:
        code = reference_file.read().replace('${NAME}', name).replace('${className}', className)
        if translation:
            code = code.replace('${translation}', translation)
        else:
            code = code.replace('${translation}', '""')
        code = code.replace('${DIR_PATH}', os.getcwd())
        code = code.replace('${FILE_NAME}', name + ".tsx")
    tsx_path = os.path.join(dir_path, name + ".tsx")
    with open(tsx_path, 'w') as new_file:
        new_file.write(code)
    print(f'{tsx_path} creado')

# Generar archivos
def submit():
    fileseeder(scss_files[variable.get()], tsx_files[variable.get()], name_entry.get(), camel_to_kebab(name_entry.get()), translation_entry.get())
    root.destroy()

# Cambiar CamelCase a kebab-case
def camel_to_kebab(string):
    # Buscamos todas las letras mayúsculas en la cadena y las reemplazamos por "-letra"
    kebab = ''.join(['-' + i.lower() if i.isupper() else i for i in string])
    # Si la cadena empieza por mayúscula, eliminamos el primer "-"
    if kebab[0] == '-':
        kebab = kebab[1:]
    return kebab

# Crear ventana
root = tk.Tk()
root.title("Generador de archivos")
root.geometry("400x230+475+500")

# Crear menú de opciones
option_label = ttk.Label(root, text="Selecciona una opción:")
option_label.pack(pady=(10, 0))
variable = tk.StringVar(root)
variable.set(options[0])
option_menu = ttk.OptionMenu(root, variable, *options)
option_menu.pack(pady=(0, 10))

# Crear campos de entrada
name_label = ttk.Label(root, text="Ingresa un nombre (en CamelCase):")
name_label.pack(pady=(10, 0))
name_entry = ttk.Entry(root, width=30)
name_entry.pack()
translation_label = ttk.Label(root, text="Ingresa una traducción (opcional):")
translation_label.pack(pady=(10, 0))
translation_entry = ttk.Entry(root, width=30)
translation_entry.pack()

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
