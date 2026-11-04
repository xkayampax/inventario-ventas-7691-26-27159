Estudiante: Xavier Emilio Serrano Domingo

Carné: "7691-26-27159"

Curso: Algoritmos - Ciclo 2-2026   

Este proyecto es la refactorización completa del "Proyecto 1" aplicando los principios de la Programación Orientada a Objetos (POO). 

Regla de Negocio Especial: Alerta de Stock Mínimo
Tema de Negocio: Farmacia
La farmacia requiere un control estricto de reabastecimiento. Esta regla se implementó y evalúa dinámicamente si el nivel de existencias de un producto requiere atención inmediata tras una venta.

Instrucciones de Ejecución
1. Asegúrate de tener instalado Python 3.14
2. Descarga los archivos.
3. Abre una terminal en la carpeta raíz del proyecto.
4. Ejecuta el programa con el comando: `python main.py`

Estructura del Proyecto
`main.py`: Punto de entrada que inicializa y arranca el sistema.
`inventario/`
`app.py`: `SistemaInventario` - Orquesta el menú, la lógica y captura excepciones.
`modelos.py`: `Producto` (encapsulado) y `Venta` (dataclass inmutable).
`inventario.py`: `Inventario` - Colección principal con diccionarios y métodos dunder.
`reglas.py`: `ReglaNegocio` y `AlertaStockMinimo` - Implementación de la regla asignada.
`persistencia.py`: `RepositorioCSV` y `Bitacora` - Manejo de archivos en disco.
`reportes.py`: `ReporteVentas` - Lógica de formato y diseño visual de salidas.
`excepciones.py`: Clases personalizadas de errores (ej. `StockInsuficienteError`).
`datos/`: Archivos `.csv` y bitácoras del sistema.
`docs/`: Documentación UML y reflexión académica.

Diagramas UML
Diagrama de Casos de Uso

<img width="1032" height="589" alt="Diagrama Casos de Uso" src="https://github.com/user-attachments/assets/64de7e29-5051-4981-b796-1a739c5435f3" />



Diagrama de Clases

<img width="2409" height="710" alt="Diagrama de clases" src="https://github.com/user-attachments/assets/51747380-f1d4-4eb2-a032-2c7816c7a2ba" />

Ejemplo de Uso

--- MENÚ FARMACIA BENDICIÓN (POO) ---
1. Agregar producto
2. Consultar producto
3. Registrar venta
4. Mostrar inventario
5. Generar reporte
6. Salir y guardar cambios
Selecciona una opción:

[REFLEXIÓN.pdf](https://github.com/user-attachments/files/34399505/REFLEXION.pdf)
