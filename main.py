import turtle
import time

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Juego de la Culebrita")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0) # Suaviza las animaciones

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup() # Para que no deje una raya al moverse
cabeza.goto(0,0)
cabeza.direction = "stop"

# Funciones de movimiento
def arriba(): cabeza.direction = "up"
def abajo(): cabeza.direction = "down"
def izquierda(): cabeza.direction = "left"
def derecha(): cabeza.direction = "right"

def mover():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

# Bucle principal
while True:
    ventana.update()
    mover()
    time.sleep(0.1) # Controla la velocidad