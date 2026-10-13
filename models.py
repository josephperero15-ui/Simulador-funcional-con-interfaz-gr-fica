from dataclasses import dataclass, replace
from typing import List

@dataclass(frozen=True)
class Personaje:
    nombre: str
    nivel: int
    vida: int
    vida_maxima: int
    ataque_base: int
    experiencia: int

@dataclass(frozen=True)
class ItemInventario:
    nombre: str
    tipo: str  # 'cura', 'arma', 'buff'
    valor: int

@dataclass(frozen=True)
class EstadoJuego:
    personaje: Personaje
    inventario: List[ItemInventario]
    historial: List[str]