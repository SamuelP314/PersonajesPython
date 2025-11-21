import tkinter as tk
import random
from tkinter import messagebox

from PersonajesPython.Clases.Guerrero import Guerrero
from PersonajesPython.Clases.Mago import Mago
from PersonajesPython.Clases.Personaje import Personaje

personajePrueba1 = Personaje("Canvas", "Prim", 10,10)
personajePrueba2 = Guerrero("Canvas", "Espartero", 11,10)
personajePrueba3 = Mago("Canvas", "Amadeo", 12,10)

print(personajePrueba1.realizar_accion())
print(personajePrueba2.realizar_accion())
print(personajePrueba3.realizar_accion())




ventana = tk.Tk()
ventana.title("JuegoPersonajesConPOO")
ventana.geometry("670x670")
frame_control = tk.Frame(ventana, pady=10, bg="#ecf0f1")
frame_control.pack(fill=tk.X)
tk.Label(frame_control, text="Nombre:", bg="#ecf0f1").pack(side=tk.LEFT, padx=5)

ventana.mainloop()




