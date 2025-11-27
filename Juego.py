import tkinter as tk
from tkinter import messagebox
import random

from PersonajesPython.Clases.Guerrero import Guerrero
from PersonajesPython.Clases.Mago import Mago
from PersonajesPython.Clases.Personaje import Personaje

personajePrueba1 = Personaje("Canvas", "Prim", 10, 10)

personajePrueba2 = Guerrero("Canvas", "Espartero", 11, 10)

personajePrueba3 = Mago("Canvas", "Amadeo", 12, 10)

print(personajePrueba1.realizar_accion())
print(personajePrueba2.realizar_accion())
print(personajePrueba3.realizar_accion())


def obtener_posicion_random(self):
    """Genera coordenadas aleatorias dentro del canvas."""
    x = random.randint(50, 750)
    y = random.randint(50, 750)
    return x, y

def crear_guerrero():
    nombre = inputName.get() or "Guerrero de cuyo nombre no quiero acordarme"
    x, y = obtener_posicion_random(ventana)

def crear_mago():
    nombre = inputName.get() or "Mago de cuyo nombre no quiero acordarme"
    x, y = obtener_posicion_random(ventana)



ventana = tk.Tk() #Creamos la ventana.
escenario_canvas = tk.Canvas(ventana, width=800, height=500, bg="#2c3e50")
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


def dibujar(self):
    """Método para visualizar el objeto en la pantalla."""
    radio = 20
    x1, y1 = self.x - radio, self.y - radio
    x2, y2 = self.x + radio, self.y + radio

# Botones para INSTANCIAR (Crear objetos)
botonGuerrero = tk.Button(frame_control, text="Crear Guerrero", bg="#e74c3c", fg="white",
command=crear_guerrero).pack(side=tk.LEFT, padx=5)

botonMago = tk.Button(frame_control, text="Crear Mago", bg="#e74c3c", fg="white",
command=crear_mago).pack(side=tk.LEFT, padx=5)

botonRubenIniguez = tk.Button(frame_control, text="Crear un clon de Ruben Iñiguez", bg="#e74c3c", fg="white",
command=crear_guerrero).pack(side=tk.LEFT, padx=5)

ventana.mainloop() #Que no se cierre la ventana.