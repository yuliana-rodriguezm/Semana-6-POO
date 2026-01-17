# Clase base Producto
# Aquí se aplica:
# - ENCAPSULACIÓN
# - BASE PARA HERENCIA

class Producto:
    def __init__(self, nombre: str, precio: float):
       
        # Atributos protegidos (encapsulación)
        self._nombre = nombre
        self._precio = precio

    # Método común (será sobrescrito → polimorfismo)
    def mostrar_info(self) -> str:
        return f"Producto: {self._nombre} | Precio: ${self._precio}"
