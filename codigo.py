def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def main():
    print("Calculadora básica")

    # Mostramos el menú al usuario
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    # Leemos la opción elegida por el usuario
    opcion = int(input("Elige una opción: "))

    # Pedimos dos números al usuario
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    # Realizamos la operación elegida
    if opcion == 1:
        resultado = suma(a, b)
    elif opcion == 2:
        resultado = resta(a, b)
    elif opcion == 3:
        resultado = multiplicacion(a, b)
    else:
        resultado = division(a, b)

    # Mostramos el resultado
    print("El resultado es:", resultado)

if __name__ == "__main__":
    main()
