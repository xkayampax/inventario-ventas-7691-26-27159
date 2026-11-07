class ReporteVentas:
    
    @staticmethod
    def mostrar_reporte_dia(ventas, fecha):
        print(f"\nReporte de ventas del día ({fecha})")
        print("-" * 54)
        print(f"{'Fecha y Hora':<24}{'Código del Producto':<22}{'Cantidad':>8}")
        print("-" * 54)
        if not ventas:
            print("No hay ventas registradas para hoy.")
        else:
            for v in ventas:
                print(f"{v.fecha_hora:<24}{v.codigo_producto:<22}{v.cantidad:>8}")
        print("-" * 54)