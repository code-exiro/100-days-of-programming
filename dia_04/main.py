# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

for numero in range(1, 101):
    if numero > 1:
        es_primo = True
        for i in range(2, int(numero**0.5) + 1): 
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            print(numero, end=" ")  # Esta bastante bien esta forma de poner los print de forma continua

