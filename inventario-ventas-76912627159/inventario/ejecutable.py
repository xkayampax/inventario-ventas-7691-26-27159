import datetime
from .inventario import Inventario
from .prod_ve import Producto, Venta
from .documentacion import RepositorioCSV, Bitacora
from .reportes import ReporteVentas
from .reglas import AlertaStockMinimo
from .errores import InventarioError

class SistemaInventario:
    def __init__(self, ruta_inventario):
        self.inventario = Inventario()
        self.repo = RepositorioCSV(ruta_inventario)
        self.bitacora = Bitacora()
        self.regla_alerta = AlertaStockMinimo(umbral=5)
        
        # Cargar datos al iniciar
        self.repo.cargar_inventario(self.inventario)
        self.bitacora.registrar("Sistema iniciado y datos cargados.")

    def ejecutar(self):
        while True:
            print("\n--- MENÚ FARMACIA BENDICIÓN (POO) ---")
            print("1. Agregar producto")
            print("2. Consultar producto")
            print("3. Registrar venta")
            print("4. Mostrar inventario")
            print("5. Generar reporte")
            print("6. Salir y guardar cambios")
            
            opcion = input("Selecciona una opción: ")
            
            try:
                if opcion == "1":
                    self._agregar_producto()
                elif opcion == "2":
                    self._consultar_producto()
                elif opcion == "3":
                    self._registrar_venta()
                elif opcion == "4":
                    self._mostrar_inventario()
                elif opcion == "5":
                    self._generar_reporte()
                elif opcion == "6":
                    self._salir()
                    break
                else:
                    print("❌ Opción no válida.")
                    
            # CAPTURA DE EXCEPCIONES: Mantiene el programa vivo
            except ValueError:
                print("❌ Error: Por favor ingresa un dato numérico válido.")
            except InventarioError as e:
                print(f"❌ Error de Inventario: {e}")
            except Exception as e:
                print(f"❌ Ocurrió un error inesperado: {e}")

    def _agregar_producto(self):
        codigo = input("Código del producto: ")
        if codigo in self.inventario:
            print(f"❌ Error: Ya existe un producto con el código {codigo}.")
            return
            
        nombre = input("Nombre del producto: ").strip().lower()
        presentacion = input("Tipo de presentación: ").strip().lower()
        categoria = input("Tipo de categoría: ").strip().lower()
        precio = input("Precio del producto: ")
        stock = input("Cantidad del producto: ")
        
        prod = Producto(codigo, nombre, presentacion, categoria, precio, stock)
        self.inventario.agregar(prod)
        self.bitacora.registrar(f"Producto agregado: {nombre} (Código: {codigo})")
        print("✅ Producto agregado exitosamente.")

    def _consultar_producto(self):
        codigo = input("Ingrese el código del producto a consultar: ")
        prod = self.inventario.buscar_por_codigo(codigo)
        print("\n✅ Producto encontrado:")
        print(prod)

    def _registrar_venta(self):
        codigo = input("Ingrese el código del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))
        
        prod = self.inventario.buscar_por_codigo(codigo)
        prod.descontar_stock(cantidad) # Valida matemáticamente
        
        # POLIMORFISMO: Aplica la regla de negocio
        alerta = self.regla_alerta.revisar(prod)
        if alerta:
            print(alerta)
        
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        venta = Venta(fecha_hora, prod.codigo, cantidad)
        
        self.repo.registrar_venta(venta)
        self.bitacora.registrar(f"Venta: {cantidad} unidades del código {codigo}")
        print(f"✅ Venta registrada. Nuevo stock: {prod.stock}")

    def _mostrar_inventario(self):
        if len(self.inventario) == 0:
            print("El inventario está vacío.")
            return
            
        print("\n¿Cómo deseas ordenar el inventario?")
        print("1. Por Nombre (A - Z)")
        print("2. Por Stock (menor a mayor)")
        print("3. Por Precio (menor a mayor)")
        opcion = input("Elige una opción: ")
        
        mapa_criterios = {"1": "nombre", "2": "stock", "3": "precio"}
        criterio = mapa_criterios.get(opcion, "nombre")
        
        productos = self.inventario.obtener_ordenados(criterio)
        print("\n" + "=" * 85)
        print(f"{'CÓDIGO':<10} {'NOMBRE':<18} {'PRESENT.':<12} {'CATEGORÍA':<15} {'PRECIO':<10} {'STOCK'}")
        print("=" * 85)
        for p in productos:
            print(f"{p.codigo:<10} {p.nombre.capitalize():<18} {p.presentacion.capitalize():<12} {p.categoria.capitalize():<15} Q{p.precio:<9.2f} {p.stock}")
        print("=" * 85)

    def _generar_reporte(self):
        fecha_hoy = datetime.datetime.today().strftime("%Y-%m-%d")
        ventas_hoy = self.repo.obtener_ventas_del_dia(fecha_hoy)
        ReporteVentas.mostrar_reporte_dia(ventas_hoy, fecha_hoy)
        self.bitacora.registrar("Reporte de ventas del día consultado")

    def _salir(self):
        self.repo.guardar_inventario(self.inventario)
        self.bitacora.registrar("Guardado de cambios y salida del sistema")
        print("✅ Cambios guardados. Saliendo del programa...")