from abc import ABC, abstractmethod

class ReglaNegocio(ABC):
    
    @abstractmethod
    def revisar(self, producto):
        """Todo hijo de ReglaNegocio DEBE tener un método llamado 'revisar'."""
        pass

class AlertaStockMinimo(ReglaNegocio):
    def __init__(self, umbral=5):
        self.umbral = umbral
        
    def revisar(self, producto):
        if producto.stock < self.umbral:
            return f"⚠️ ¡Atención! El stock de {producto.nombre.capitalize()} es crítico ({producto.stock} unidades)."
        return None