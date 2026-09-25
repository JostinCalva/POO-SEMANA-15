from dataclasses import dataclass


@dataclass
class Venta:
    usuario: str
    producto: str
    fecha: str

    def to_dict(self):
        return {
            "usuario": self.usuario,
            "producto": self.producto,
            "fecha": self.fecha
        }

    @staticmethod
    def from_dict(data):
        return Venta(
            usuario=str(data.get("usuario", "")),
            producto=str(data.get("producto", "")),
            fecha=str(data.get("fecha", ""))
        )