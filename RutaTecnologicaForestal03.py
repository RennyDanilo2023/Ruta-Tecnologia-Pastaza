import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller. """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def abrir_imagen(nombre_imagen):
    imagen_path = resource_path(f"{nombre_imagen}.png")
    print(f"Intentando abrir la imagen en: {imagen_path}")  # Depuración: imprime la ruta de la imagen.
    try:
        imagen = Image.open(imagen_path)
        foto = ImageTk.PhotoImage(imagen)
        etiqueta_imagen.config(image=foto)
        etiqueta_imagen.image = foto  # Mantener una referencia.
        print("Imagen cargada correctamente.")  # Depuración: confirma que la imagen se carga.
    except FileNotFoundError:
        print(f"No se encontró la imagen: {nombre_imagen}.png")

root = tk.Tk()
root.title("Interfaz de Tecnología Forestal")
root.geometry("1000x500")  # Adjust as needed

etiqueta_imagen = tk.Label(root)
etiqueta_imagen.grid(row=0, column=6, rowspan=3, sticky="nsew", padx=10, pady=10)

nombres_figuras = {
    "Tecnología Forestal 1 (Pellets)": "TF1",
    "Tecnología Forestal 2 (Carbón)": "TF2",
    "Tecnología Forestal 3 (Gases de Síntesis)": "TF3",
    "Tecnología Forestal 4 (Pulpa Kraft)": "TF4",
    "Tecnología Forestal 5 (Etanol)": "TF5"
}

for i in range(4):
    root.grid_rowconfigure(i, weight=1)
for j in range(7):
    root.grid_columnconfigure(j, weight=1)

etiquetas_texto = {
    (0, 1): "Pellets",
    (0, 2): "Carbón",
    (0, 3): "Gases de síntesis",
    (0, 4): "Pulpa kraft",
    (0, 5): "Etanol",
    (1, 0): "Pique",
    (2, 0): "Pulpa kraft"
}

for pos, texto in etiquetas_texto.items():
    label = tk.Label(root, text=texto, relief="ridge", borderwidth=2)
    label.grid(row=pos[0], column=pos[1], sticky="nsew", padx=1, pady=1)

for (nombre, imagen_nombre) in nombres_figuras.items():
    boton = tk.Button(root, text=nombre, bg="yellow", command=lambda nf=imagen_nombre: abrir_imagen(nf))
    fila = 1 if nombre != "Tecnología Forestal 5 (Etanol)" else 2
    columna = list(nombres_figuras.keys()).index(nombre) + 1
    boton.grid(row=fila, column=columna, sticky="nsew", padx=1, pady=1)

etiqueta_final = tk.Label(root, text="UNIVERSIDAD ESTATAL AMAZONICA\nElaborado por: VINOCUNGA-PILLAJO RENNY DANILO & PEREZ-MARTINEZ AMAURY",
                          fg="black", bg="white", font=("Helvetica", 13, "bold"))
etiqueta_final.grid(row=3, column=0, columnspan=7, sticky="ew")

root.mainloop()
