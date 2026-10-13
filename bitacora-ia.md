# Bitácora de Uso de Inteligencia Artificial

## Prompt 1: Estructura modular inicial
* **Prompt usado:** "Ayúdame a estructurar un proyecto en Python con Tkinter y TtkBootstrap que cumpla con programación funcional separando capas de datos, lógica y visual."
* **Sugerencia de la IA:** Propuso dividir el proyecto en tres archivos principales (`models.py`, `logic.py`, `main.py`) usando `dataclasses`[cite: 3].
* **Decisión:** Aceptado por completo, ya que cumple exactamente con la restricción de diseño obligatoria de separar la interfaz, la lógica y el estado[cite: 3].

## Prompt 2: Implementación de Closures y Herramientas Funcionales
* **Prompt usado:** "Muéstrame un ejemplo claro de closure real aplicado a estadísticas de un juego y cómo integrar map, filter y reduce."
* **Sugerencia de la IA:** Fábrica de funciones con funciones anidadas y uso de `reduce` con funciones lambda[cite: 4].
* **Decisión:** Modificado parcialmente. Se adaptó la lógica del closure para que sea una fábrica clara de multiplicadores de atributos y se estructuró `reduce` para sumar valores del inventario de forma limpia[cite: 4].

## Prompt 3: Control de efectos secundarios y funciones impuras
* **Prompt usado:** "¿Cómo puedo justificar funciones impuras que escriban en archivos sin romper la pureza del dominio?"
* **Sugerencia de la IA:** Aislar las operaciones de escritura de archivos en funciones separadas fuera de la lógica de negocio[cite: 4].
* **Decisión:** Aceptado. Se implementó `registrar_bitacora_externa` de forma independiente para cumplir rigurosamente con los requisitos del docente[cite: 4].