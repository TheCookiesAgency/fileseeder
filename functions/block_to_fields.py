import re


def blocks_to_fields(texto_entrada):
    # Usamos una expresión regular para encontrar todos los componentes
    # Buscamos patrones como <ComponentName />
    patron = r'<([A-Z][a-zA-Z0-9]*)\s*\/>'

    # Encontrar todos los componentes en el texto
    componentes = re.findall(patron, texto_entrada)

    # Preparar el texto de salida
    salida = ""

    # Procesar cada componente encontrado
    for componente in componentes:
        # Convertir nombre del componente a camelCase para el campo 'name'
        nombre_campo = componente[0].lower() + componente[1:]

        # Crear la definición del campo
        definicion = f"""defineField({{
    title: '{componente}',
    name: '{nombre_campo}',
    type: 'copyAndMedia',
    options: {{
        collapsible: true,
        collapsed: true,
    }},
}}),
"""
        # Añadir al texto de salida
        salida += definicion

    return salida
