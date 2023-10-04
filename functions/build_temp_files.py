import os


def build_temp_files( element ):

    root_path = os.getcwd()
    md_path = os.path.join(root_path, 'structure.md')
    layout_path = os.path.join(root_path, 'temp_layout_fs.tsx')
    imports_path = os.path.join(root_path, 'temp_imports_fs.tsx')
    queries_path = os.path.join(root_path, 'temp_queries_fs.tsx')
    schemas_path = os.path.join(root_path, 'temp_schemas_fs.tsx')

    with open(md_path, "r") as file:

        organismos = []
        inside_section = False

        for line in file:
            stripped_line = line.strip()

            if stripped_line.startswith('# * ' + element) or stripped_line.startswith('# ' + element):
                inside_section = True
            elif inside_section and line.startswith('## '):
                organismos.append(line[2:].strip())
            elif stripped_line == "":
                inside_section = False
    

    with open(layout_path, 'w') as f:
        for organismo in organismos:
            organismo_lower = organismo[0].lower() + organismo[1:]
            f.write('      <'+organismo+' data={data.page?.'+organismo_lower+' as Queries.Sanity'+organismo+'} />\n')

    organismos.sort()



    with open(imports_path, 'w') as f:
        for organismo in organismos:
            f.write('import { '+organismo+' } from "../sections/'+organismo+'/'+organismo+'";\n')

    with open(queries_path, 'w') as f:
        for organismo in organismos:
            organismo_lower = organismo[0].lower() + organismo[1:]
            f.write(organismo_lower + '{ \n \n } \n')

    with open(schemas_path, 'w') as f:
            for organismo in organismos:
                organismo_lower = organismo[0].lower() + organismo[1:]
                f.write(organismo_lower + '{... on Sanity'+organismo+' {name slug { current}}\n \n } \n')
