# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def invertir_cadena(texto):
    resultado = ""
    for caracter in texto:
        resultado = caracter + resultado
    return resultado

texto = input('Ingresa el texto: ')
resultado = invertir_cadena(texto)
print("Cadena invertida: ", resultado)