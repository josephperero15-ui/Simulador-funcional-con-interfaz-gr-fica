from functools import reduce
from dataclasses import replace
from typing import Callable, List
from models import Personaje, ItemInventario

def calcular_danio_base(nivel: int) -> int:

    return nivel * 15

def actualizar_vida_personaje(personaje: Personaje, delta: int) -> Personaje:
  
    nueva_vida = max(0, min(personaje.vida_maxima, personaje.vida + delta))
    return replace(personaje, vida=nueva_vida)

def filtrar_items_curativos(items: List[ItemInventario]) -> List[ItemInventario]:
    #Uso real de filter (Unidad 2): Filtra elementos de tipo curación."""
    return list(filter(lambda item: item.tipo == 'cura', items))

def transformar_nombres_items(items: List[ItemInventario]) -> List[str]:
    return list(map(lambda item: f"{item.nombre} (Efecto: +{item.valor})", items))

def calcular_poder_total_inventario(items: List[ItemInventario]) -> int:

    return reduce(lambda acumulado, item: acumulado + item.valor, items, 0)

# --- PATTERN MATCHING CON MATCH/CASE (Unidad 1) ---
def procesar_accion_combate(accion: str, personaje: Personaje) -> Personaje:
    # Procesa acciones del sistema mediante pattern matching estricto."""
    match accion.lower():
        case "atacar":
            return replace(personaje, experiencia=personaje.experiencia + 25)
        case "descansar":
            return actualizar_vida_personaje(personaje, 35)
        case "entrenar":
            return replace(personaje, nivel=personaje.nivel + 1, vida_maxima=personaje.vida_maxima + 20)
        case _:
            return personaje

# --- CLOSURE REAL (Unidad 2) ---
def crear_multiplicador_buff(factor_base: float) -> Callable[[int], int]:
    
    def aplicar_buff_especial(valor: int) -> int:
        return int(valor * factor_base)
    return aplicar_buff_especial

# --- FUNCIONES IMPURAS JUSTIFICADAS ---
def registrar_bitacora_externa(mensaje: str) -> None:
    with open("bitacora_sistema.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[LOG FUNCIONAL]: {mensaje}\n")