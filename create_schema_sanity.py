import os

def camel_to_kebab(string):
    # Buscamos todas las letras mayúsculas en la cadena y las reemplazamos por "-letra"
    kebab = ''.join(['-' + i.lower() if i.isupper() else i for i in string])
    # Si la cadena empieza por mayúscula, eliminamos el primer "-"
    if kebab[0] == '-':
        kebab = kebab[1:]
    return kebab

def build_temp_files_sanity():
    root_path = os.getcwd()
    md_path = os.path.join(root_path, 'structure.md')
    documents_docs_path = os.path.join(root_path, 'temp_documents_n_objects_fields_fs.ts')
    documents_imports_path = os.path.join(root_path, 'temp_all_imports_sanity_fs.ts')

    with open(md_path, "r") as file:
        docs = []
        objs = []

        for line in file:
            stripped_line = line.strip()

            if stripped_line.startswith('# * '):
                item = line[4:].strip()
                if item not in docs:
                    docs.append(item)
            elif stripped_line.startswith('# '):
                item = line[2:].strip()
                if item not in docs:
                    docs.append(item)
            elif line.startswith('## '):
                item = line[3:].strip()
                if item not in objs:
                    objs.append(item)
    

    with open(documents_docs_path, 'w') as f:
        for doc in docs:
            doc_lower = doc[0].lower() + doc[1:]
            f.write(doc_lower + ', \n')

        for obj in objs:
            obj_lower = obj[0].lower() + obj[1:]
            f.write(obj_lower + ', \n')


    with open(documents_imports_path, 'w') as f:
        for doc in docs:
            doc_lower = doc[0].lower() + doc[1:]
            f.write('import ' + doc_lower + ' from "./' + camel_to_kebab(doc) + '";\n')

        for obj in objs:
            obj_lower = obj[0].lower() + obj[1:]
            f.write('import ' + obj_lower + ' from "./objects/' + camel_to_kebab(obj) + '";\n')
