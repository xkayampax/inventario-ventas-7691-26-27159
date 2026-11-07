from inventario.app import SistemaInventario
import os

if __name__ == "__main__":
    # Asegura que la carpeta de datos exista antes de arrancar
    os.makedirs("datos", exist_ok=True)
    
    # Lanza todo el sistema de POO
    SistemaInventario("datos/inventario.csv").ejecutar()