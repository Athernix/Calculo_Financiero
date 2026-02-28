import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.theme = parent.theme
        super().__init__(parent, bg=self.theme.SECONDARY, width=260)
        self.pack_propagate(False)
        self._build_widgets()

    def _build_widgets(self):
        # LOGO
        tk.Label(
            self, text="⚡ Cálculo Pro", bg=self.theme.SECONDARY, 
            fg=self.theme.TEXT_DARK, font=self.theme.FONT_TITLE, anchor="w"
        ).pack(fill="x", pady=30, padx=20)

        # --- LÓGICA DE DETECCIÓN DE VISTA ACTIVA ---
        from UI.Views.Inicio import Inicio
        from UI.Views.Configuracion import Configuracion
        
        # Obtenemos qué vista tiene cargada el MainUI actualmente
        vista_actual = getattr(self.parent, 'current_view', None)

        # Definimos los items: (Nombre, Icono, Comando, Clase_Relacionada)
        menu_items = [
            ("Inicio", "🏠", self.parent.mostrar_inicio, Inicio),
            ("Finanzas", "💰", None, None),
            ("Cálculos", "🔢", None, None),
            ("Gráficos", "📊", None, None),
            ("Configuración", "⚙️", self.parent.mostrar_configuracion, Configuracion)
        ]

        for text, icon, cmd, clase_vista in menu_items:
            # Si la vista actual es una instancia de la clase_vista, está activo
            es_activo = isinstance(vista_actual, clase_vista) if clase_vista else False
            self._create_menu_button(text, icon, cmd, es_activo)

        spacer = tk.Frame(self, bg=self.theme.SECONDARY)
        spacer.pack(fill="both", expand=True)

    def _create_menu_button(self, text, icon, command, active):
        # Colores basados en si está seleccionado o no
        if active:
            bg = self.theme.ACCENT  # Color resaltado (Morado/Azul)
            fg = "white"
        else:
            bg = self.theme.SECONDARY
            # En modo claro el texto muted es gris, en oscuro es blanco suave
            fg = self.theme.TEXT_MUTED if self.parent.current_mode == "light" else self.theme.TEXT_DARK
        
        btn = tk.Button(
            self, text=f"   {icon}    {text}", anchor="w", bg=bg, fg=fg,
            font=self.theme.FONT_BUTTON, bd=0, padx=20, pady=12,
            activebackground=self.theme.ACCENT, activeforeground="white",
            cursor="hand2", command=command if command else lambda: print(f"Click en {text}")
        )
        btn.pack(fill="x", padx=10, pady=2)