# Simulador de Autómatas Finitos

Este proyecto es un simulador visual de autómatas finitos deterministas (AFD) desarrollado con Python y la biblioteca CustomTkinter. Permite visualizar y validar cadenas en un autómata de forma interactiva, mostrando el recorrido paso a paso tanto gráficamente como en una descripción textual.

## Características

- **Interfaz gráfica intuitiva** diseñada con CustomTkinter
- **Visualización dinámica del autómata** con estados y transiciones
- **Animación paso a paso** del recorrido del autómata al validar una cadena
- **Representación visual del resultado** con códigos de color (verde para cadenas aceptadas, rojo para rechazadas)
- **Descripción detallada** del análisis de cada cadena
- **Validación del lenguaje** para la expresión regular `a(ba)*d + a(ba)*c(e)`

## Requisitos

- Python 3.6 o superior
- CustomTkinter
- Tkinter (incluido con la mayoría de las instalaciones de Python)

## Instalación

1. Clona este repositorio o descarga los archivos
2. Instala las dependencias:
   ```bash
   pip install customtkinter
   ```
3. Ejecuta el programa principal:
   ```bash
   python main.py
   ```

## Uso

1. Ingresa una cadena a validar en el campo de texto
2. Haz clic en "Validar cadena" para iniciar la simulación
3. Observa la animación del recorrido por el autómata
4. Revisa el resultado (aceptado o rechazado) y la descripción del análisis
5. Usa el botón de limpiar (🧹) para reiniciar el simulador

## Estructura del proyecto

- `main.py`: Archivo principal que ejecuta la aplicacion
- `objects/Estado.py`: Clase para representar estados del autómata
- `objects/Transcicion.py`: Clase para representar transiciones entre estados
- `objects/Automata.py`: Clase para analizar la cadena de acuerdo al automata
- `Aplicacion.py`: Clase que realiza la interfaz grafica

## Detalle del Autómata Implementado

El programa implementa por defecto un autómata que reconoce el lenguaje `a(ba)*d + a(ba)*c(e)`. Este autómata tiene:

- 5 estados (numerados del 1 al 5)
- Estado inicial: 1
- Estado final: 5
- Transiciones:
  - Del estado 1 a sí mismo con el símbolo 'b'
  - Del estado 1 al estado 2 con el símbolo 'a'
  - Del estado 2 al estado 3 con el símbolo 'b'
  - Del estado 2 al estado 5 con el símbolo 'd'
  - Del estado 3 a sí mismo con el símbolo 'a'
  - Del estado 3 al estado 4 con el símbolo 'c'
  - Del estado 4 al estado 5 con el símbolo 'e'

## Funcionamiento

1. **Inicialización**: Al iniciar, el programa dibuja el autómata en el canvas.
2. **Validación**: Al introducir una cadena, la aplicación:
   - Simula el recorrido estado por estado
   - Resalta visualmente cada estado y transición visitada
   - Muestra el análisis de la cadena en tiempo real
   - Indica el resultado final (aceptada o rechazada)
3. **Finalización**: Al completar el análisis:
   - Los estados y transiciones visitados se colorean en verde (si la cadena es aceptada) o en rojo (si es rechazada)
   - Se muestra un mensaje indicando si la cadena pertenece o no al lenguaje

## Personalización

El código está estructurado para permitir modificaciones sencillas:
- Se puede cambiar el autómata modificando el diccionario `automata` en el código principal
- Es posible ajustar la apariencia visual modificando los parámetros de las clases `Estado` y `Transicion`
- La velocidad de la animación puede ajustarse cambiando el valor en `self.interfaz.after(500, ...)`

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y personal.

## Colaboradores

- Louis Gerardo Serrano Alamo
- Carlos Emmanuel Gonzalez Alvarez

---

*Este simulador de autómatas fue desarrollado como proyecto educativo para la comprensión y visualización de autómatas finitos deterministas.*
