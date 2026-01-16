# Clase base Producto
# Aquí aplicamos ENCAPSULACIÓN y definimos atributos y métodos comunes

class Producto:
    def __init__(self, nombre: str, precio: float):
        # Atributos protegidos (encapsulación)
        self._nombre = nombre
        self._precio = precio

    # Getter
    def obtener_nombre(self) -> str:
        return self._nombre

    # Getter
    def obtener_precio(self) -> float:
        return self._precio

    # Setter
    def cambiar_precio(self, nuevo_precio: float) -> None:
        self._precio = nuevo_precio

    # Método que será sobrescrito (POLIMORFISMO)
    def mostrar_info(self) -> str:
        return f"Producto: {self._nombre} - Precio: ${self._precio}"
