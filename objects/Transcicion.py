import tkinter as tk
import math


class Transicion:
    def __init__(self, canvas, nombre, origen, destino, coordenadas=None, es_lazo=False):
        self.canvas = canvas
        self.nombre = nombre
        self.origen = origen
        self.destino = destino
        self.activo = False
        self.transicion = None
        self.id_texto = None
        self.cantidad_repeticiones = 0
        self.es_lazo = es_lazo

        if coordenadas is None:
            self.calcular_coordenadas()
        else:
            self.coordenadas = coordenadas

        self.dibujar_transicion()

    def __str__(self):
        return f"Transicion: {self.nombre}, Origen: {self.origen.nombre}, Destino: {self.destino.nombre}"

    def calcular_coordenadas(self):
        x1, y1 = self.origen.coordenadas
        x2, y2 = self.destino.coordenadas

        if self.es_lazo:
            self.tipo = "bucle"
            self.coordenadas = (x1, y1)
        else:
            radio = 20
            dx = x2 - x1
            dy = y2 - y1
            longitud = math.sqrt(dx * dx + dy * dy)

            if longitud > 0:
                nx = dx / longitud
                ny = dy / longitud

                x1_ajustado = x1 + nx * radio
                y1_ajustado = y1 + ny * radio
                x2_ajustado = x2 - nx * radio
                y2_ajustado = y2 - ny * radio

                self.coordenadas = (x1_ajustado, y1_ajustado, x2_ajustado, y2_ajustado)
                self.tipo = "recto"

    def dibujar_transicion(self):
        if self.transicion:
            self.canvas.delete(self.transicion)
            self.transicion = None
        if self.id_texto:
            self.canvas.delete(self.id_texto)
            self.id_texto = None

        color = "blue" if self.activo else "black"
        grosor = 2 + self.cantidad_repeticiones

        if self.es_lazo:
            x, y = self.origen.get_coordenadas()
            largo = 25
            espacio = 15
            offset_x = 15
            offset_y = -20

            self.transicion = self.canvas.create_line(
                x + offset_x, y + offset_y,
                x + offset_x, y - largo + offset_y,
                x - largo + offset_x, y - largo + offset_y,
                x - largo + offset_x, y + offset_y,
                fill=color,
                width=grosor,
                arrow=tk.LAST
            )

            self.id_texto = self.canvas.create_text(
                x - largo + offset_x - espacio, y - largo + offset_y,
                text=self.nombre,
                fill=color
            )

        else:
            x1, y1, x2, y2 = self.coordenadas

            self.transicion = self.canvas.create_line(
                x1, y1, x2, y2,
                fill=color,
                width=grosor,
                arrow=tk.LAST
            )

            medio_x = (x1 + x2) / 2
            medio_y = (y1 + y2) / 2

            offset = 15
            if abs(y2 - y1) < 10:
                medio_y -= offset

            self.id_texto = self.canvas.create_text(
                medio_x, medio_y,
                text=self.nombre,
                fill=color
            )

    def activar_transicion(self):
        self.activo = True
        self.cantidad_repeticiones += 1
        self.dibujar_transicion()

    def desactivar_transicion(self):
        self.activo = False
        self.cantidad_repeticiones = 0
        self.dibujar_transicion()

    def se_acepto(self):
        self.canvas.itemconfig(self.transicion, fill="green")

    def no_se_acepto(self):
        self.canvas.itemconfig(self.transicion, fill="red")