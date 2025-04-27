import customtkinter as ctk
import tkinter as tk

from objects.Automata import Automata
from objects.Estado import Estado
from objects.Transcicion import Transicion

automata = {
    "1": [("2", "a"), ("1", "b")],
    "2": [("3", "b"), ("5", "d")],
    "3": [("4", "c"), ("3", "a")],
    "4": [("5", "e")]
}

class Aplicacion:
    def __init__(self, interfaz):
        self.interfaz = interfaz
        self.interfaz.title("Automata")
        self.interfaz.geometry("1250x700")
        self.interfaz.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.interfaz.grid_rowconfigure(0, weight=1)
        self.interfaz.grid_columnconfigure(0, weight=1)
        self.interfaz.grid_columnconfigure(1, weight=1)

        self.marco_izquierdo = ctk.CTkFrame(self.interfaz, width=500, height=650, corner_radius=15)
        self.marco_izquierdo.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.etiqueta_titulo = ctk.CTkLabel(self.marco_izquierdo, text="Automata",
                                            font=ctk.CTkFont(family="Roboto", size=24, weight="bold"), anchor="center")
        self.etiqueta_titulo.grid(row=0, column=0, pady=(15, 10), padx=20, sticky="ew", columnspan=2)

        self.entrada_cadena = ctk.CTkEntry(self.marco_izquierdo, placeholder_text="Cadena a analizar", width=400,
                                           height=40, border_width=2, corner_radius=10, font=ctk.CTkFont(size=15))
        self.entrada_cadena.grid(row=1, column=0, pady=(0, 15), padx=20, sticky="ew", columnspan=2)

        self.frame_botones = ctk.CTkFrame(self.marco_izquierdo, fg_color="transparent")
        self.frame_botones.grid(row=2, column=0, pady=(0, 15), padx=20, sticky="ew", columnspan=2)
        self.frame_botones.grid_columnconfigure(0, weight=4)
        self.frame_botones.grid_columnconfigure(1, weight=1)

        self.boton_validar = ctk.CTkButton(self.frame_botones, text="Validar cadena",
                                           command=self.validar_cadena, height=40, fg_color="#3498db",
                                           hover_color="#2980b9", font=ctk.CTkFont(size=16), corner_radius=10)
        self.boton_validar.grid(row=0, column=0, padx=(0, 5), sticky="ew")

        self.boton_limpiar = ctk.CTkButton(self.frame_botones, text="🧹", command=self.limpiar_campos, width=40,
                                           height=40, fg_color="#e74c3c", hover_color="#c0392b",
                                           font=ctk.CTkFont(size=16), corner_radius=10)
        self.boton_limpiar.grid(row=0, column=1, padx=(5, 0), sticky="e")

        self.etiqueta_resultado = ctk.CTkLabel(self.marco_izquierdo, text="", font=ctk.CTkFont(size=18, weight="bold"),
                                               anchor="center")
        self.etiqueta_resultado.grid(row=3, column=0, pady=(0, 10), padx=20, sticky="ew", columnspan=2)

        self.marco_expresion = ctk.CTkFrame(self.marco_izquierdo, corner_radius=10)
        self.marco_expresion.grid(row=4, column=0, pady=(5, 15), padx=20, sticky="ew", columnspan=2)

        self.etiqueta_expresion_titulo = ctk.CTkLabel(self.marco_expresion, text="Lenguaje",
                                                      font=ctk.CTkFont(size=16, weight="bold"), anchor="center")
        self.etiqueta_expresion_titulo.grid(row=0, column=0, pady=(10, 0), padx=20, sticky="ew")

        self.etiqueta_expresion = ctk.CTkLabel(self.marco_expresion, text="", font=ctk.CTkFont(size=12), wraplength=420,
                                               justify="center", anchor="center")
        self.etiqueta_expresion.grid(row=1, column=0, pady=(0, 10), padx=20, sticky="ew")

        self.etiqueta_analisis_titulo = ctk.CTkLabel(self.marco_izquierdo, text="Análisis de Cadena",
                                                     font=ctk.CTkFont(size=16, weight="bold"), anchor="center")
        self.etiqueta_analisis_titulo.grid(row=5, column=0, pady=(5, 10), padx=20, sticky="ew", columnspan=2)

        self.area_analisis_cadena = ctk.CTkTextbox(self.marco_izquierdo, width=400, height=300,
                                                   font=ctk.CTkFont(size=18),  # Aumentar tamaño de texto
                                                   corner_radius=10, border_width=2)
        self.area_analisis_cadena.grid(row=6, column=0, pady=(5, 20), padx=20, sticky="ew", columnspan=2)

        self.marco_derecho = ctk.CTkFrame(self.interfaz, width=500, height=100, corner_radius=15)
        self.marco_derecho.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

        self.titulo_automata = ctk.CTkLabel(self.marco_derecho, text="Diagrama del Autómata",
                                            font=ctk.CTkFont(family="Roboto", size=24, weight="bold"), anchor="center")
        self.titulo_automata.grid(row=0, column=0, pady=(15, 5), padx=20, sticky="ew")

        self.canvas_automata = tk.Canvas(self.marco_derecho, width=700, height=400, bg="#F0F0F0", highlightthickness=0)
        self.canvas_automata.grid(row=1, column=0, pady=(0, 20), padx=20)

        lenguaje_automata = 'a(ba)*d + a(ba)*c(e)'
        self.etiqueta_expresion.configure(text=lenguaje_automata, text_color="gray")

        self.inicializar_automata()

    def inicializar_automata(self):
        self.estados = {}

        self.estados["1"] = Estado(self.canvas_automata, "1", False, (100, 150))
        self.estados["2"] = Estado(self.canvas_automata, "2", False, (250, 150))
        self.estados["3"] = Estado(self.canvas_automata, "3", False, (400, 150))
        self.estados["4"] = Estado(self.canvas_automata, "4", False, (550, 150))
        self.estados["5"] = Estado(self.canvas_automata, "5", True, (550, 250))

        self.transiciones = []

        self.transiciones.append(Transicion(self.canvas_automata, "b", self.estados["1"], self.estados["1"], es_lazo=True))
        self.transiciones.append(Transicion(self.canvas_automata, "a", self.estados["1"], self.estados["2"]))
        self.transiciones.append(Transicion(self.canvas_automata, "b", self.estados["2"], self.estados["3"]))
        self.transiciones.append(Transicion(self.canvas_automata, "\nd", self.estados["2"], self.estados["5"]))
        self.transiciones.append(Transicion(self.canvas_automata, "a", self.estados["3"], self.estados["3"], es_lazo=True))
        self.transiciones.append(Transicion(self.canvas_automata, "c", self.estados["3"], self.estados["4"]))
        self.transiciones.append(Transicion(self.canvas_automata, "\te", self.estados["4"], self.estados["5"]))

        x, y = self.estados["1"].coordenadas
        self.canvas_automata.create_line(x - 50, y, x - 25, y, arrow=tk.LAST, width=2)
        self.canvas_automata.create_text(x - 35, y - 15, text="Inicio", fill="black")

    def validar_cadena(self):
        cadena = self.entrada_cadena.get()
        lenguaje_automata = 'a(ba)*d + a(ba)*c(e)'

        for estado in self.estados.values():
            estado.activo = False
            estado.cantidad_repeticiones = 0
            estado.dibujar_estado()

        for transicion in self.transiciones:
            transicion.activo = False
            transicion.cantidad_repeticiones = 0
            transicion.dibujar_transicion()

        # Habilitar temporalmente para modificar el contenido
        self.area_analisis_cadena.configure(state="normal")
        self.area_analisis_cadena.delete(0.0, "end")

        if cadena.strip() == "" or not cadena:
            self.etiqueta_resultado.configure(text="Cadena vacía ε", text_color="orange")
            self.etiqueta_expresion.configure(text=lenguaje_automata, text_color="gray")  # Color neutro
            self.area_analisis_cadena.insert("1.0", "ε")
            self.area_analisis_cadena.configure(state="disabled")  # Deshabilitar después de modificar
            return




        automata_obj = Automata("1", "5", automata)
        pasos, self.seAcepta = automata_obj.analizar_cadena(cadena)

        if pasos[-1].startswith("\n🎉") or self.seAcepta:
            self.etiqueta_resultado.configure(text="Cadena ACEPTADA", text_color="green")
            self.etiqueta_expresion.configure(text=lenguaje_automata, text_color="green")  # Verde si se acepta
        else:
            self.etiqueta_resultado.configure(text="Cadena RECHAZADA", text_color="red")
            self.etiqueta_expresion.configure(text=lenguaje_automata, text_color="red")  # Rojo si se rechaza

        # Deshabilitar después de borrar el contenido y antes de iniciar la animación
        self.area_analisis_cadena.configure(state="disabled")

        # Comenzar la animación con la escritura simultánea
        self.interfaz.after(100, lambda: self.animar_recorrido(pasos, 0))

    def animar_recorrido(self, pasos, indice):
        if indice >= len(pasos):
            # Una vez terminada la animación, colorear estados y transiciones según el resultado
            if self.seAcepta:
                # Colorear de verde si se aceptó
                for estado_nombre in self.lista_estados_recorridos:
                    self.estados[estado_nombre].se_acepto()
                for transicion in self.lista_transiciones_recorridos:
                    transicion.se_acepto()
            else:
                # Colorear de rojo si no se aceptó
                for estado_nombre in self.lista_estados_recorridos:
                    self.estados[estado_nombre].no_se_acepto()
                for transicion in self.lista_transiciones_recorridos:
                    transicion.no_se_acepto()
            return

        self.lista_estados_recorridos = [] if indice == 0 else self.lista_estados_recorridos
        self.lista_transiciones_recorridos = [] if indice == 0 else self.lista_transiciones_recorridos
        paso = pasos[indice]

        # Escribir el paso actual en el área de análisis
        if indice > 0:  # Evitar escribir el paso inicial repetido
            texto_paso = paso.split("➡️ ")[1] if "➡️ " in paso else paso

            # Habilitar temporalmente para agregar texto
            self.area_analisis_cadena.configure(state="normal")
            self.area_analisis_cadena.insert("end", texto_paso)
            self.area_analisis_cadena.see("end")  # Auto-scroll para ver siempre lo último
            self.area_analisis_cadena.configure(state="disabled")  # Deshabilitar después
            self.area_analisis_cadena.update()

        if "➡️" in paso:
            partes = paso.split("➡️ ")[1]
            estado_actual = partes[0]

            if estado_actual in self.estados:
                self.estados[estado_actual].activar_estado()
                if estado_actual not in self.lista_estados_recorridos:
                    self.lista_estados_recorridos.append(estado_actual)

                if indice > 0 and "➡️" in pasos[indice - 1]:
                    estado_anterior = pasos[indice - 1].split("➡️ ")[1][0]

                    lazo_encontrado = False
                    if estado_anterior == estado_actual:
                        for t in self.transiciones:
                            if t.origen.nombre == estado_actual and t.destino.nombre == estado_actual and t.es_lazo:
                                t.activar_transicion()
                                if t not in self.lista_transiciones_recorridos:
                                    self.lista_transiciones_recorridos.append(t)
                                lazo_encontrado = True
                                break

                    if not lazo_encontrado:
                        for t in self.transiciones:
                            if t.origen.nombre == estado_anterior and t.destino.nombre == estado_actual:
                                t.activar_transicion()
                                if t not in self.lista_transiciones_recorridos:
                                    self.lista_transiciones_recorridos.append(t)
                                break

        # Programar el siguiente paso
        self.interfaz.after(500, lambda: self.animar_recorrido(pasos, indice + 1))

    def limpiar_campos(self):
        self.entrada_cadena.delete(0, 'end')

        # Habilitar temporalmente para limpiar
        self.area_analisis_cadena.configure(state="normal")
        self.area_analisis_cadena.delete(0.0, "end")
        self.area_analisis_cadena.configure(state="disabled")  # Deshabilitar después

        self.etiqueta_resultado.configure(text="", text_color="black")

        # Volver el lenguaje a color neutro
        lenguaje_automata = 'a(ba)*d + a(ba)*c(e)'
        self.etiqueta_expresion.configure(text=lenguaje_automata, text_color="gray")

        for estado in self.estados.values():
            estado.desactivar_estado()

        for transicion in self.transiciones:
            transicion.desactivar_transicion()

