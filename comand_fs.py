import sys
from functions.fileseeder import fileseeder

if __name__ == "__main__":

    # Establecer valores por defecto
    tipo = None
    name = None
    delete = None
    
    # Obtener los valores de tipo y name desde los argumentos de línea de comandos
    if len(sys.argv) >= 3:
        tipo = sys.argv[1]
        name = sys.argv[2]
        
        # Comprobar si se proporcionó un tercer parámetro opcional
        if len(sys.argv) >= 4:
            delete = sys.argv[3]

    # Llamar a la función fileseeder con los valores de tipo, name y delete
    fileseeder(tipo, name, delete)
