import os
import tkinter as tk
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App - Semana 16")
        self.root.geometry("1000x700")
        self.root.minsize(900, 600)

        # --- SECCIÓN DEL ICONO DE VENTANA ---
        ruta_icono = "assets/logo.png" 
        if os.path.exists(ruta_icono):
            icono_img = tk.PhotoImage(file=ruta_icono)
            self.root.iconphoto(False, icono_img)
        # ------------------------------------

        # 1. Instanciamos el servicio de archivos
        self.archivo_servicio = ArchivoServicio()
        # 2. Instanciamos el servicio del restaurante
        self.restaurante_servicio = RestauranteServicio(self.archivo_servicio)

        self.vista_actual = None
        self.mostrar_login()

    def mostrar_login(self):
        self._limpiar_vista()
        self.vista_actual = LoginView(self.root, self.restaurante_servicio, self.iniciar_sesion)

    def iniciar_sesion(self, usuario_logueado):
        self._limpiar_vista()
        self.vista_actual = MainView(self.root, self.restaurante_servicio, usuario_logueado, self.cerrar_sesion)

    def cerrar_sesion(self):
        self.mostrar_login()

    def _limpiar_vista(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()