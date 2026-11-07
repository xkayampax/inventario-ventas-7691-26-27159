from .excepciones import ProductoNoEncontradoError

class Inventario:
    def __init__(self):
        
        # La llave será el código (str) y el valor será el objeto Producto entero.
        self._productos = {}

        # Los sets son geniales porque ignoran automáticamente los duplicados.
        self._categorias = set()

    def agregar(self, producto):
        """Agrega un objeto Producto al diccionario de inventario."""
        codigo_str = str(producto.codigo)
        self._productos[codigo_str] = producto
        self._categorias.add(producto.categoria.lower())

    def buscar_por_codigo(self, codigo):
        """Busca un producto exacto. Lanza error si no existe."""
        codigo_str = str(codigo)
        if codigo_str not in self._productos:
            # REQUISITO 3.8: Lanzar excepciones personalizadas en la capa de lógica
            raise ProductoNoEncontradoError(f"No existe un producto con el código {codigo}.")
        
        # Retorna el objeto Producto completo
        return self._productos[codigo_str]

    def buscar_por_nombre(self, texto):
        """
        REQUISITO 3.9 (Cadenas): Búsqueda parcial sin distinguir mayúsculas.
        Retorna una lista con todos los productos que coincidan.
        """
        texto_lower = texto.lower()
        encontrados = []
        for producto in self._productos.values():
            if texto_lower in producto.nombre.lower():
                encontrados.append(producto)
        return encontrados

    def obtener_ordenados(self, criterio="nombre"):

        # Extraemos todos los objetos Producto del diccionario y los hacemos lista
        lista_productos = list(self._productos.values())
        
        if criterio == "nombre":
            # Ordena alfabéticamente ignorando mayúsculas
            return sorted(lista_productos, key=lambda p: p.nombre.lower())
        elif criterio == "stock":
            # Ordena de menor a mayor cantidad
            return sorted(lista_productos, key=lambda p: p.stock)
        elif criterio == "precio":
            # Ordena del más barato al más caro
            return sorted(lista_productos, key=lambda p: p.precio)
        else:
            return lista_productos

    
    def __len__(self):
        """Permite al sistema hacer len(mi_inventario) para saber cuántos productos hay."""
        return len(self._productos)

    def __contains__(self, codigo):
        """Permite al sistema preguntar 'if codigo in mi_inventario' directamente."""
        return str(codigo) in self._productos

    def __iter__(self):
        """Permite usar un ciclo 'for producto in mi_inventario' sin extraer el diccionario manualmente."""
        return iter(self._productos.values())