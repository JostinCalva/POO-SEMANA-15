import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

from modelos.producto import Producto


class MainView:

    def __init__(self, root, restaurante_servicio, cerrar_sesion):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.cerrar_sesion = cerrar_sesion

        # ============================================================
        # RUTA DE ASSETS
        # ============================================================
        self.ruta_assets = (
            Path(__file__).resolve().parent.parent / "assets"
        )

        # ============================================================
        # CARGAR IMÁGENES
        # ============================================================
        self.cargar_imagenes()

        # ============================================================
        # CONTENEDOR PRINCIPAL
        # ============================================================
        self.frame = ttk.Frame(root, padding=15)
        self.frame.pack(fill="both", expand=True)

        self.crear_interfaz()
        self.actualizar_todo()

    # ================================================================
    # CARGAR IMÁGENES
    # ================================================================
    def cargar_imagenes(self):

        try:
            self.logo_image = tk.PhotoImage(
                file=str(self.ruta_assets / "logo.png")
            )

            self.usuarios_image = tk.PhotoImage(
                file=str(self.ruta_assets / "usuarios.png")
            )

            self.productos_image = tk.PhotoImage(
                file=str(self.ruta_assets / "productos.png")
            )

            self.ventas_image = tk.PhotoImage(
                file=str(self.ruta_assets / "ventas.png")
            )

            # Reducimos los iconos para que no ocupen demasiado espacio
            self.usuarios_image = self.usuarios_image.subsample(4, 4)
            self.productos_image = self.productos_image.subsample(4, 4)
            self.ventas_image = self.ventas_image.subsample(4, 4)

        except Exception as e:
            print("Advertencia: no se pudieron cargar los assets.")
            print(e)

            self.logo_image = None
            self.usuarios_image = None
            self.productos_image = None
            self.ventas_image = None

    # ================================================================
    # INTERFAZ PRINCIPAL
    # ================================================================
    def crear_interfaz(self):

        # ------------------------------------------------------------
        # ENCABEZADO
        # ------------------------------------------------------------
        encabezado = ttk.Frame(self.frame)
        encabezado.pack(fill="x", pady=(0, 15))

        # Logo
        if self.logo_image:
            lbl_logo = ttk.Label(
                encabezado,
                image=self.logo_image
            )
            lbl_logo.pack(side="left")

        # Botón cerrar sesión
        boton_cerrar = ttk.Button(
            encabezado,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        )
        boton_cerrar.pack(side="right", padx=5)

        # ------------------------------------------------------------
        # RESUMEN
        # ------------------------------------------------------------
        resumen = ttk.LabelFrame(
            self.frame,
            text="Resumen del sistema",
            padding=10
        )
        resumen.pack(fill="x", pady=(0, 15))

        self.label_usuarios = ttk.Label(
            resumen,
            text="Usuarios: 0",
            font=("Arial", 11, "bold")
        )
        self.label_usuarios.pack(side="left", padx=20)

        self.label_productos = ttk.Label(
            resumen,
            text="Productos: 0",
            font=("Arial", 11, "bold")
        )
        self.label_productos.pack(side="left", padx=20)

        self.label_ventas = ttk.Label(
            resumen,
            text="Ventas: 0",
            font=("Arial", 11, "bold")
        )
        self.label_ventas.pack(side="left", padx=20)

        # ------------------------------------------------------------
        # NOTEBOOK
        # ------------------------------------------------------------
        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(fill="both", expand=True)

        # Crear pestañas
        self.crear_tab_usuarios()
        self.crear_tab_productos()
        self.crear_tab_ventas()

    # ================================================================
    # TAB USUARIOS
    # ================================================================
    def crear_tab_usuarios(self):

        self.tab_usuarios = ttk.Frame(
            self.notebook,
            padding=15
        )

        self.notebook.add(
            self.tab_usuarios,
            text=" Usuarios",
            image=self.usuarios_image,
            compound="left"
        )

        titulo = ttk.Label(
            self.tab_usuarios,
            text="Consulta de usuarios",
            font=("Arial", 15, "bold")
        )
        titulo.pack(anchor="w", pady=(0, 10))

        self.tree_usuarios = ttk.Treeview(
            self.tab_usuarios,
            columns=(
                "identificacion",
                "nombre",
                "usuario"
            ),
            show="headings"
        )

        self.tree_usuarios.heading(
            "identificacion",
            text="Identificación"
        )

        self.tree_usuarios.heading(
            "nombre",
            text="Nombre"
        )

        self.tree_usuarios.heading(
            "usuario",
            text="Usuario"
        )

        self.tree_usuarios.column(
            "identificacion",
            width=150
        )

        self.tree_usuarios.column(
            "nombre",
            width=250
        )

        self.tree_usuarios.column(
            "usuario",
            width=150
        )

        self.tree_usuarios.pack(
            fill="both",
            expand=True
        )

    # ================================================================
    # TAB PRODUCTOS
    # ================================================================
    def crear_tab_productos(self):

        self.tab_productos = ttk.Frame(
            self.notebook,
            padding=15
        )

        self.notebook.add(
            self.tab_productos,
            text=" Productos",
            image=self.productos_image,
            compound="left"
        )

        titulo = ttk.Label(
            self.tab_productos,
            text="Gestión de productos",
            font=("Arial", 15, "bold")
        )
        titulo.pack(anchor="w", pady=(0, 10))

        # ------------------------------------------------------------
        # FORMULARIO
        # ------------------------------------------------------------
        formulario = ttk.LabelFrame(
            self.tab_productos,
            text="Datos del producto",
            padding=10
        )
        formulario.pack(
            fill="x",
            pady=(0, 10)
        )

        ttk.Label(
            formulario,
            text="Código:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_codigo = ttk.Entry(
            formulario,
            width=25
        )
        self.entrada_codigo.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_nombre = ttk.Entry(
            formulario,
            width=25
        )
        self.entrada_nombre.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_precio = ttk.Entry(
            formulario,
            width=25
        )
        self.entrada_precio.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Stock:"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.entrada_stock = ttk.Entry(
            formulario,
            width=25
        )
        self.entrada_stock.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        # ------------------------------------------------------------
        # BOTONES PRODUCTOS
        # ------------------------------------------------------------
        botones = ttk.Frame(
            self.tab_productos
        )
        botones.pack(
            fill="x",
            pady=(0, 10)
        )

        ttk.Button(
            botones,
            text="Registrar",
            command=self.registrar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            botones,
            text="Actualizar",
            command=self.actualizar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            botones,
            text="Eliminar",
            command=self.eliminar_producto
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_formulario
        ).pack(
            side="left",
            padx=5
        )

        # ------------------------------------------------------------
        # TABLA PRODUCTOS
        # ------------------------------------------------------------
        self.tree_productos = ttk.Treeview(
            self.tab_productos,
            columns=(
                "codigo",
                "nombre",
                "precio",
                "stock"
            ),
            show="headings"
        )

        self.tree_productos.heading(
            "codigo",
            text="Código"
        )

        self.tree_productos.heading(
            "nombre",
            text="Nombre"
        )

        self.tree_productos.heading(
            "precio",
            text="Precio"
        )

        self.tree_productos.heading(
            "stock",
            text="Stock"
        )

        self.tree_productos.column(
            "codigo",
            width=120
        )

        self.tree_productos.column(
            "nombre",
            width=250
        )

        self.tree_productos.column(
            "precio",
            width=120
        )

        self.tree_productos.column(
            "stock",
            width=100
        )

        self.tree_productos.pack(
            fill="both",
            expand=True
        )

        self.tree_productos.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_producto
        )

    # ================================================================
    # TAB VENTAS
    # ================================================================
    def crear_tab_ventas(self):

        self.tab_ventas = ttk.Frame(
            self.notebook,
            padding=15
        )

        self.notebook.add(
            self.tab_ventas,
            text=" Ventas",
            image=self.ventas_image,
            compound="left"
        )

        titulo = ttk.Label(
            self.tab_ventas,
            text="Registro de ventas",
            font=("Arial", 15, "bold")
        )
        titulo.pack(
            anchor="w",
            pady=(0, 10)
        )

        # ------------------------------------------------------------
        # FORMULARIO DE VENTA
        # ------------------------------------------------------------
        formulario = ttk.LabelFrame(
            self.tab_ventas,
            text="Nueva venta",
            padding=15
        )
        formulario.pack(
            fill="x",
            pady=(0, 15)
        )

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.combo_usuario = ttk.Combobox(
            formulario,
            state="readonly",
            width=35
        )
        self.combo_usuario.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        ttk.Label(
            formulario,
            text="Producto:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.combo_producto = ttk.Combobox(
            formulario,
            state="readonly",
            width=35
        )
        self.combo_producto.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # ============================================================
        # BOTÓN PRINCIPAL DE VENTA
        # ============================================================
        ttk.Button(
            formulario,
            text="Registrar venta",
            command=self.registrar_venta
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=10
        )

        # ------------------------------------------------------------
        # TABLA DE VENTAS
        # ------------------------------------------------------------
        ttk.Label(
            self.tab_ventas,
            text="Ventas registradas",
            font=("Arial", 12, "bold")
        ).pack(
            anchor="w",
            pady=(0, 5)
        )

        self.tree_ventas = ttk.Treeview(
            self.tab_ventas,
            columns=(
                "usuario",
                "producto",
                "fecha"
            ),
            show="headings"
        )

        self.tree_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tree_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tree_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tree_ventas.column(
            "usuario",
            width=180
        )

        self.tree_ventas.column(
            "producto",
            width=180
        )

        self.tree_ventas.column(
            "fecha",
            width=180
        )

        self.tree_ventas.pack(
            fill="both",
            expand=True
        )

    # ================================================================
    # PRODUCTOS
    # ================================================================
    def registrar_producto(self):

        try:
            codigo = self.entrada_codigo.get().strip()
            nombre = self.entrada_nombre.get().strip()
            precio = float(self.entrada_precio.get())
            stock = int(self.entrada_stock.get())

            producto = Producto(
                codigo=codigo,
                nombre=nombre,
                precio=precio,
                stock=stock
            )

            correcto, mensaje = (
                self.restaurante_servicio.registrar_producto(producto)
            )

            if correcto:
                messagebox.showinfo(
                    "Éxito",
                    mensaje
                )

                self.limpiar_formulario()
                self.actualizar_todo()

            else:
                messagebox.showerror(
                    "Error",
                    mensaje
                )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Precio y stock deben contener valores válidos."
            )

    def actualizar_producto(self):

        seleccion = self.tree_productos.selection()

        if not seleccion:
            messagebox.showwarning(
                "Advertencia",
                "Seleccione un producto."
            )
            return

        try:
            codigo = self.entrada_codigo.get().strip()
            nombre = self.entrada_nombre.get().strip()
            precio = float(self.entrada_precio.get())
            stock = int(self.entrada_stock.get())

            producto = Producto(
                codigo=codigo,
                nombre=nombre,
                precio=precio,
                stock=stock
            )

            correcto, mensaje = (
                self.restaurante_servicio.actualizar_producto(producto)
            )

            if correcto:
                messagebox.showinfo(
                    "Éxito",
                    mensaje
                )

                self.limpiar_formulario()
                self.actualizar_todo()

            else:
                messagebox.showerror(
                    "Error",
                    mensaje
                )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Precio y stock deben contener valores válidos."
            )

    def eliminar_producto(self):

        seleccion = self.tree_productos.selection()

        if not seleccion:
            messagebox.showwarning(
                "Advertencia",
                "Seleccione un producto."
            )
            return

        valores = self.tree_productos.item(
            seleccion[0],
            "values"
        )

        codigo = valores[0]

        confirmar = messagebox.askyesno(
            "Confirmar",
            "¿Desea eliminar este producto?"
        )

        if not confirmar:
            return

        correcto, mensaje = (
            self.restaurante_servicio.eliminar_producto(codigo)
        )

        if correcto:
            messagebox.showinfo(
                "Éxito",
                mensaje
            )

            self.limpiar_formulario()
            self.actualizar_todo()

        else:
            messagebox.showerror(
                "Error",
                mensaje
            )

    def seleccionar_producto(self, event=None):

        seleccion = self.tree_productos.selection()

        if not seleccion:
            return

        valores = self.tree_productos.item(
            seleccion[0],
            "values"
        )

        self.entrada_codigo.delete(0, tk.END)
        self.entrada_codigo.insert(0, valores[0])

        self.entrada_nombre.delete(0, tk.END)
        self.entrada_nombre.insert(0, valores[1])

        self.entrada_precio.delete(0, tk.END)
        self.entrada_precio.insert(0, valores[2])

        self.entrada_stock.delete(0, tk.END)
        self.entrada_stock.insert(0, valores[3])

    def limpiar_formulario(self):

        self.entrada_codigo.delete(0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_precio.delete(0, tk.END)
        self.entrada_stock.delete(0, tk.END)

    # ================================================================
    # VENTAS
    # ================================================================
    def registrar_venta(self):

        usuario_seleccionado = self.combo_usuario.get()
        producto_seleccionado = self.combo_producto.get()

        if not usuario_seleccionado:
            messagebox.showwarning(
                "Advertencia",
                "Seleccione un usuario."
            )
            return

        if not producto_seleccionado:
            messagebox.showwarning(
                "Advertencia",
                "Seleccione un producto."
            )
            return

        identificacion_usuario = (
            usuario_seleccionado.split(" - ")[0]
        )

        codigo_producto = (
            producto_seleccionado.split(" - ")[0]
        )

        # Delegamos la lógica al servicio
        correcto, mensaje = (
            self.restaurante_servicio.registrar_venta(
                identificacion_usuario,
                codigo_producto
            )
        )

        if correcto:

            messagebox.showinfo(
                "Venta registrada",
                mensaje
            )

            self.actualizar_todo()

        else:

            messagebox.showerror(
                "Error",
                mensaje
            )

    # ================================================================
    # ACTUALIZAR TODO
    # ================================================================
    def actualizar_todo(self):

        self.actualizar_resumen()
        self.actualizar_usuarios()
        self.actualizar_productos()
        self.actualizar_combos()
        self.actualizar_ventas()

    # ================================================================
    # RESUMEN
    # ================================================================
    def actualizar_resumen(self):

        self.label_usuarios.config(
            text=(
                f"Usuarios: "
                f"{self.restaurante_servicio.cantidad_usuarios()}"
            )
        )

        self.label_productos.config(
            text=(
                f"Productos: "
                f"{self.restaurante_servicio.cantidad_productos()}"
            )
        )

        self.label_ventas.config(
            text=(
                f"Ventas: "
                f"{len(self.restaurante_servicio.obtener_ventas())}"
            )
        )

    # ================================================================
    # ACTUALIZAR USUARIOS
    # ================================================================
    def actualizar_usuarios(self):

        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)

        for usuario in self.restaurante_servicio.usuarios:

            self.tree_usuarios.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.usuario
                )
            )

    # ================================================================
    # ACTUALIZAR PRODUCTOS
    # ================================================================
    def actualizar_productos(self):

        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)

        for producto in self.restaurante_servicio.productos:

            self.tree_productos.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    f"{producto.precio:.2f}",
                    producto.stock
                )
            )

    # ================================================================
    # ACTUALIZAR COMBOS
    # ================================================================
    def actualizar_combos(self):

        usuarios = []

        for usuario in self.restaurante_servicio.usuarios:
            usuarios.append(
                f"{usuario.identificacion} - {usuario.nombre}"
            )

        productos = []

        for producto in self.restaurante_servicio.productos:

            if producto.stock > 0:
                productos.append(
                    f"{producto.codigo} - {producto.nombre}"
                )

        self.combo_usuario["values"] = usuarios
        self.combo_producto["values"] = productos

        if usuarios:
            self.combo_usuario.current(0)
        else:
            self.combo_usuario.set("")

        if productos:
            self.combo_producto.current(0)
        else:
            self.combo_producto.set("")

    # ================================================================
    # ACTUALIZAR VENTAS
    # ================================================================
    def actualizar_ventas(self):

        for item in self.tree_ventas.get_children():
            self.tree_ventas.delete(item)

        ventas = self.restaurante_servicio.obtener_ventas()

        for venta in ventas:

            self.tree_ventas.insert(
                "",
                "end",
                values=(
                    venta.usuario,
                    venta.producto,
                    venta.fecha
                )
            )

    # ================================================================
    # DESTRUIR VISTA
    # ================================================================
    def destruir(self):

        self.frame.destroy()