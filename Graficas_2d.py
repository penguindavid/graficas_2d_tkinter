from tkinter import *

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
c.place(x=0, y=0)

# -----------------
# Líneas rectas
# -----------------
linea_1 = c.create_line(BASE/2, ALTURA/2, BASE, 0, fill="red", width=2)
linea_2 = c.create_line(0, 0, BASE/2, ALTURA/2, fill="green", width=5)

# -------------------
# Dibujar texto
# -------------------
texto_1 = c.create_text(BASE/4, ALTURA/4, anchor="center",
                        text="David Macias", font=("Arial", 25, "bold"),
                        fill="blue", activefill="yellow")

# -----------
# Rectángulo
# -----------
rectangulo_1 = c.create_rectangle(BASE/2, ALTURA/2, BASE, ALTURA, fill="pink", outline="blue")

# ----------
# Polígono
# ----------
poligono_1 = c.create_polygon(0, 0, BASE/2, ALTURA/2, 0, ALTURA, fill="red", outline="red")

# --------
# Círculo
# --------
# Se define correctamente con dos puntos opuestos del óvalo
circulo_1 = c.create_oval(BASE/2 - 50, ALTURA/2 - 50, BASE/2 + 50, ALTURA/2 + 50,
                          fill="orange", outline="green")

# --------
# Arco
# --------
arco_1 = c.create_arc(BASE/2 - 30, ALTURA/2 - 30, BASE/2 + 30, ALTURA/2 + 30,
                      start=45, extent=270, fill="black")

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
