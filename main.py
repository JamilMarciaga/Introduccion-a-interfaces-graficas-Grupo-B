import Operaciones


def ejecutar_calculadora():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Seleccione una operación: ").strip()

    if opcion == "1":
        resultado = Operaciones.sumar(numero1, numero2)
    elif opcion == "2":
        resultado = Operaciones.restar(numero1, numero2)
    elif opcion == "3":
        resultado = Operaciones.multiplicar(numero1, numero2)
    elif opcion == "4":
        resultado = Operaciones.dividir(numero1, numero2)
    else:
        resultado = "Opción no válida"

    print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    ejecutar_calculadora()
