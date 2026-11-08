import csv
import os
import datetime
from .modelos import Producto, Venta

class RepositorioCSV:
    def __init__(self, ruta_inventario, ruta_ventas="datos/Reporte de ventas.csv"):
        self.ruta_inventario = ruta_inventario
        self.ruta_ventas = ruta_ventas

    def cargar_inventario(self, inventario):
        if not os.path.exists(self.ruta_inventario):
            return 
        with open(self.ruta_inventario, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                prod = Producto(
                    codigo=fila["codigo"],
                    nombre=fila["nombre"],
                    presentacion=fila["presentacion"],
                    categoria=fila["categoria"],
                    precio=float(fila["precio"]),
                    stock=int(fila["stock"])
                )
                inventario.agregar(prod)

    def guardar_inventario(self, inventario):
        with open(self.ruta_inventario, "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["codigo", "nombre", "presentacion", "categoria", "precio", "stock"])
            for p in inventario:
                writer.writerow([p.codigo, p.nombre, p.presentacion, p.categoria, p.precio, p.stock])

    def registrar_venta(self, venta: Venta):
        existe = os.path.exists(self.ruta_ventas)
        with open(self.ruta_ventas, "a", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            if not existe:
                writer.writerow(["fecha_hora", "codigo_producto", "cantidad"])
            writer.writerow([venta.fecha_hora, venta.codigo_producto, venta.cantidad])

    def obtener_ventas_del_dia(self, fecha_str):
        ventas = []
        if not os.path.exists(self.ruta_ventas):
            return ventas
        with open(self.ruta_ventas, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                if fila["fecha_hora"].startswith(fecha_str):
                    ventas.append(Venta(fila["fecha_hora"], fila["codigo_producto"], int(fila["cantidad"])))
        return ventas


class Bitacora:
    def __init__(self, ruta="datos/bitacora.txt"):
        self.ruta = ruta

    def registrar(self, mensaje):
        existe = os.path.exists(self.ruta)
        with open(self.ruta, "a", encoding="utf-8") as b:
            if not existe:
                b.write("Bitácora:\n")
            fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            b.write(f"{fecha_hora} - {mensaje}\n")
