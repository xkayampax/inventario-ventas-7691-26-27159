# Programa de gestión de inventario

#Importo modulo de operaciones
import operaciones

#menu de inventario
while True:
    print("--- MENÚ FARMACIA BENDICIÓN ---")
    print("1. Agregar producto")
    print("2. Consultar producto")
    print("3. Registrar venta")
    print("4. Mostrar inventario")
    print("5. Generar reporte")
    print("6. Salir y guardar cambios")
    try:
        opcion = int(input("Selecciona una opción: "))

        #Codigo para manejar opcion 1 del menú, que es agregar un producto al inventario
            
        if opcion == 1:
            print("Ha seleccionado la opción de agregar un producto.")
            operaciones.agregar_producto()


        #Codigo para manejar opcion 2 del menú, que es consultar un producto en el inventario    
        elif opcion == 2:
            print("Ha seleccionado la opción de consultar un producto.")
            operaciones.consultar_producto()


        #Codigo para manejar opcion 3 del menú, que es registrar una venta de un producto en el inventario
        elif opcion == 3:
            print("Ha seleccionado la opción de registrar una venta.")
            operaciones.registrar_venta()


        #Codigo para manejar opcion 4 del menú, que es mostrar el inventario completo
        elif opcion == 4:
            print("Ha seleccionado la opción de mostrar el inventario completo.")
            operaciones.mostrar_inventario()


        #Codigo para manejar opcion 5 del menú, que es generar un reporte de ventas
        elif opcion == 5:
            print("Ha seleccionado la opción de generar un reporte de ventas.")
            operaciones.generar_reporte()


        #Codigo para manejar opcion 6 del menú, que es salir y guardar cambios
        elif opcion == 6:
            print("Ha seleccionado la opción de salir y guardar cambios.")
            operaciones.salir_y_guardar()

        else:
            print("Opción no válida. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")    
        break