#JEYZON MAURULIO BARRAGAN ESPINO
#FELIX MORALES FLORES
#RICARDO VAZQUEZ MURILLO
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image

root = Tk()
root.geometry("600x800")
root.title("BIBI OUT-CONTROL DE TEMPERATURA DE UN HORNO")
root.config(bg="beige")

fig, ax = plt.subplots()
fig.set_size_inches(4, 4)  

def graficar():
    ax.clear()
    x = np.arange(0, int(gas_values.get()))
    y = (2*x**2-50)
    ax.plot(x, y)
    max_y = np.max(y)
    ax.set_xlabel("Presion")
    ax.set_ylabel("Temperatura(°F)")

    if max_y > 450:
        messagebox.showwarning("Alerta", f"La Temperatura esta demasiado alta.")
    valor_maximo.set(f"Temperatura Maxima:{max_y}°F")
    canvas.draw()

frame = Frame(root,bg="beige")
frame.pack()
ax.set_xlabel("Presion")
ax.set_ylabel("Temperatura(°F)")

#TITULO
titulo = Label(frame, text="CONTROL DE TEMPERATURA DE UN HORNO",bg="white")
titulo.config(font=("Roboto",18,"bold"))
titulo.pack(padx=10, pady=10, side=TOP)

columna_izquierda = Frame(frame).place(relx=0.1,rely=0.2)
#columna_izquierda.pack(side=LEFT)

#TEXTO DE PRESION
gas_label = Label(columna_izquierda, text="PRESION:", font=("Roboto",15),bg="beige").place(relx=0.1,rely=0.75)
#gas_label.pack(pady=8, padx=10)

#LISTA DE LOS VALORES DE LAS PRESIONES
gas_values = StringVar()
gas_values.set("10")
lista_desplegable = ttk.Combobox(columna_izquierda, width=17, values=["10", "12", "14", "16", "18", "20"], textvariable=gas_values).place(relx=0.3,rely=0.77)
#lista_desplegable.pack(pady=8, padx=10)

#BOTON DE ENCENDIDO
botonGraficar = Button(columna_izquierda, text="ENCENDER", command=graficar,bg="green",width=9, height=2,font=("Roboto", 10)).place(relx=0.3,rely=0.82)
#botonGraficar.pack(pady=15, padx=10)

#TEXTO DEL VALOR MAXIMO
valor_maximo = StringVar()
etiqueta_valor_maximo = Label(frame, textvariable=valor_maximo, font=("Roboto", 15),bg="white")#.place(relx=0.1,rely=0.8)
etiqueta_valor_maximo.pack(padx=15, pady=30, side=TOP)

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=True)

root.mainloop()