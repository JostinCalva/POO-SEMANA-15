import os
import tkinter as tk
from tkinter import messagebox

class LoginView:
    def __init__(self, root, servicio, callback_iniciar_sesion):
        self.root = root
        self.servicio = servicio
        self.callback_iniciar_sesion = callback_iniciar_sesion
        self._crear_interfaz()

    def _crear_interfaz(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        # --- SECCIÓN DEL LOGO ---
        ruta_logo = "assets/logo.png" 
        if os.path.exists(ruta_logo):
            self.logo_img = tk.PhotoImage(file=ruta_logo)
            # Si el logo es muy grande, puedes descomentar la siguiente línea:
            # self.logo_img = self.logo_img.subsample(2, 2)
            tk.Label(frame, image=self.logo_img).pack(pady=5)
        # ------------------------

        tk.Label(frame, text="RESTAURANTE APP", font=("Arial", 24, "bold")).pack(pady=5)
        tk.Label(frame, text="Sistema de gestión de restaurante", font=("Arial", 12)).pack(pady=10)

        frame_form = tk.Frame(frame)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_user = tk.Entry(frame_form)
        self.entry_user.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frame_form, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_pass = tk.Entry(frame_form, show="*")
        self.entry_pass.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(frame, text="Ingresar", command=self.procesar_login).pack(pady=15)

    def procesar_login(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()

        es_valido, usuario_encontrado = self.servicio.validar_acceso(username, password)

        if es_valido:
            self.callback_iniciar_sesion(usuario_encontrado)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")