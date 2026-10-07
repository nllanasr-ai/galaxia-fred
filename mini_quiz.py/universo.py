import turtle
import random
import math
import time

ventana = turtle.Screen()
ventana.bgcolor("black")
ventana.title("Para Fredy ❤️")
ventana.setup(700, 550)
ventana.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

colores_galaxia = ["deepskyblue", "cyan", "lightblue", "gold", "yellow", "white"]
colores_planetas = ["red", "lime", "blue", "magenta", "yellow", "cyan", "orange"]

mensajes = [
    "Fredy, perdóname por no ser tan atenta 💔",
    "Te amo con todo mi corazón ❤️",
    "Eres lo más bonito ✨",
    "Siempre pienso en ti 💭",
    "Perdóname, eres mi favorito 🌌",
    "Te adoro infinitamente 🥰",
    "Fredy, mi amor brilla más que las estrellas 🌟",
    "Lo siento si no te demostré todo 💫",
    "Eres mi amor eterno 💙"
]

def hacer_galaxia():
    for i in range(600):
        ang = i * 0.02
        r = 0.12 * i
        x = r * math.cos(ang) + random.uniform(-1,1)
        y = r * math.sin(ang) + random.uniform(-1,1)
        if r < 40: c = "white"
        elif r < 120: c = random.choice(["gold", "yellow"])
        else: c = random.choice(["deepskyblue", "cyan"])
        t.goto(x,y)
        t.dot(random.randint(2,4), c)
    t.goto(0,0); t.dot(12,"white")

planetas = []
for _ in range(5):
    planetas.append({"r":random.randint(100,250), "a":random.uniform(0,6), "v":random.uniform(0.002,0.01), "tam":random.randint(8,18), "c":random.choice(colores_planetas)})

def ver_planetas():
    for p in planetas:
        p["a"] += p["v"]
        x = p["r"] * math.cos(p["a"])
        y = p["r"] * math.sin(p["a"])
        t.goto(x,y); t.dot(p["tam"], p["c"])

textos = []
for m in mensajes:
    textos.append({"t":m, "x":random.randint(-300,300), "y":random.randint(-200,200), "vx":random.uniform(-0.2,0.2), "vy":random.uniform(-0.15,0.15), "c":random.choice(["gold","cyan","white","pink"])})

def ver_texto():
    for m in textos:
        m["x"] += m["vx"]; m["y"] += m["vy"]
        if abs(m["x"])>340: m["vx"] *= -1
        if abs(m["y"])>240: m["vy"] *= -1
        t.goto(m["x"],m["y"]); t.color(m["c"]); t.write(m["t"], align="center", font=("Arial",10,"bold"))
    t.goto(0,-250); t.color("pink"); t.write("💖 Para Fredy, con amor y perdón 💖", align="center", font=("Arial",16,"bold"))

hacer_galaxia()

while True:
    t.clear()
    hacer_galaxia()
    ver_planetas()
    ver_texto()
    ventana.update()
    time.sleep(0.02)