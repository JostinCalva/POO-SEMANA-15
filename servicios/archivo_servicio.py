import json
import os


class ArchivoServicio:

    def asegurar_archivo(self, ruta, contenido_inicial=None):
        carpeta = os.path.dirname(ruta)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        if not os.path.exists(ruta):
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(
                    contenido_inicial if contenido_inicial is not None else [],
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

    def leer_json(self, ruta):
        self.asegurar_archivo(ruta, [])

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def guardar_json(self, ruta, datos):
        carpeta = os.path.dirname(ruta)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                ensure_ascii=False,
                indent=4
            )