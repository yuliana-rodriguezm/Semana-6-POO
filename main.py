from servicios.tienda_service import TiendaService

def main():
    print("TIENDA DE COSMÉTICOS\n")

    tienda = TiendaService()

    tienda.agregar_maquillaje(
        "Corrector en barra",
        10.50,
        "Piel semiseca a seca"
    )

    tienda.agregar_maquillaje(
        "Polvo Compacto de alta cobertura",
        12.00,
        "Piel grasa"
    )

    tienda.agregar_skincare(
        "Crema Hidratante Nocturna",
        18.00,
        "Uso diario antes de dormir"
    )

    tienda.agregar_skincare(
        "Serum rejuvenecedor",
        26.00,
        "Uso diario para piel madura"
    )

    print("== Productos disponibles ==")
    tienda.mostrar_productos()

if __name__ == "__main__":
    main()

