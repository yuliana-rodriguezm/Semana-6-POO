# Clase derivada Cosmetico
# Aquí aplicamos HERENCIA y POLIMORFISMO

from Modelo.producto import Producto


class Cosmetico(Producto):
    def __init__(self, nombre: str, precio: float, tipo_piel: str):
        # Llamamos al constructor de la clase base (herencia)
        super().__init__(nombre, precio)
        self.tipo_piel = tipo_piel

    # Sobrescribimos el método (POLIMORFISMO)
    def mostrar_info(self) -> str:
        return (
            f"Cosmético: {self._nombre} | "
            f"Precio: ${self._precio} | "
            f"Tipo de piel: {self.tipo_piel}"
        )
