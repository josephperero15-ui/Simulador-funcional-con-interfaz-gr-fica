import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox  # <--- Importación correcta para tu versión

from dataclasses import replace
from models import Personaje, ItemInventario, EstadoJuego
from logic import (
    procesar_accion_combate,
    crear_multiplicador_buff,
    filtrar_items_curativos,
    transformar_nombres_items,
    calcular_poder_total_inventario,
    registrar_bitacora_externa
)


class SimuladorFuncionalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador Funcional - Actividad Integradora U1 y U2")
        self.root.geometry("700x550")
        
        # Estado inmutable inicial
        self.estado = EstadoJuego(
            personaje=Personaje(nombre="Guerrero del Sistema", nivel=1, vida=100, vida_maxima=100, ataque_base=20, experiencia=0),
            inventario=[
                ItemInventario(nombre="Poción Menor", tipo="cura", valor=30),
                ItemInventario(nombre="Poción Mayor", tipo="cura", valor=60),
                ItemInventario(nombre="Escudo de Luz", tipo="defensa", valor=40)
            ],
            historial=[]
        )
        
        self.buff_maestro = crear_multiplicador_buff(1.4)
        
        self.construir_interfaz()

    def construir_interfaz(self):
        titulo = ttk.Label(self.root, text="Gestión de Arena Funcional (Python + TtkBootstrap)", font=("Helvetica", 13, "bold"))
        titulo.pack(pady=12)
        
        # Panel de Estado
        self.frame_stats = ttk.Labelframe(self.root, text=" Estado Actual del Personaje (Inmutable) ", padding=15)
        self.frame_stats.pack(fill=X, padx=20, pady=8)
        
        self.lbl_nombre = ttk.Label(self.frame_stats, text="", font=("Helvetica", 10))
        self.lbl_nombre.pack(anchor=W)
        self.lbl_nivel = ttk.Label(self.frame_stats, text="", font=("Helvetica", 10))
        self.lbl_nivel.pack(anchor=W)
        self.lbl_vida = ttk.Label(self.frame_stats, text="", font=("Helvetica", 10))
        self.lbl_vida.pack(anchor=W)
        self.lbl_exp = ttk.Label(self.frame_stats, text="", font=("Helvetica", 10))
        self.lbl_exp.pack(anchor=W)
        
        self.actualizar_etiquetas_stats()
      
        frame_acciones = ttk.Labelframe(self.root, text=" Acciones del Sistema (Match / Case) ", padding=15)
        frame_acciones.pack(fill=X, padx=20, pady=8)
        
        btn_atacar = ttk.Button(frame_acciones, text="Atacar", bootstyle=DANGER, command=lambda: self.gestionar_evento_accion("atacar"))
        btn_atacar.pack(side=LEFT, expand=True, padx=4)
        
        btn_descansar = ttk.Button(frame_acciones, text="Descansar", bootstyle=SUCCESS, command=lambda: self.gestionar_evento_accion("descansar"))
        btn_descansar.pack(side=LEFT, expand=True, padx=4)
        
        btn_entrenar = ttk.Button(frame_acciones, text="Entrenar Nivel", bootstyle=INFO, command=lambda: self.gestionar_evento_accion("entrenar"))
        btn_entrenar.pack(side=LEFT, expand=True, padx=4)

        # Panel de Herramientas Funcionales (Map, Filter, Reduce, Closures)
        frame_herramientas = ttk.Labelframe(self.root, text=" Herramientas Funcionales Avanzadas ", padding=15)
        frame_herramientas.pack(fill=X, padx=20, pady=8)
        
        btn_filtrar = ttk.Button(frame_herramientas, text="Procesar Inventario (Filter + Map + Reduce)", bootstyle=WARNING, command=self.ejecutar_herramientas_funcionales)
        btn_filtrar.pack(side=LEFT, expand=True, padx=4)
        
        btn_closure = ttk.Button(frame_herramientas, text="Aplicar Buff (Closure)", bootstyle=PRIMARY, command=self.ejecutar_closure)
        btn_closure.pack(side=LEFT, expand=True, padx=4)

    def actualizar_etiquetas_stats(self):
        p = self.estado.personaje
        self.lbl_nombre.config(text=f"Nombre: {p.nombre}")
        self.lbl_nivel.config(text=f"Nivel: {p.nivel}")
        self.lbl_vida.config(text=f"Vida actual: {p.vida} / {p.vida_maxima}")
        self.lbl_exp.config(text=f"Experiencia acumulada: {p.experiencia}")

    def gestionar_evento_accion(self, tipo: str):
        # Transición inmutable de estado
        nuevo_personaje = procesar_accion_combate(tipo, self.estado.personaje)
        self.estado = EstadoJuego(
            personaje=nuevo_personaje,
            inventario=self.estado.inventario,
            historial=self.estado.historial + [tipo]
        )
        self.actualizar_etiquetas_stats()
    
        registrar_bitacora_externa(f"Se ejecutó la acción '{tipo}' sobre la entidad {nuevo_personaje.nombre}")
        Messagebox.show_info(f"Acción '{tipo}' procesada correctamente mediante match/case.", "Proceso Exitoso")

    def ejecutar_herramientas_funcionales(self):
        filtrados = filtrar_items_curativos(self.estado.inventario)
        mapeados = transformar_nombres_items(filtrados)
        reducidos = calcular_poder_total_inventario(filtrados)
        
        texto = "Items de curación detectados (Filter + Map):\n" + "\n".join(mapeados) + f"\n\nValor curativo total acumulado (Reduce): {reducidos}"
        Messagebox.show_info(texto, "Reporte Funcional")

    def ejecutar_closure(self):
        base = self.estado.personaje.ataque_base
        resultado = self.buff_maestro(base)
        # CORRECCIÓN: Uso de Messagebox.show_info con (mensaje, título)
        Messagebox.show_info(f"Ataque base: {base}\nAtaque incrementado mediante Closure: {resultado}", "Closure Aplicado")


if __name__ == "__main__":
    app = ttk.Window(themename="flatly")
    SimuladorFuncionalApp(app)
    app.mainloop()
