import tkinter as tk
from PIL import Image, ImageTk, ImageOps

# Esta función abre la imagen dentro de la ventana actual de Tkinter.
def abrir_imagen(nombre_imagen):
    try:
        # Carga la imagen con el nombre proporcionado y agrega un contorno negro.
        imagen = Image.open(f"{nombre_imagen}.png")
        imagen_con_borde = ImageOps.expand(imagen, border=5, fill='black')  # Borde más delgado
        foto = ImageTk.PhotoImage(imagen_con_borde)
        
        # Actualiza la etiqueta de la imagen con la nueva imagen.
        etiqueta_imagen.config(image=foto)
        etiqueta_imagen.image = foto  # Mantener una referencia.
    except FileNotFoundError:
        print(f"No se encontró la imagen: {nombre_imagen}.png")

root = tk.Tk()
root.title("Interfaz de Tecnología Forestal")
root.geometry("1000x500")  # Tamaño ajustado para dar cabida a la etiqueta final

# Configuración inicial de la etiqueta de la imagen.
etiqueta_imagen = tk.Label(root)
etiqueta_imagen.grid(row=0, column=6, rowspan=3, sticky="nsew", padx=10, pady=10)

# Define los nombres de las figuras asociadas a cada botón.
nombres_figuras = {
    "Tecnología Forestal 1 (Pellets)": "TF1",
    "Tecnología Forestal 2 (Carbón)": "TF2",
    "Tecnología Forestal 3 (Gases de Síntesis)": "TF3",
    "Tecnología Forestal 4 (Pulpa Kraft)": "TF4",
    "Tecnología Forestal 5 (Etanol)": "TF5"
}

# Configura las filas y columnas para que se expandan uniformemente.
for i in range(4):  # Cuatro filas para incluir la etiqueta final.
    root.grid_rowconfigure(i, weight=1)
for j in range(7):  # Siete columnas.
    root.grid_columnconfigure(j, weight=1)

# Define los textos de las etiquetas según su posición en la grilla.
etiquetas_texto = {
    (0, 1): "Pellets",
    (0, 2): "Carbón",
    (0, 3): "Gases de síntesis",
    (0, 4): "Pulpa kraft",
    (0, 5): "Etanol",
    (1, 0): "Pique",
    (2, 0): "Pulpa kraft"
}

# Crea etiquetas en las posiciones especificadas.
for pos, texto in etiquetas_texto.items():
    label = tk.Label(root, text=texto, relief="ridge", borderwidth=2)
    label.grid(row=pos[0], column=pos[1], sticky="nsew", padx=1, pady=1)

# Crea botones para las tecnologías forestales y los asocia con la imagen correspondiente.
for (nombre, imagen_nombre) in nombres_figuras.items():
    boton = tk.Button(root, text=nombre, bg="yellow",
                      command=lambda nf=imagen_nombre: abrir_imagen(nf))
    fila = 1 if nombre != "Tecnología Forestal 5 (Etanol)" else 2
    columna = list(nombres_figuras.keys()).index(nombre) + 1
    boton.grid(row=fila, column=columna, sticky="nsew", padx=1, pady=1)

# Etiqueta final con la información de la universidad y los elaboradores, más grande y en negrita.
etiqueta_final = tk.Label(root, text="UNIVERSIDAD ESTATAL AMAZONICA\nElaborado por: VINOCUNGA-PILLAJO RENNY DANILO & PEREZ-MARTINEZ AMAURY",
                          fg="black", bg="white", font=("Helvetica", 13, "bold"))
etiqueta_final.grid(row=3, column=0, columnspan=7, sticky="ew")

root.mainloop()
