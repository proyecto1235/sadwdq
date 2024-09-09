import turtle

# Crear una ventana para el dibujo
window = turtle.Screen()

# Crear un objeto turtle
t = turtle.Turtle()

# Función para dibujar un cuadrado
def dibujar_cuadrado(lado):
    for _ in range(4):
        t.forward(lado)  # Mover hacia adelante
        t.right(90)      # Girar 90 grados a la derecha

# Dibujar un cuadrado de 100 píxeles de lado
dibujar_cuadrado(100)

# Esperar a que se cierre la ventana con un clic
window.mainloop()
