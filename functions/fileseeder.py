import os
import re
from .camel_to_kebab import camel_to_kebab
from .delete_dir import delete_dir
from .alpha_filter import alpha_filter

def fileseeder( tipo = None, camelName = None, camelTraduccion = None, delete = False, renameFile = False ):

    # Definir carpeta raiz del proyecto
    root_path = os.getcwd()

    # Definir el directorio donde se encuentra instalado fileseeder
    fs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Definir los directorios donde irá cada componente
    org_path = os.path.join(root_path, 'web/src/sections')
    mol_path = os.path.join(root_path, 'web/src/modules')
    atom_path = os.path.join(root_path, 'web/src/styles/components/atoms')
    sdoc_path = os.path.join(root_path, 'backoffice/schemas')
    sobj_path = os.path.join(root_path, 'backoffice/schemas/objects')
    gpag_path = os.path.join(root_path, 'web/src/pages')
    gtemp_path = os.path.join(root_path, 'web/src/templates')
    land_path = os.path.join(root_path, 'web/src/styles/layouts')

    # Definir la ruta donde se encontrará el layout y los imports temporales en caso de gastby
    layout_path = os.path.join(root_path, 'temp_layout_fs.tsx')
    imports_path = os.path.join(root_path, 'temp_imports_fs.tsx')
    imports_documents_path = os.path.join(root_path, 'temp_imports_fields_fs.ts')
    documents_fields_path = os.path.join(root_path, 'temp_documents_fields_fs.ts')
    queries_path = os.path.join(root_path, 'temp_queries_fs.tsx')

    # Definir variables de posibles archivos
    scss_file = None
    tsx_file = None
    ts_file = None
    new_folder = None
    is_folder = False

    # Restricción de la variable name
    if camelName == None:
        print(f'Debes agregar el nombre del componente que quieres crear (CamelCase)')
        return
    
    #Primera letra siempre mayúscula
    camelName = alpha_filter(camelName)
    camelNameWithoutPrefix = camelName
    camelName = camelName[0].upper() + camelName[1:]

    # Restricción de la variable type y definir archivos y directorio
    if tipo == "org":
        scss_file = os.path.join(fs_path, 'templates/Class-Organism.scss')
        tsx_file = os.path.join(fs_path, 'templates/React-Organism.tsx')
        destination_path = org_path
        is_folder = True
        new_folder = camelName
    if tipo == "mol":
        scss_file = os.path.join(fs_path, 'templates/Class-Molecule.scss')
        tsx_file = os.path.join(fs_path, 'templates/React-Molecule.tsx')
        destination_path = mol_path
        is_folder = True
        new_folder = camelName
    if tipo == "atom":
        scss_file = os.path.join(fs_path, 'templates/Class-Atom.scss')
        destination_path = atom_path
    if tipo == "sdoc":
        ts_file = os.path.join(fs_path, 'templates/Sanity-Document.ts')
        destination_path = sdoc_path

    if tipo == "sdoc-prototype":
        ts_file = os.path.join(fs_path, 'templates/Sanity-Document-Prototype.ts')
        destination_path = sdoc_path


        # Restricción del nombre index en documento de Sanity
        if camelName == "Index":
            camelName = "Home"
            
    if tipo == "sobj":
        ts_file = os.path.join(fs_path, 'templates/Sanity-Object.ts')
        destination_path = sobj_path
    if tipo == "gpag":
        tsx_file = os.path.join(fs_path, 'templates/Gastby-Layout.tsx')
        destination_path = gpag_path
        camelName = camelName + "Page"
    if tipo == "gtemp":
        tsx_file = os.path.join(fs_path, 'templates/Gastby-Template-Info.tsx')
        destination_path = gtemp_path
        camelName = camelName + "Template"
    if tipo == "gprototype":
        tsx_file = os.path.join(fs_path, 'templates/Gastby-Template-Prototype.tsx')
        destination_path = gtemp_path
        camelName = camelName + "Template"
    if tipo == "land":
        scss_file = os.path.join(fs_path, 'templates/Class-Landing.scss')
        destination_path = land_path
    if tipo not in ["org", "mol", "atom", "sdoc", "sobj", "gpag", "gtemp", "land", "gprototype", "sdoc-prototype"]:
        print(f'Debes especificar que quieres crear')
        return

    # Creación de la variable kebabName
    kebabName = camel_to_kebab(camelName)



    # Definir carpeta del componente
    if is_folder:
        destination_path = os.path.join(destination_path, new_folder)

    # Definir carpeta del componente con ruta relativa
    rel_path = os.path.relpath(destination_path, root_path)

    # Definir la ruta completa del archivo por crear
    if scss_file is not None:
        if "web/src/styles" in destination_path:
            file_path = os.path.join(destination_path, "_" + kebabName + ".scss")
        else:
            file_path = os.path.join(destination_path, kebabName + ".scss")
    if tsx_file is not None:
        file_path = os.path.join(destination_path, camelName + ".tsx")
    if ts_file is not None:
        file_path = os.path.join(destination_path, kebabName + ".ts")

    # Comprobar directorio
    if os.path.exists(file_path):

        # Casos para borrar el componente recién creado
        if delete:
            if is_folder:
                delete_dir(destination_path)
            else:
                os.remove(file_path)
            print(f'{camelName} se ha eliminado correctamente')
        else:
            print(f'{file_path} ya existe, por favor inserte otro nombre (CamelCase)')

    else:
        if delete == False:
            # Crear directorio en caso de que no exista
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
                print(f'{destination_path} creado')

            # Crear archivo SCSS
            if scss_file is not None:
                with open(scss_file, 'r') as reference_file:
                    code = reference_file.read().replace('${NAME}', kebabName)
                if is_folder:
                    file_path = os.path.join(destination_path, kebabName + ".scss")
                with open(file_path, 'w') as new_file:
                    new_file.write(code)
                print(f'{file_path} creado')

            # Crear archivo TSX
            if tsx_file is not None:
                with open(tsx_file, 'r') as reference_file:
                    code = reference_file.read().replace('${NAME}', camelName).replace('${className}', kebabName)
                    code = code.replace('${DIR_PATH}', rel_path)
                    code = code.replace('${FILE_NAME}', camelName + ".tsx")
                    code = code.replace('${namePage}', camelName)
                    code = code.replace('${nameWithOutPrefix}', camelNameWithoutPrefix)
                    if os.path.exists(layout_path) and os.path.exists(imports_path) and os.path.exists(queries_path):
                        with open(layout_path, 'r') as tempLayoutLine:
                            layout = tempLayoutLine.read().strip()
                        with open(queries_path, 'r') as tempQueryLine:
                            queries = tempQueryLine.read().strip()
                        with open(imports_path, 'r') as tempImportsLine:
                            imports = tempImportsLine.read().strip()
                        code = code.replace('${LAYOUT}', layout)
                        code = code.replace('${IMPORTS}', imports)
                        code = code.replace('${QUERIES}', queries)
                        os.remove(layout_path)
                        os.remove(imports_path)
                        os.remove(queries_path)
                    else:
                        code = code.replace('${LAYOUT}', "")
                        code = code.replace('${IMPORTS}', "")
                        code = code.replace('${QUERIES}', "")
                if is_folder:
                    file_path = os.path.join(destination_path, camelName + ".tsx")
                with open(file_path, 'w') as new_file:
                    new_file.write(code)
                print(f'{file_path} creado')

            # Crear archivo TS
            if ts_file is not None:
                with open(ts_file, 'r') as reference_file:
                    code = reference_file.read().replace('${NAME}', camelName)
                    if os.path.exists(documents_fields_path) and os.path.exists(imports_documents_path):
                        with open(documents_fields_path, 'r') as tempFieldsDocs:
                            fields = tempFieldsDocs.read().strip()
                        with open(imports_documents_path, 'r') as tempImportsDocuments:
                            imports = tempImportsDocuments.read().strip()
                        code = code.replace('${FIELDS}', fields)
                        code = code.replace('${IMPORTS}', imports)
                        os.remove(documents_fields_path)
                        os.remove(imports_documents_path)
                    else:
                        code = code.replace('${FIELDS}', "No encuentra fields")
                        code = code.replace('${IMPORTS}', "No encuentra imports")
                with open(file_path, 'w') as new_file:
                    new_file.write(code)
                print(f'{file_path} creado')

        # Caso por si se ha puesto --d por error
        else:
            print(f'El componente que estas intentando eliminar no existe')