import os


def build_layout( element ):

    root_path = os.getcwd()
    md_path = os.path.join(root_path, 'structure.md')
    temptxt_path = os.path.join(root_path, 'temp_layout_fs.txt')

    with open(md_path, "r") as file:

        organismos = []

        for line in file:
            if line.strip().startswith('# **'+element+'**'):
                for line in file:
                    if line.startswith('## '):
                        organismos.append(line[2:].strip())
                    elif line.strip() == "":
                        break
    

    with open(temptxt_path, 'w') as f:
        for organismo in organismos:
            f.write('      <'+organismo+' element={`'+element+'`} />\n')