#Librería para manejar archivos CSV
import csv

#Libreria para agregar fecha y hora a los reportes
import datetime

#Librearia para saber la existencia de un archivo
import os


#Función para agregar un producto al inventario
def agregar_producto():    
            print("Ingrese los datos del producto:")
            codigo = int(input("Código del producto: "))
            nombre = input("Nombre del producto: ").strip().lower()
        
            nombres_existentes = set()
            if os.path.exists("inventario.csv"):
                with open("inventario.csv", "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for fila in reader:
                        nombres_existentes.add(fila["nombre"].strip().lower())

            if nombre in nombres_existentes:
                print(f"❌ Error: El producto '{nombre}' ya existe en el inventario. No se permiten duplicados.")
                return  
            presentacion = input("Tipo de presentación: ").strip().lower()
            categoria = input("Tipo de categoria: ").strip().lower()
            precio = float(input("Precio del producto: "))
            stock = int(input("Cantidad del producto: "))
        
            if stock >= 1:

                try:
                    with open("inventario.csv", "a", encoding="utf-8") as f:
                        f.write(f"{codigo},{nombre},{presentacion},{categoria},{precio},{stock}\n")
                        print("Producto agregado exitosamente.")
                        registrar_bitacora(f"Producto agregado: {nombre} (Código: {codigo})")
                except FileNotFoundError:
                        print("El archivo no existe. Verifica la ruta.")
                except PermissionError:
                        print("No tienes permisos para abrir este archivo.")
            else:
                        print("Error: La cantidad no puede ser negativa.")


#Funcion para consultar un producto en el inventario
def consultar_producto():
    codigo = int(input("Ingrese el código del producto a consultar: "))
    try:
        with open("inventario.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                if fila["codigo"] == str(codigo):
                    print(f"Producto encontrado: {fila}")
                    return
            print("Producto no encontrado.")
    except FileNotFoundError:
        print("El archivo no existe. Verifica la ruta.")
    except PermissionError:
        print("No tienes permisos para abrir este archivo.")


#Funion para registrar una venta de un producto en el inventario
def registrar_venta():
    codigo = int(input("Ingrese el código del producto a vender: "))
    cantidad = int(input("Ingrese la cantidad a vender: "))
    try:
        with open("inventario.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            productos = list(reader)
            for producto in productos:
                if producto["codigo"] == str(codigo):
                    if int(producto["stock"]) >= cantidad:
                        producto["stock"] = str(int(producto["stock"]) - cantidad)
                        if int(producto["stock"]) < 5:
                            print("""¡Atención! El stock del producto es bajo. Considera reabastecerlo pronto.""")
                        print(f"Venta registrada. Nuevo stock: {producto['stock']}")
                        registrar_bitacora(f"Venta: {cantidad} unidades del código {codigo}")
                        with open("Reporte de ventas.csv", "a", encoding="utf-8") as rv:
                            fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            rv.write(f"{fecha_hora},{codigo},{cantidad}\n")
                    else:
                        print("No hay suficiente stock para realizar la venta.")
                    break
            else:
                print("Producto no encontrado.")
        with open("inventario.csv", "w", encoding="utf-8", newline='') as f:
            fieldnames = ["codigo", "nombre", "presentacion", "categoria", "precio", "stock"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(productos)
    except FileNotFoundError:
        print("El archivo no existe. Verifica la ruta.")
    except PermissionError:
        print("No tienes permisos para abrir este archivo.")

#Funcion para mostrar el inventario completo
def mostrar_inventario():
    try:
        with open("inventario.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            productos = list(reader)

        if not productos:
            print("El inventario está vacío.")
            return

        print("\n¿Cómo deseas ordenar el inventario?")
        print("1. Por Nombre (A - Z)")
        print("2. Por Stock (menor a mayor)")
        print("3. Por Precio (menor a mayor)")
        criterio = input("Elige una opción de orden: ").strip()

        if criterio == "1":
            # Criterio 1: Nombre alfabético
            productos_ordenados = sorted(productos, key=lambda x: x["nombre"].lower())
        elif criterio == "2":
            # Criterio 2: Stock numérico
            productos_ordenados = sorted(productos, key=lambda x: int(x["stock"]))
        elif criterio == "3":
            # Criterio 3: Precio numérico
            productos_ordenados = sorted(productos, key=lambda x: float(x["precio"]))
        else:
            print("Opción no válida, mostrando en orden original.")
            productos_ordenados = productos

        print("\n" + "=" * 75)
        print(f"{'CÓDIGO':<10} {'NOMBRE':<18} {'CATEGORÍA':<24} {'PRECIO':<12} {'STOCK'}")
        print("=" * 75)
        for p in productos_ordenados:
            print(f"{p['codigo']:<10} {p['nombre'].capitalize():<18} {p['categoria'].capitalize():<24} Q{float(p['precio']):<12f} {p['stock']}")
        print("=" * 75)

    except FileNotFoundError:
        print("El archivo de inventario aún no existe.")


#Funcion para generar un reporte del inventario
def generar_reporte():
    try:
        with open("Reporte de ventas.csv", "r", encoding="utf-8") as f:
            fecha = datetime.datetime.today().strftime("%Y-%m-%d")
            reader = csv.reader(f)
            print("Reporte de ventas del día ")
            print("-" * 54)
            print(f"{'Fecha y Hora':<24}{'Código del Producto':<22}{'Cantidad':>8}")
            print("-" * 54)
            for linea in reader:
                if len(linea)>=3 and linea[0].startswith(fecha):
                        print(f"{linea[0]:<30}{linea[1]:<22}{linea[2]:>8}")
                        registrar_bitacora("Reporte de ventas del día consultado")
    except FileNotFoundError:
        print("El archivo no existe. Verifica la ruta.")
    except PermissionError:
        print("No tienes permisos para abrir este archivo.")




def registrar_bitacora(mensaje):
    existe = os.path.exists("bitacora.txt")
    with open("bitacora.txt", "a", encoding="utf-8") as b:
        if not existe:
            b.write("Bitácora:\n")
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        b.write(f"{fecha_hora} - {mensaje}\n")

# Función para salir del programa y guardar los cambios
def salir_y_guardar():
    print("Saliendo del programa...")
    registrar_bitacora("Guardado de cambios y salida del sistema")
        