## Semana 16 - Gestión de Usuarios y Manejo de Eventos

En esta evolución del sistema, se incorporó la administración de usuarios estructurada por el atributo `rol`. La principal mejora técnica es la implementación de eventos en Tkinter separando la interfaz de la lógica de persistencia.

### Eventos Implementados
* **`<<TreeviewSelect>>`**: Asociado mediante `bind()` a la tabla de usuarios. Al hacer clic en una fila, recupera el ID, consulta los datos a través de `RestauranteServicio` (evitando extraer datos de la capa visual) y rellena el formulario.
* **`<Return>`**: Atajo de teclado en las entradas de texto que invoca el callback de registro, reutilizando el método del botón `command=` para evitar duplicidad de lógica.
* **`<Escape>`**: Atajo de teclado global que limpia el formulario actual y elimina la selección activa de las tablas.
* **`<<ComboboxSelected>>`**: Detecta cambios dinámicos en el menú desplegable de roles.
* **`command=`**: Mantenido para las interacciones estáticas directas de los botones (Registrar, Actualizar, Eliminar).