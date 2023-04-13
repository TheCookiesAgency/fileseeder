import os
from .camel_to_kebab import camel_to_kebab

def fileseeder( tipo=None, name=""):

    # Definir el directorio components para crear los subdirectorios
    dir_path = os.path.join(os.getcwd(), 'components')

    # Definir los subdirectorios de components
    org_path = os.path.join(dir_path, 'org')
    mol_path = os.path.join(dir_path, 'mol')
    atom_path = os.path.join(dir_path, 'atom')

    # Restricción de la variable name
    if name == "":
        print(f'Debes agregar el nombre del componente que quieres crear (CamelCase)')
        return

    # Restricción de la variable type
    if tipo == "org":
        scss_file = os.path.join(dir_path, 'templates/Class-Organism.scss')
        tsx_file = os.path.join(dir_path, 'templates/React-Organism.tsx')
    if tipo == "mol":
        scss_file = os.path.join(dir_path, 'templates/Class-Molecule.scss')
        tsx_file = os.path.join(dir_path, 'templates/React-Molecule.tsx')
    if tipo == "atom":
        scss_file = os.path.join(dir_path, 'templates/Class-Atom.scss')
    if tipo not in ["org", "mol", "atom"]:
        print(f'Debes especificar si quieres crear un organismo, una molécula o un átomo')
        return

    #Primera letra siempre mayúscula
    name = name[0].upper() + name[1:]

    # Creación de la variable className
    className = camel_to_kebab(name)

    # Crear el directorio components si no existe
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

        # Crear los subdirectorios 'org', 'mol' y 'atom' dentro del directorio components
        if not os.path.exists(org_path):
            os.mkdir(org_path)
        if not os.path.exists(mol_path):
            os.mkdir(mol_path)
        if not os.path.exists(atom_path):
            os.mkdir(atom_path)

    # Asignar directorio dependiendo del tipo
    if tipo == "org":
        dir_path = org_path
    if tipo == "mol":
        dir_path = mol_path
    if tipo == "atom":
        dir_path = atom_path

    # Comprobar directorio
    dir_path = os.path.join(dir_path, name)
    if os.path.exists(dir_path):
        print(f'Este componente ya existe, por favor inserte otro nombre (CamelCase)')
    else:

        # Crear directorio
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
            code = code.replace('${DIR_PATH}', dir_path)
            code = code.replace('${FILE_NAME}', name + ".tsx")
        tsx_path = os.path.join(dir_path, name + ".tsx")
        with open(tsx_path, 'w') as new_file:
            new_file.write(code)
        print(f'{tsx_path} creado')