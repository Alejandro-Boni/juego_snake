import turtle
import time
import random

posponer = 0.1
score = 0
high_score = 0

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Juego de la Culebrita")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# Comida (Nueva parte)
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Cuerpo de la serpiente (Lista para guardar los segmentos)
segmentos = []

# Texto del marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0   High Score: 0", align="center", font=("Courier", 24, "normal"))

# Funciones de dirección
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"
def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"
def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"
def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

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

    # Colisión con bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        
        # Esconder segmentos (Reiniciar juego)
        for segmento in segmentos:
            segmento.goto(1000, 1000)
        segmentos.clear()
        score = 0
        texto.clear()
        texto.write(f"Score: {score}   High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Colisión con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        # Añadir nuevo segmento
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("lightgreen")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        # Aumentar marcador
        score += 10
        if score > high_score:
            high_score = score
        texto.clear()
        texto.write(f"Score: {score}   High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Mover el cuerpo (Lógica de seguimiento)
    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x, y)
    
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mover()

    # Colisión con el propio cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            for s in segmentos:
                s.goto(1000, 1000)
            segmentos.clear()
            score = 0
            texto.clear()
            texto.write(f"Score: {score}   High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(posponer)