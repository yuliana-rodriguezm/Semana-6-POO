from modelo.producto import Producto

# Otra clase derivada para demostrar polimorfismo

class SkinCare(Producto):
    def __init__(self, nombre: str, precio: float, uso: str):
        super().__init__(nombre, precio)
        self.uso = uso

    def mostrar_info(self) -> str:
        return (
            f"SkinCare: {self._nombre} | "
            f"Precio: ${self._precio} | "
            f"Uso: {self.uso}"
        )
