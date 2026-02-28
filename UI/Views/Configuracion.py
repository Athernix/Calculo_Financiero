import tkinter as tk

class Configuracion(tk.Frame):
    def __init__(self, parent):
        # El parent es view_container, parent.master es MainUI
        super().__init__(parent)
        self.main_app = parent.master 
        self.theme = self.main_app.theme
        
        self.configure(bg=self.theme.BG_LIGHT)
        self._build_layout()

    def _build_layout(self):
        header = tk.Frame(self, bg=self.theme.BG_LIGHT, height=100)
        header.pack(fill="x", padx=40)
        header.pack_propagate(False)

        tk.Label(header, text="Ajustes / Sistema", bg=self.theme.BG_LIGHT, 
                 fg=self.theme.TEXT_MUTED, font=self.theme.FONT_LABEL).pack(side="top", anchor="w", pady=(25, 0))

        tk.Label(header, text="Configuración", bg=self.theme.BG_LIGHT, 
                 fg=self.theme.TEXT_DARK, font=("Inter", 22, "bold")).pack(side="top", anchor="w")

        content = tk.Frame(self, bg=self.theme.BG_LIGHT)
        content.pack(fill="both", expand=True, padx=40, pady=20)

        # CARD DE APARIENCIA
        tk.Label(content, text="Apariencia", bg=self.theme.BG_LIGHT, fg=self.theme.TEXT_DARK, 
                 font=("Inter", 12, "bold")).pack(anchor="w", pady=(10, 15))
        
        card = tk.Frame(content, bg=self.theme.CARD, padx=20, pady=20, 
                        highlightbackground=self.theme.BORDER, highlightthickness=1)
        card.pack(fill="x")

        row = tk.Frame(card, bg=self.theme.CARD)
        row.pack(fill="x")

        tk.Label(row, text="Cambiar Tema Visual", bg=self.theme.CARD, fg=self.theme.TEXT_DARK, 
                 font=self.theme.FONT_BUTTON).pack(side="left")

        toggle_text = "🌙 Modo Oscuro" if self.main_app.current_mode == "dark" else "☀️ Modo Claro"
        tk.Button(
            row, text=toggle_text, bg=self.theme.ACCENT, fg="white",
            font=("Inter", 9, "bold"), bd=0, padx=15, pady=8, cursor="hand2",
            command=self.main_app.toggle_theme
        ).pack(side="right")