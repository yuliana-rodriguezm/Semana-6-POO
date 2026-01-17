from modelo.producto import Producto

# Clase hija Maquillaje
# Aquí se aplica:
# - HERENCIA
# - POLIMORFISMO

class Maquillaje(Producto):
    def __init__(self, nombre: str, precio: float, tipo_piel: str):
        
        # Llamamos al constructor de la clase base (HERENCIA)
        super().__init__(nombre, precio)
        self.tipo_piel = tipo_piel

    # Sobrescribimos el método (POLIMORFISMO)
    def mostrar_info(self) -> str:
        return (
            f"Maquillaje: {self._nombre} | "
            f"Precio: ${self._precio} | "
            f"Tipo de piel: {self.tipo_piel}"
        )


