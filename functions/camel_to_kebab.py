def camel_to_kebab(string):
    # Buscamos todas las letras mayúsculas en la cadena y las reemplazamos por "-letra"
    kebab = ''.join(['-' + i.lower() if i.isupper() else i for i in string])
    # Si la cadena empieza por mayúscula, eliminamos el primer "-"
    if kebab[0] == '-':
        kebab = kebab[1:]
    return kebab


def pascal_to_camel(string):
    # Si la cadena está vacía o tiene solo un carácter, la devolvemos tal cual
    if len(string) <= 1:
        return string.lower()
    
    # Convertimos el primer carácter a minúscula
    camel = string[0].lower() + string[1:]
    
    return camel

