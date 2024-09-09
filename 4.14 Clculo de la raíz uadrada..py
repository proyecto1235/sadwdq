import math

# Función para calcular la raíz cuadrada
def calcular_raiz_cuadrada(numero):
    if numero >= 0:
        return math.sqrt(numero)
    else:
        return "El número no puede ser negativo para la raíz cuadrada real."

# Programa principal
def main():
    try:
        # Solicitar al usuario que ingrese un número
        numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))
        resultado = calcular_raiz_cuadrada(numero)
        print(f"La raíz cuadrada de {numero} es: {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
