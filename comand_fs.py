import sys
from functions.fileseeder import fileseeder

if __name__ == "__main__":
    # Obtener los valores de tipo y name desde los argumentos de línea de comandos
    tipo = sys.argv[1]
    name = sys.argv[2]

    # Llamar a la función fileseeder con los valores de tipo y name
    fileseeder(tipo, name)
