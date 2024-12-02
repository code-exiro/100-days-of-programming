# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# La función recibirá por parámetro sólo UN polígono a la vez.
# Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# Imprime el cálculo del área de un polígono de cada tipo.

#base = int(input('Ingresa la base: '))
#altura = int(input('Ingresa la altura: '))
#lado = int(input('Ingresa un lado: '))

# def triangulo(base, altura):
#     area = (base * altura) / 2
#     return area

# def cuadrado(lado):
#     area = (lado * lado)
#     return area

# def rectuangulo(base, altura):
#     area = (base * altura)
#     return area

# resultado = triangulo(base, altura)
# print(f"area {resultado}")

# resultado1 = cuadrado(lado)
# print(f"area {resultado1}")

# resultado = rectuangulo(base, altura)
# print(f"area {resultado}")



print("Polígono a escoger:")
print("1: Triángulo")
print("2: Cuadrado")
print("3: Rectángulo")
opcion = input("Selecciona una opción (1, 2, 3): ")

def calcular_area_poligono(opcion):
    if opcion == "1":  # Triángulo
        base = float(input('Ingresa la base del triángulo: '))
        altura = float(input('Ingresa la altura del triángulo: '))
        return (base * altura) / 2
    elif opcion == "2":  # Cuadrado
        lado = float(input('Ingresa el lado del cuadrado: '))
        return lado ** 2
    elif opcion == "3":  # Rectángulo
        base = float(input('Ingresa la base del rectángulo: '))
        altura = float(input('Ingresa la altura del rectángulo: '))
        return base * altura
    else:
        return "Opción no válida. Escoge 1, 2 o 3."

resultado = calcular_area_poligono(opcion)
print(f"Área: {resultado}")
