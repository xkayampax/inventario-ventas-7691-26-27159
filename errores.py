class InventarioError(Exception):
    """Excepción base para todos los errores de nuestro sistema."""
    pass

class PrecioInvalidoError(InventarioError):
    pass

class StockInsuficienteError(InventarioError):
    pass

class ProductoNoEncontradoError(InventarioError):
    pass
