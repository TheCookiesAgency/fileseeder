import os
from .camel_to_kebab import camel_to_kebab
from .delete_dir import delete_dir

def fileseeder( tipo = None, name = None, delete = None ):

    # Definir carpeta raiz del proyecto
    root_path = os.getcwd()

    # Definir el directorio donde se encuentra instalado fileseeder
    fs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Definir los directorios donde irá cada componente
    org_path = os.path.join(root_path, 'web/src/sections')
    mol_path = os.path.join(root_path, 'web/src/modules')
    atom_path = os.path.join(root_path, 'web/src/styles/components/atoms')

    # Restricción de la variable name
    if name == None or name.startswith("--"):
        print(f'Debes agregar el nombre del componente que quieres crear (CamelCase)')
        return

    # Restricción de la variable type y definir archivos y directorio
    if tipo == "org":
        scss_file = os.path.join(fs_path, 'templates/Class-Organism.scss')
        tsx_file = os.path.join(fs_path, 'templates/React-Organism.tsx')
        destination_path = org_path
        tipo_componente = "El organismo"
    if tipo == "mol":
        scss_file = os.path.join(fs_path, 'templates/Class-Molecule.scss')
        tsx_file = os.path.join(fs_path, 'templates/React-Molecule.tsx')
        destination_path = mol_path
        tipo_componente = "La molécula"
    if tipo == "atom":
        scss_file = os.path.join(fs_path, 'templates/Class-Atom.scss')
        destination_path = atom_path
        tipo_componente = "El átomo"
    if tipo not in ["org", "mol", "atom"]:
        print(f'Debes especificar si quieres crear un organismo, una molécula o un átomo')
        return

    #Primera letra siempre mayúscula y nunca empieza por barra baja
    if name.startswith("_"):
        name = name.lstrip("_")
    name = name[0].upper() + name[1:]

    # Creación de la variable className
    className = camel_to_kebab(name)

    # Definir carpeta del componente
    dir_path = os.path.join(destination_path, name)

    # Definir carpeta del componente con ruta relativa
    rel_path = os.path.relpath(dir_path, root_path)

    # Comprobar directorio
    if os.path.exists(dir_path):

        # Casos para borrar el componente recién creado
        if delete == "--d":
            delete_dir(dir_path)
            print(f'{tipo_componente} {name} se ha eliminado correctamente')
        elif delete == None:
            print(f'{tipo_componente} {name} ya existe, por favor inserte otro nombre (CamelCase)')
        else:
            print(f'Para borrar el componente debes añadir --d al final del comando')

    else:
        if delete == None:
            # Crear directorio en caso de que no exista
            os.makedirs(dir_path)
            print(f'{dir_path} creado')

            # Crear archivo SCSS
            with open(scss_file, 'r') as reference_file:
                code = reference_file.read().replace('${NAME}', className)
            if tipo == "atom":
                scss_path = os.path.join(dir_path, "_" + className + ".scss")
            else:
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
                code = code.replace('${DIR_PATH}', rel_path)
                code = code.replace('${FILE_NAME}', name + ".tsx")
            tsx_path = os.path.join(dir_path, name + ".tsx")
            with open(tsx_path, 'w') as new_file:
                new_file.write(code)
            print(f'{tsx_path} creado')

        # Caso por si se ha puesto --d por error
        else:
            print(f'El componente que estas intentando eliminar no existe')