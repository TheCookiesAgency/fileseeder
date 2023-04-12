import os
from .camel_to_kebab import camel_to_kebab

def fileseeder( tipo, name):

    # Creación de la variable className
    className = camel_to_kebab(name)

    # Restricción de la variable type
    if tipo == "org":
        scss_file = "./templates/Class-Organism.scss"
        tsx_file = "./templates/React-Organism.tsx"
    if tipo == "mol":
        scss_file = "./templates/Class-Molecule.scss"
        tsx_file = "./templates/React-Molecule.tsx"
    if tipo == "atom":
        scss_file = "./templates/Class-Atom.scss"
    if tipo not in ["org", "mol", "atom"]:
        return

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
    if tipo == "atom":
        return

    # Crear archivo TSX
    with open(tsx_file, 'r') as reference_file:
        code = reference_file.read().replace('${NAME}', name).replace('${className}', className)
        code = code.replace('${DIR_PATH}', os.getcwd())
        code = code.replace('${FILE_NAME}', name + ".tsx")
    tsx_path = os.path.join(dir_path, name + ".tsx")
    with open(tsx_path, 'w') as new_file:
        new_file.write(code)
    print(f'{tsx_path} creado')