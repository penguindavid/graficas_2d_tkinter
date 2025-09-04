from tkinter import *

# --------------------
# Variables globales
# --------------------
BASE = 460
ALTURA = 460
base= 340
alto=280

# ---------------------
# Ventana principal
# ---------------------
ventana_principal = Tk()
ventana_principal.title("Gráficas 2D")
ventana_principal.geometry("500x500")
ventana_principal.config(bg="PINK")

# --------------------
# Frame de graficación
# --------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="gray", width=480, height=480)
frame_graficacion.place(x=10, y=10)

# --------------------
# Lienzo de graficación
# --------------------
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

# -----------------
# Líneas rectas
# -----------------
#linea_1 = c.create_line(BASE/2, ALTURA/2, BASE, 0, fill="red", width=2)
#linea_2 = c.create_line(0, 0, BASE/2, ALTURA/2, fill="green", width=5)

# -------------------
# Dibujar texto
# -------------------
#texto_1 = c.create_text(BASE/4, ALTURA/4, anchor="center",
                    #text="David Macias", font=("Arial", 25, "bold"),
                    #fill="blue", activefill="yellow")

# -----------
# Rectángulo
# -----------
rectangulo_1 = c.create_rectangle(270/2 - 50,150/2 +  60  , 270/2 + 50, 150/2 + 210, fill="gray", outline="blue")

# ----------
# Polígono
# ----------
#poligono_1 = c.create_polygon(0, 0, BASE/2, ALTURA/2, 0, ALTURA, fill="red", outline="red")

# --------
# Círculo
# --------
# Círculo centrado en (200, 150) con radio 40
irculo_1 = c.create_oval(460/2 -50,220/2+140, 460/2 + 30, 220/2 + 200,fill="orange",outline="green")

# --------
# Arco
# --------
#arco_1 = c.create_arc(BASE/2 - 30, ALTURA/2 - 30, BASE/2 + 30, ALTURA/2 + 30,
                    #start=45, extent=270, fill="black")

# --------------------
# Frame de controles
# --------------------
#frame_controles = Frame(ventana_principal)
#frame_controles.config(bg="black", width=480, height=240)
#frame_controles.place(x=10, y=260)  # Lo movemos abajo para no tapar el frame de graficación

# ---------------------------
# Desplegar ventana principal
# ---------------------------
ventana_principal.mainloop()
