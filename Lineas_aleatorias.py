from tkinter import *
import  random

# --------------------
# Variables globales
# --------------------
BASE = 460
ALTURA = 220

# ---------------------
# Ventana principal
# ---------------------
ventana_principal = Tk()
ventana_principal.title("Gráficas 2D")
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

# --------------------
# Frame de graficación
# --------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

# --------------------
# Lienzo de graficación
# --------------------
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

# -------------------------
# figuras de color y/o cambio de color
# -------------------------
for i in range(100):
    x= random.randint(0, BASE -20)
    y= random.randint(0, ALTURA -20)

    color = "#"

    for caracter in range (6): 
        color = color + random.choice("0123456789abcdef")

    circulo = c.create_oval(x, y, x+20, y+20, fill= color)

# --------------------
# Frame de controles
# --------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="black", width=480, height=240)
frame_controles.place(x=10, y=260)  # Lo movemos abajo para no tapar el frame de graficación

# ---------------------------
# Desplegar ventana principal
# ---------------------------
ventana_principal.mainloop()
