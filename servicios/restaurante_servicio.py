from modelos.usuario import Usuario
from modelos.producto import Producto

class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio

    # --- AUTENTICACIÓN ---
    def validar_acceso(self, username, password):
        usuarios = self.obtener_usuarios()
        for usuario in usuarios:
            if usuario.username == username and usuario.password == password:
                return True, usuario 
        return False, None 

    # --- CRUD USUARIOS ---
    def obtener_usuarios(self):
        datos = self.archivo_servicio.leer_archivo("datos/usuarios.json")
        if not datos:
            return []
        return [Usuario.from_dict(d) for d in datos]

    def obtener_usuario_por_id(self, id_usuario):
        usuarios = self.obtener_usuarios()
        for u in usuarios:
            if u.id_usuario == id_usuario:
                return u
        return None

    def registrar_usuario(self, nuevo_usuario):
        usuarios = self.obtener_usuarios()
        if any(u.username == nuevo_usuario.username for u in usuarios):
            raise ValueError("El nombre de usuario ya existe.")
        
        usuarios.append(nuevo_usuario)
        self._guardar_usuarios(usuarios)

    def actualizar_usuario(self, usuario_actualizado):
        usuarios = self.obtener_usuarios()
        for i, u in enumerate(usuarios):
            if u.id_usuario == usuario_actualizado.id_usuario:
                usuarios[i] = usuario_actualizado
                self._guardar_usuarios(usuarios)
                return
        raise ValueError("Usuario no encontrado.")

    def eliminar_usuario(self, id_usuario, id_admin_actual):
        if id_usuario == id_admin_actual:
            raise ValueError("Acción denegada: No puede eliminar su propia cuenta administrativa.")
        
        usuarios = self.obtener_usuarios()
        usuarios = [u for u in usuarios if u.id_usuario != id_usuario]
        self._guardar_usuarios(usuarios)

    def _guardar_usuarios(self, usuarios):
        datos = [u.to_dict() for u in usuarios]
        self.archivo_servicio.escribir_archivo("datos/usuarios.json", datos)

    # --- CRUD PRODUCTOS ---
    def obtener_productos(self):
        datos = self.archivo_servicio.leer_archivo("datos/productos.json")
        if not datos:
            return []
        return [Producto.from_dict(d) for d in datos]

    def obtener_producto_por_id(self, id_producto):
        productos = self.obtener_productos()
        for p in productos:
            if p.id_producto == id_producto:
                return p
        return None

    def registrar_producto(self, nuevo_producto):
        productos = self.obtener_productos()
        if any(p.id_producto == nuevo_producto.id_producto for p in productos):
            raise ValueError("El ID del producto ya existe.")
        productos.append(nuevo_producto)
        self._guardar_productos(productos)

    def actualizar_producto(self, producto_actualizado):
        productos = self.obtener_productos()
        for i, p in enumerate(productos):
            if p.id_producto == producto_actualizado.id_producto:
                productos[i] = producto_actualizado
                self._guardar_productos(productos)
                return
        raise ValueError("Producto no encontrado.")

    def eliminar_producto(self, id_producto):
        productos = self.obtener_productos()
        productos = [p for p in productos if p.id_producto != id_producto]
        self._guardar_productos(productos)

    def _guardar_productos(self, productos):
        datos = [p.to_dict() for p in productos]
        self.archivo_servicio.escribir_archivo("datos/productos.json", datos)