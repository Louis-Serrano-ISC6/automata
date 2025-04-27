class Automata:
    def __init__(self, estado_inicial: str, estado_final: str, automata: dict):
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.automata = automata

    def analizar_cadena(self, cadena: str) -> list:
        estado_actual = self.estado_inicial
        pasos = [f"🚀 Estado inicial: {estado_actual}{cadena}\n"]

        pasos.append(f"➡️ {estado_actual}{cadena}\n")

        for i in range(len(cadena)):
            if not cadena:
                break  # Por si la cadena ya está vacía
            simbolo = cadena[0]
            transiciones = self.automata.get(estado_actual, [])
            encontrada = False

            for destino, letra_valida in transiciones:
                if simbolo == letra_valida:
                    estado_actual = destino
                    cadena = cadena[1:]  # Avanzamos al siguiente símbolo
                    pasos.append(f"➡️ {estado_actual}{cadena}\n")

                    encontrada = True
                    break

            if not encontrada:
                break

        if estado_actual == self.estado_final:
            pasos.append(f"{estado_actual} ϵ F ∴ se acepta\n")
            return pasos, True
        else:
            pasos.append(f"{estado_actual} ∉ F ∴ se rechaza\n")
            return pasos, False
