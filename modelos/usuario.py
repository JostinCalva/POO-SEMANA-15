from dataclasses import dataclass


@dataclass
class Usuario:
    identificacion: str
    nombre: str
    usuario: str
    password: str

    def to_dict(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "password": self.password
        }

    @staticmethod
    def from_dict(data):
        return Usuario(
            identificacion=str(
                data.get("identificacion", "")
            ).strip(),

            nombre=str(
                data.get("nombre", "")
            ).strip(),

            usuario=str(
                data.get("usuario", "")
            ).strip(),

            password=str(
                data.get("password", "")
            ).strip()
        )