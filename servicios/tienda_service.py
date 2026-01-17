from modelo.maquillaje import Maquillaje
from modelo.skincare import SkinCare

# Servicio: lógica del sistema

class TiendaService:
    def __init__(self):
        self.productos = []

    def agregar_maquillaje(self, nombre, precio, tipo_piel):
        self.productos.append(Maquillaje(nombre, precio, tipo_piel))

    def agregar_skincare(self, nombre, precio, uso):
        self.productos.append(SkinCare(nombre, precio, uso))

    def mostrar_productos(self):
       
        # POLIMORFISMO:
        # todos usan mostrar_info(), pero cada uno se comporta distinto
        for p in self.productos:
            print(p.mostrar_info())

