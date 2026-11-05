from dataclasses import dataclass
from .excepciones import PrecioInvalidoError, StockInsuficienteError

# REQUISITO 3.9: Venta inmutable con @dataclass(frozen=True)
@dataclass(frozen=True)


class Producto:
    def __init__(self, codigo, nombre, presentacion, categoria, precio, stock):
        self.codigo = str(codigo)
        self.nombre = str(nombre)
        self.presentacion = str(presentacion)
        self.categoria = str(categoria)
        self.precio = precio
        self.stock = stock

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if float(nuevo_precio) < 0:
            raise PrecioInvalidoError(f"El precio no puede ser negativo: {nuevo_precio}")
        self._precio = float(nuevo_precio)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock):
        if int(nuevo_stock) < 0:
            raise StockInsuficienteError("El stock no puede quedar por debajo de cero.")
        self._stock = int(nuevo_stock)

    def descontar_stock(self, cantidad):
        self.stock -= cantidad

    def __str__(self):
        return f"[{self.codigo}] {self.nombre.capitalize()} | {self.categoria.capitalize()} | Q{self.precio:.2f} | Stock: {self.stock}"
        return f"[{self.codigo}] {self.nombre.capitalize()} - {self.categoria.capitalize()} | Q{self.precio:.2f} | Stock: {self.stock}"