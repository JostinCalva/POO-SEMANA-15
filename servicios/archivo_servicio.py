import json
import os

class ArchivoServicio:
    def leer_archivo(self, ruta):
        if not os.path.exists(ruta):
            return []
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)

    def escribir_archivo(self, ruta, datos):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4)