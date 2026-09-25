import tkinter as tk
from tkinter import ttk, messagebox


class LoginView:

    def __init__(
        self,
        root,
        restaurante_servicio,
        iniciar_sesion
    ):
        self.root = root
        self.restaurante_servicio = restaurante_servicio
        self.iniciar_sesion = iniciar_sesion

        self.frame = ttk.Frame(
            root,
            padding=30
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        self.crear_interfaz()

    def crear_interfaz(self):

        ttk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 24, "bold")
        ).pack(pady=(50, 10))

        ttk.Label(
            self.frame,
            text="Sistema de gestión de restaurante",
            font=("Arial", 12)
        ).pack(pady=(0, 30))

        formulario = ttk.Frame(
            self.frame
        )

        formulario.pack()

        ttk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.entrada_usuario = ttk.Entry(
            formulario,
            width=30
        )

        self.entrada_usuario.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            formulario,
            text="Contraseña:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.entrada_password = ttk.Entry(
            formulario,
            width=30,
            show="*"
        )

        self.entrada_password.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Button(
            formulario,
            text="Ingresar",
            command=self.procesar_login
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=20
        )

    def procesar_login(self):

        usuario = self.entrada_usuario.get().strip()
        password = self.entrada_password.get().strip()

        if not usuario or not password:

            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese usuario y contraseña."
            )

            return

        correcto, usuario_encontrado = (
            self.restaurante_servicio.validar_acceso(
                usuario,
                password
            )
        )

        if correcto:

            self.iniciar_sesion(
                usuario_encontrado
            )

        else:

            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos."
            )

    def destruir(self):
        self.frame.destroy()