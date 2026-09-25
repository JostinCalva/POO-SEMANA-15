import tkinter as tk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Restaurante App - Semana 15"
        )

        self.root.geometry(
            "1000x700"
        )

        self.root.minsize(
            900,
            600
        )

        self.archivo_servicio = ArchivoServicio()

        self.restaurante_servicio = RestauranteServicio(
            self.archivo_servicio
        )

        self.login_view = None
        self.main_view = None

        self.mostrar_login()

    def mostrar_login(self):

        if self.main_view is not None:
            self.main_view.destruir()
            self.main_view = None

        self.login_view = LoginView(
            self.root,
            self.restaurante_servicio,
            self.iniciar_sesion
        )

    def iniciar_sesion(self, usuario):

        if self.login_view is not None:
            self.login_view.destruir()
            self.login_view = None

        self.main_view = MainView(
            self.root,
            self.restaurante_servicio,
            self.cerrar_sesion
        )

    def cerrar_sesion(self):

        if self.main_view is not None:
            self.main_view.destruir()
            self.main_view = None

        self.mostrar_login()


def main():

    root = tk.Tk()

    app = RestauranteApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()