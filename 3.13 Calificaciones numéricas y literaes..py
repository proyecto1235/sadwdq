# Función para convertir una calificación numérica a una literal
def convertir_a_literal(calificacion):
    if calificacion >= 90:
        return "A"
    elif calificacion >= 80:
        return "B"
    elif calificacion >= 70:
        return "C"
    elif calificacion >= 60:
        return "D"
    else:
        return "F"

# Programa principal
def main():
    # Ingresar la calificación numérica
    try:
        calificacion = float(input("Ingrese la calificación numérica (0-100): "))
        if 0 <= calificacion <= 100:
            literal = convertir_a_literal(calificacion)
            print(f"La calificación literal correspondiente es: {literal}")
        else:
            print("Por favor, ingrese un valor entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
