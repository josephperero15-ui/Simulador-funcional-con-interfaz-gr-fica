Documento de Análisis Funcional - Simulador de Arena
1. Problema que resuelve la aplicación
Para este proyecto decidí desarrollar un simulador interactivo enfocado en la gestión de personajes y recursos dentro de una arena de combate. La aplicación permite administrar el estado de un héroe, ejecutar acciones tácticas como atacar, descansar o entrenar, y procesar colecciones de inventario aplicando de forma práctica los conceptos de la programación funcional en Python.

2. Estructuras de datos utilizadas
Para modelar las entidades del sistema (como Personaje, ItemInventario y EstadoJuego), utilicé dataclasses configuradas con la opción frozen=True. Esto lo hice con el propósito de garantizar que ninguna estructura pueda ser modificada directamente en memoria, asegurando un control estricto de los datos.

3. Dónde se aplicó la Unidad 1
Pattern Matching: Implementé bloques match/case dentro del módulo de lógica (logic.py). Me pareció la forma más limpia y declarativa de manejar las distintas acciones del usuario (atacar, descansar, entrenar) en lugar de usar múltiples if-elif-else anidados.

Modelado de datos: Se estructuró todo el dominio usando clases inmutables con dataclass.

Enfoque funcional vs. imperativo: Evité por completo el uso de variables globales mutables y bucles tradicionales que modifican estados sobre la marcha. En su lugar, preferí diseñar transformaciones de datos puras.

4. Dónde se aplicó la Unidad 2
Funciones Lambda: Las utilicé puntualmente para expresiones pequeñas y de una sola línea dentro de los predicados rápidos de filter y map.

Closures: Creé una fábrica de funciones llamada crear_multiplicador_buff. Su función es encapsular un factor matemático de configuración para aplicarlo de forma personalizada a los atributos del personaje sin recurrir a variables globales.

Inmutabilidad: Cada vez que el estado del programa cambia, el sistema no muta el objeto anterior, sino que devuelve una nueva instancia limpia utilizando dataclasses.replace.

Pureza y Efectos Secundarios: Separé la lógica de negocio pura (cálculos matemáticos y reglas de juego) de las operaciones que afectan al entorno exterior (como la interfaz o la escritura de archivos).

Herramientas funcionales: Integré el uso real de map para transformar los nombres y descripciones de los items, filter para aislar únicamente los elementos curativos, y reduce para calcular el valor total acumulado del inventario.

5. Partes puras e impuras
Funciones Puras: Son aquellas que no tienen efectos colaterales y siempre devuelven el mismo resultado con los mismos argumentos. En mi código destacan calcular_danio_base, actualizar_vida_personaje, filtrar_items_curativos, transformar_nombres_items, calcular_poder_total_inventario y procesar_accion_combate.

Funciones Impuras: Las concentré únicamente en la función registrar_bitacora_externa y en los eventos de la interfaz con Tkinter, ya que interactúan directamente con el sistema de archivos (bitacora_sistema.txt) y generan ventanas flotantes en pantalla.

6. Efectos secundarios existentes
El único efecto secundario controlado del sistema de dominio se produce al guardar un registro en texto plano de las acciones en el archivo bitacora_sistema.txt, además de la actualización visual de los componentes en la interfaz gráfica.

7. Manejo inmutable del estado
El estado global (EstadoJuego) evoluciona de manera funcional. Cada vez que interactúo con un botón de acción, el sistema genera un nuevo objeto inmutable con los valores actualizados, conservando la integridad de los datos anteriores en memoria.

8. Closure implementado y propósito
Implementé el closure crear_multiplicador_buff(factor_base). Su propósito principal es encapsular un multiplicador numérico que modifica los atributos de combate de manera dinámica, manteniendo un estado interno protegido sin contaminar el código con variables globales.

9. Partes sugeridas por la IA
La IA me ayudó a proponer la estructura modular inicial dividiendo el proyecto en tres archivos limpios (models.py, logic.py, main.py) y en la base para integrar ttkbootstrap con la arquitectura funcional.

10. Qué se corrigió o rechazó de la IA
Tuve que rechazar varias propuestas iniciales donde la IA intentaba meter toda la lógica de actualización directamente dentro de las funciones anónimas de los botones (callbacks). Modifiqué eso porque entendí que violaba la regla estricta del docente sobre la separación obligatoria de capas y la organización del código.

11. Aprendizajes técnicos
Con este trabajo aprendí a estructurar una aplicación modular real en Python aplicando un paradigma funcional estricto. Me quedó mucho más claro cómo controlar los efectos secundarios, por qué es útil la inmutabilidad y cómo implementar patrones avanzados como match/case y closures en un escenario práctico.