import tkinter as tk
from tkinter import messagebox
import random

from PersonajesPython.Clases.Guerrero import Guerrero
from PersonajesPython.Clases.Mago import Mago
from PersonajesPython.Clases.Personaje import Personaje

listaPersonajes = []

def obtener_posicion_random(self):
    """Genera coordenadas aleatorias dentro del canvas."""
    x = random.randint(50, 450)
    y = random.randint(50, 450)
    return x, y

def crear_guerrero():
    nombre = inputName.get() or "Guerrero de cuyo nombre no quiero acordarme"
    x, y = obtener_posicion_random(ventana)
    nuevoGuerrero = Guerrero(escenario_canvas, nombre, x, y)
    nuevoGuerrero.dibujar()
    listaPersonajes.append(nuevoGuerrero)


def crear_mago():
    nombre = inputName.get() or "Mago de cuyo nombre no quiero acordarme"
    x, y = obtener_posicion_random(ventana)
    nuevoMago = Mago(escenario_canvas, nombre, x, y)
    nuevoMago.dibujar()
    listaPersonajes.append(nuevoMago)

def todos_actuan():
    txt = ""
    for personaje in listaPersonajes:
        txt += personaje.realizar_accion()
    labelAtaque.config(text=txt)



ventana = tk.Tk() #Creamos la ventana.
ventana.title("JuegoPersonajesConPOO") #Le ponemos titulo a la ventana.
ventana.geometry("670x670") #Le damos un tamaño.
frame_control = tk.Frame(ventana, pady=10, bg="#ecf0f1")
frame_control.pack(fill=tk.X)
tk.Label(frame_control, text="Nombre:", bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
inputName = tk.Entry(frame_control)
inputName.pack(side=tk.LEFT, padx=5)
#Creamos una variable canvas para poder escribir sobre ella
escenario_canvas = tk.Canvas(ventana, width=800, height=500, bg="#2c3e50")
escenario_canvas.pack(fill=tk.BOTH, expand=True) # expand=True permite que crezca si la ventana cambia de tamaño
labelAtaque = tk.Label(ventana, bg="#ecf0f1")
labelAtaque.pack(side=tk.LEFT, padx=5)


# Botones para INSTANCIAR (Crear objetos)
botonGuerrero = tk.Button(frame_control, text="Crear Guerrero", bg="#ff1800", fg="white",
    command=crear_guerrero).pack(side=tk.LEFT, padx=5)

botonMago = tk.Button(frame_control, text="Crear Mago", bg="#0000ff", fg="white",
    command=crear_mago).pack(side=tk.LEFT, padx=5)

botonAtaque = tk.Button(frame_control, text="Todos Atacan", bg="#dbdbdb", fg="black",
    command=todos_actuan).pack(side=tk.LEFT, padx=5)

ventana.mainloop() #Que no se cierre la ventana.