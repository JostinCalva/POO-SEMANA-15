class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id_producto=data.get("id_producto"),
            nombre=data.get("nombre"),
            precio=data.get("precio", 0.0),
            stock=data.get("stock", 0)
        )