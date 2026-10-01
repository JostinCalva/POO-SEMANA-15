import tkinter as tk
from tkinter import ttk, messagebox
from modelos.usuario import Usuario
from modelos.producto import Producto

class MainView:
    def __init__(self, root, servicio, usuario_actual, callback_cerrar_sesion):
        self.root = root
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.callback_cerrar_sesion = callback_cerrar_sesion
        
        self._crear_interfaz()

    def _crear_interfaz(self):
        # --- CABECERA DE USUARIO ---
        frame_header = tk.Frame(self.root, bg="#333333", pady=10)
        frame_header.pack(fill='x')
        
        lbl_bienvenida = tk.Label(frame_header, text=f"Bienvenido: {self.usuario_actual.nombre} | Rol: {self.usuario_actual.rol}", fg="white", bg="#333333", font=("Arial", 12, "bold"))
        lbl_bienvenida.pack(side='left', padx=20)
        
        btn_salir = tk.Button(frame_header, text="Cerrar Sesión", command=self.callback_cerrar_sesion, bg="#ff4c4c", fg="white")
        btn_salir.pack(side='right', padx=20)

        # --- PESTAÑAS ---
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Pestaña de Productos (Funcional)
        self._crear_pestana_productos()

        # --- PESTAÑA USUARIOS (Solo Administrador) ---
        if self.usuario_actual.rol == "Administrador":
            self._crear_pestana_usuarios()

        self.root.bind('<Escape>', self._on_escape)

    def _crear_pestana_productos(self):
        self.tab_productos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_productos, text="Gestión de Productos")

        frame_form = ttk.LabelFrame(self.tab_productos, text="Datos del Producto")
        frame_form.pack(padx=10, pady=10, fill='x')

        ttk.Label(frame_form, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_id_prod = ttk.Entry(frame_form)
        self.entry_id_prod.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_nombre_prod = ttk.Entry(frame_form)
        self.entry_nombre_prod.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="Precio ($):").grid(row=1, column=0, padx=5, pady=5)
        self.entry_precio = ttk.Entry(frame_form)
        self.entry_precio.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Stock:").grid(row=1, column=2, padx=5, pady=5)
        self.entry_stock = ttk.Entry(frame_form)
        self.entry_stock.grid(row=1, column=3, padx=5, pady=5)

        # BOTONES PRODUCTOS
        frame_btn = ttk.Frame(self.tab_productos)
        frame_btn.pack(pady=5)
        
        ttk.Button(frame_btn, text="Registrar", command=self._registrar_producto_cmd).grid(row=0, column=0, padx=5)
        ttk.Button(frame_btn, text="Actualizar", command=self._actualizar_producto_cmd).grid(row=0, column=1, padx=5)
        ttk.Button(frame_btn, text="Eliminar", command=self._eliminar_producto_cmd).grid(row=0, column=2, padx=5)
        ttk.Button(frame_btn, text="Limpiar", command=self._limpiar_formulario_productos).grid(row=0, column=3, padx=5)

        # TABLA PRODUCTOS
        self.tree_productos = ttk.Treeview(self.tab_productos, columns=("ID", "Nombre", "Precio", "Stock"), show='headings')
        self.tree_productos.heading("ID", text="ID")
        self.tree_productos.heading("Nombre", text="Nombre")
        self.tree_productos.heading("Precio", text="Precio ($)")
        self.tree_productos.heading("Stock", text="Stock")
        self.tree_productos.pack(padx=10, pady=10, fill='both', expand=True)

        self.tree_productos.bind('<<TreeviewSelect>>', self._on_producto_seleccionado)
        self._cargar_tabla_productos()

    def _crear_pestana_usuarios(self):
        self.tab_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_usuarios, text="Gestión de Usuarios")

        frame_form = ttk.LabelFrame(self.tab_usuarios, text="Datos del Usuario")
        frame_form.pack(padx=10, pady=10, fill='x')

        ttk.Label(frame_form, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_id_usuario = ttk.Entry(frame_form)
        self.entry_id_usuario.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_nombre = ttk.Entry(frame_form)
        self.entry_nombre.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="Username:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_username = ttk.Entry(frame_form)
        self.entry_username.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Rol:").grid(row=1, column=2, padx=5, pady=5)
        self.combo_rol = ttk.Combobox(frame_form, values=["Administrador", "Empleado", "Cliente"], state="readonly")
        self.combo_rol.grid(row=1, column=3, padx=5, pady=5)

        frame_btn = ttk.Frame(self.tab_usuarios)
        frame_btn.pack(pady=5)
        
        ttk.Button(frame_btn, text="Registrar", command=self._registrar_usuario_cmd).grid(row=0, column=0, padx=5)
        ttk.Button(frame_btn, text="Actualizar", command=self._actualizar_usuario_cmd).grid(row=0, column=1, padx=5)
        ttk.Button(frame_btn, text="Eliminar", command=self._eliminar_usuario_cmd).grid(row=0, column=2, padx=5)
        ttk.Button(frame_btn, text="Limpiar", command=self._limpiar_formulario_usuarios).grid(row=0, column=3, padx=5)

        self.tree_usuarios = ttk.Treeview(self.tab_usuarios, columns=("ID", "Nombre", "Usuario", "Rol"), show='headings')
        self.tree_usuarios.heading("ID", text="ID")
        self.tree_usuarios.heading("Nombre", text="Nombre")
        self.tree_usuarios.heading("Usuario", text="Usuario")
        self.tree_usuarios.heading("Rol", text="Rol")
        self.tree_usuarios.pack(padx=10, pady=10, fill='both', expand=True)

        self.tree_usuarios.bind('<<TreeviewSelect>>', self._on_usuario_seleccionado)
        self._cargar_tabla_usuarios()

    # ================= EVENTOS PRODUCTOS =================
    def _on_producto_seleccionado(self, event):
        seleccion = self.tree_productos.selection()
        if seleccion:
            item = self.tree_productos.item(seleccion[0])
            id_prod = item['values'][0]
            producto = self.servicio.obtener_producto_por_id(str(id_prod))
            if producto:
                self._limpiar_formulario_productos()
                self.entry_id_prod.insert(0, producto.id_producto)
                self.entry_id_prod.config(state='readonly')
                self.entry_nombre_prod.insert(0, producto.nombre)
                self.entry_precio.insert(0, producto.precio)
                self.entry_stock.insert(0, producto.stock)

    def _registrar_producto_cmd(self):
        try:
            nuevo_prod = Producto(
                id_producto=self.entry_id_prod.get(),
                nombre=self.entry_nombre_prod.get(),
                precio=float(self.entry_precio.get()),
                stock=int(self.entry_stock.get())
            )
            self.servicio.registrar_producto(nuevo_prod)
            self._cargar_tabla_productos()
            self._limpiar_formulario_productos()
            messagebox.showinfo("Éxito", "Producto registrado correctamente.")
        except ValueError as e:
            messagebox.showerror("Error de formato", "Verifique que el precio sea numérico y el stock un número entero.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _actualizar_producto_cmd(self):
        try:
            prod = Producto(
                id_producto=self.entry_id_prod.get(),
                nombre=self.entry_nombre_prod.get(),
                precio=float(self.entry_precio.get()),
                stock=int(self.entry_stock.get())
            )
            self.servicio.actualizar_producto(prod)
            self._cargar_tabla_productos()
            self._limpiar_formulario_productos()
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _eliminar_producto_cmd(self):
        id_prod = self.entry_id_prod.get()
        if not id_prod:
            messagebox.showwarning("Atención", "Seleccione un producto de la tabla.")
            return

        if messagebox.askyesno("Confirmar", f"¿Desea eliminar el producto {id_prod}?"):
            try:
                self.servicio.eliminar_producto(id_prod)
                self._cargar_tabla_productos()
                self._limpiar_formulario_productos()
                messagebox.showinfo("Éxito", "Producto eliminado.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def _cargar_tabla_productos(self):
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        productos = self.servicio.obtener_productos()
        for p in productos:
            self.tree_productos.insert("", "end", values=(p.id_producto, p.nombre, f"${p.precio:.2f}", p.stock))

    def _limpiar_formulario_productos(self):
        self.entry_id_prod.config(state='normal')
        self.entry_id_prod.delete(0, tk.END)
        self.entry_nombre_prod.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)

    # ================= EVENTOS USUARIOS =================
    def _on_usuario_seleccionado(self, event):
        seleccion = self.tree_usuarios.selection()
        if seleccion:
            item = self.tree_usuarios.item(seleccion[0])
            id_usuario = item['values'][0]
            usuario = self.servicio.obtener_usuario_por_id(str(id_usuario))
            if usuario:
                self._limpiar_formulario_usuarios()
                self.entry_id_usuario.insert(0, usuario.id_usuario)
                self.entry_id_usuario.config(state='readonly')
                self.entry_nombre.insert(0, usuario.nombre)
                self.entry_username.insert(0, usuario.username)
                self.combo_rol.set(usuario.rol)

    def _registrar_usuario_cmd(self):
        try:
            nuevo_usuario = Usuario(
                id_usuario=self.entry_id_usuario.get(),
                nombre=self.entry_nombre.get(),
                username=self.entry_username.get(),
                password="123",
                rol=self.combo_rol.get()
            )
            self.servicio.registrar_usuario(nuevo_usuario)
            self._cargar_tabla_usuarios()
            self._limpiar_formulario_usuarios()
            messagebox.showinfo("Éxito", "Usuario registrado.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _actualizar_usuario_cmd(self):
        try:
            usuario = Usuario(
                id_usuario=self.entry_id_usuario.get(),
                nombre=self.entry_nombre.get(),
                username=self.entry_username.get(),
                password="123",
                rol=self.combo_rol.get()
            )
            self.servicio.actualizar_usuario(usuario)
            self._cargar_tabla_usuarios()
            self._limpiar_formulario_usuarios()
            messagebox.showinfo("Éxito", "Usuario actualizado.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _eliminar_usuario_cmd(self):
        id_usuario = self.entry_id_usuario.get()
        if not id_usuario:
            messagebox.showwarning("Atención", "Seleccione un usuario.")
            return

        if messagebox.askyesno("Confirmar", f"¿Eliminar a {id_usuario}?"):
            try:
                self.servicio.eliminar_usuario(id_usuario, self.usuario_actual.id_usuario)
                self._cargar_tabla_usuarios()
                self._limpiar_formulario_usuarios()
                messagebox.showinfo("Éxito", "Usuario eliminado.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def _cargar_tabla_usuarios(self):
        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)
        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            self.tree_usuarios.insert("", "end", values=(u.id_usuario, u.nombre, u.username, u.rol))

    def _limpiar_formulario_usuarios(self):
        self.entry_id_usuario.config(state='normal')
        self.entry_id_usuario.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_username.delete(0, tk.END)
        self.combo_rol.set('')

    def _on_escape(self, event):
        self._limpiar_formulario_productos()
        self._limpiar_formulario_usuarios()