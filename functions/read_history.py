import os

root_path = os.getcwd()
his_path = os.path.join(root_path, 'historial_fs.txt')
with open(his_path, "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        if linea.find("ya existe") != -1:
            print(linea.strip())

os.remove(his_path)