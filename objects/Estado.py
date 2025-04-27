import tkinter as tk

class Estado:
    def __init__(self, canvas, nombre, final, coordenadas):
        self.canvas = canvas
        self.nombre = nombre
        self.final = final
        self.activo = False
        self.coordenadas = coordenadas
        self.estado = None
        self.estado_interno = None  # Para guardar referencia al círculo interno si es final
        self.texto = None  # Para guardar referencia al texto
        self.cantidad_repeticiones = 0

        self.dibujar_estado()

    def __str__(self):
        return f"Estado: {self.nombre}, Final: {self.final}, Activo: {self.activo}"

    def dibujar_estado(self):
        if self.estado:
            self.canvas.delete(self.estado)
        if self.estado_interno:
            self.canvas.delete(self.estado_interno)
        if self.texto:
            self.canvas.delete(self.texto)

        x, y = self.coordenadas
        radio = 20

        color = "blue" if self.activo else "black"
        grosor = 2 + self.cantidad_repeticiones

        self.estado = self.canvas.create_oval(
            x - radio, y - radio, x + radio, y + radio,
            outline=color,
            width=grosor,
            fill="white"
        )

        if self.final:
            margen = 4
            self.estado_interno = self.canvas.create_oval(
                x - radio + margen, y - radio + margen,
                x + radio - margen, y + radio - margen,
                outline=color,
                width=grosor,
                fill="white"
            )

        self.texto = self.canvas.create_text(
            x, y,
            text=self.nombre,
            fill="black"  # Cambiado de rojo a negro
        )

    def activar_estado(self):
        self.activo = True
        self.cantidad_repeticiones += 1
        self.dibujar_estado()

    def desactivar_estado(self):
        self.activo = False
        self.cantidad_repeticiones = 0
        self.dibujar_estado()

    def se_acepto(self):
        self.canvas.itemconfig(self.estado, outline="green")
        if self.final and self.estado_interno:
            self.canvas.itemconfig(self.estado_interno, outline="green")

    def no_se_acepto(self):
        self.canvas.itemconfig(self.estado, outline="red")
        if self.final and self.estado_interno:
            self.canvas.itemconfig(self.estado_interno, outline="red")

    def get_coordenadas(self):
        return self.coordenadas