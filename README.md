# Restaurante App - Semana 15

# Jostin Anthony Calva Salinas

## Programación Orientada a Objetos

Aplicación de escritorio desarrollada en Python utilizando Tkinter y una arquitectura modular.

La Semana 15 corresponde a la evolución del proyecto restaurante_app desarrollado durante las semanas anteriores.

## Funcionalidades

- Inicio de sesión de usuarios.
- Consulta de usuarios.
- Consulta de productos.
- Registro de ventas.
- Selección de usuario y producto mediante componentes ttk.
- Persistencia de información mediante archivos JSON.
- Visualización de ventas mediante Treeview.
- Actualización automática de la interfaz después de registrar una venta.
- Uso de callbacks mediante `command=`.
- Separación entre interfaz, servicios, modelos y datos.

## Arquitectura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── login_view.py
│   └── main_view.py
│
├── assets/
│   ├── logo.png
│   ├── usuarios.png
│   ├── productos.png
│   └── ventas.png
│
├── main.py
└── README.md