import math

# Función para convertir de grados a radianes
def grados_a_radianes(grados):
    return grados * math.pi / 180

# Función para convertir de radianes a grados
def radianes_a_grados(radianes):
    return radianes * 180 / math.pi

# Programa principal
def main():
    print("Conversión entre grados y radianes:")
    print("1. Convertir de grados a radianes")
    print("2. Convertir de radianes a grados")
    
    opcion = input("Elija una opción (1 o 2): ")

    if opcion == "1":
        # Conversión de grados a radianes
        try:
            grados = float(input("Ingrese el valor en grados: "))
            radianes = grados_a_radianes(grados)
            print(f"{grados} grados son {radianes} radianes.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")
    
    elif opcion == "2":
        # Conversión de radianes a grados
        try:
            radianes = float(input("Ingrese el valor en radianes: "))
            grados = radianes_a_grados(radianes)
            print(f"{radianes} radianes son {grados} grados.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")
    
    else:
        print("Opción no válida. Por favor elija 1 o 2.")

if __name__ == "__main__":
    main()
