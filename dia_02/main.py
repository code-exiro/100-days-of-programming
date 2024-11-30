# Es un anagrama?

# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS
# las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

palabra1 = input('Primera palabra: ')
palabra2 = input('Segunda palabra: ')

def anagrama(palabra1, palabra2):
    if len(palabra1) != len(palabra2):  #len funciona para ver la longitud de un elemento
        return False
    elif palabra1 == palabra2:
        return False
    elif sorted(palabra1) == sorted(palabra2):  #sorted se utiliza para ordenar elementos 
        return True
    else:
        return False  

resultado = anagrama(palabra1, palabra2)
print(f"¿Son anagramas? {resultado}")

