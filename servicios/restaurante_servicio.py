from datetime import datetime

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class RestauranteServicio:

    def __init__(
        self,
        archivo_servicio,
        archivo_productos="datos/productos.json",
        archivo_usuarios="datos/usuarios.json",
        archivo_ventas="datos/ventas.json"
    ):
        self.archivo_servicio = archivo_servicio

        self.archivo_productos = archivo_productos
        self.archivo_usuarios = archivo_usuarios
        self.archivo_ventas = archivo_ventas

        self.productos = []
        self.usuarios = []
        self.ventas = []

        self.cargar_productos()
        self.cargar_usuarios()
        self.cargar_ventas()

    # ==========================================
    # PRODUCTOS
    # ==========================================

    def cargar_productos(self):
        datos = self.archivo_servicio.leer_json(
            self.archivo_productos
        )

        self.productos = [
            Producto.from_dict(producto)
            for producto in datos
        ]

    def guardar_productos(self):
        datos = [
            producto.to_dict()
            for producto in self.productos
        ]

        self.archivo_servicio.guardar_json(
            self.archivo_productos,
            datos
        )

    def cantidad_productos(self):
        return len(self.productos)

    def registrar_producto(self, producto):
        if not producto.codigo:
            return False, "El código es obligatorio."

        if not producto.nombre:
            return False, "El nombre es obligatorio."

        if producto.precio < 0:
            return False, "El precio no puede ser negativo."

        if producto.stock < 0:
            return False, "El stock no puede ser negativo."

        if self.buscar_producto(producto.codigo):
            return False, "Ya existe un producto con ese código."

        self.productos.append(producto)
        self.guardar_productos()

        return True, "Producto registrado correctamente."

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(self, producto):
        existente = self.buscar_producto(producto.codigo)

        if existente is None:
            return False, "El producto no existe."

        existente.nombre = producto.nombre
        existente.precio = producto.precio
        existente.stock = producto.stock

        self.guardar_productos()

        return True, "Producto actualizado correctamente."

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "El producto no existe."

        self.productos.remove(producto)
        self.guardar_productos()

        return True, "Producto eliminado correctamente."

    # ==========================================
    # USUARIOS
    # ==========================================

    def cargar_usuarios(self):
        datos = self.archivo_servicio.leer_json(
            self.archivo_usuarios
        )

        self.usuarios = [
            Usuario.from_dict(usuario)
            for usuario in datos
        ]

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def validar_acceso(self, usuario, password):
        usuario = str(usuario).strip()
        password = str(password).strip()

        for usuario_actual in self.usuarios:

            usuario_guardado = str(
                usuario_actual.usuario
            ).strip()

            password_guardado = str(
                usuario_actual.password
            ).strip()

            if (
                usuario_guardado == usuario
                and password_guardado == password
            ):
                return True, usuario_actual

        return False, None

    # ==========================================
    # VENTAS
    # ==========================================

    def cargar_ventas(self):
        datos = self.archivo_servicio.leer_json(
            self.archivo_ventas
        )

        self.ventas = [
            Venta.from_dict(venta)
            for venta in datos
        ]

    def guardar_ventas(self):
        datos = [
            venta.to_dict()
            for venta in self.ventas
        ]

        self.archivo_servicio.guardar_json(
            self.archivo_ventas,
            datos
        )

    def obtener_ventas(self):
        return self.ventas

    def registrar_venta(self, identificacion_usuario, codigo_producto):

        if not identificacion_usuario:
            return False, "Debe seleccionar un usuario."

        if not codigo_producto:
            return False, "Debe seleccionar un producto."

        usuario_encontrado = None

        for usuario in self.usuarios:

            if usuario.identificacion == identificacion_usuario:
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            return False, "El usuario seleccionado no existe."

        producto_encontrado = self.buscar_producto(
            codigo_producto
        )

        if producto_encontrado is None:
            return False, "El producto seleccionado no existe."

        if producto_encontrado.stock <= 0:
            return False, "El producto seleccionado no tiene stock."

        fecha_actual = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        nueva_venta = Venta(
            usuario=usuario_encontrado.identificacion,
            producto=producto_encontrado.codigo,
            fecha=fecha_actual
        )

        self.ventas.append(nueva_venta)

        producto_encontrado.stock -= 1

        self.guardar_productos()
        self.guardar_ventas()

        return True, "Venta registrada correctamente."