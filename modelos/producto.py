from dataclasses import dataclass


@dataclass
class Producto:
    codigo: str
    nombre: str
    precio: float
    stock: int

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            codigo=str(data.get("codigo", "")),
            nombre=str(data.get("nombre", "")),
            precio=float(data.get("precio", 0)),
            stock=int(data.get("stock", 0))
        )