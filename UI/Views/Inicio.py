import tkinter as tk

class Inicio(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.theme = parent.master.theme
        self.configure(bg=self.theme.BG_LIGHT)
        self._build_layout()

    def _build_layout(self):
        header = tk.Frame(self, bg=self.theme.BG_LIGHT, height=100)
        header.pack(fill="x", padx=40)
        header.pack_propagate(False)

        tk.Label(header, text="Dashboard / Inicio", bg=self.theme.BG_LIGHT, 
                 fg=self.theme.TEXT_MUTED, font=self.theme.FONT_LABEL).pack(side="top", anchor="w", pady=(25, 0))

        tk.Label(header, text="Resumen Financiero", bg=self.theme.BG_LIGHT, 
                 fg=self.theme.TEXT_DARK, font=("Inter", 22, "bold")).pack(side="top", anchor="w")

        content = tk.Frame(self, bg=self.theme.BG_LIGHT)
        content.pack(fill="both", expand=True, padx=40, pady=20)

        # Tarjetas de ejemplo
        metrics_frame = tk.Frame(content, bg=self.theme.BG_LIGHT)
        metrics_frame.pack(fill="x")

        self._metric_card(metrics_frame, "Total Préstamos", "1,240", "↗ 12%").pack(side="left", expand=True, fill="x", padx=(0, 10))
        self._metric_card(metrics_frame, "Tasa Promedio", "5.4%", "Stable").pack(side="left", expand=True, fill="x", padx=(10, 0))

    def _metric_card(self, parent, title, value, badge):
        card = tk.Frame(parent, bg=self.theme.CARD, highlightbackground=self.theme.BORDER, 
                        highlightthickness=1, padx=20, pady=20)
        tk.Label(card, text=title, bg=self.theme.CARD, fg=self.theme.TEXT_MUTED, font=self.theme.FONT_LABEL).pack(anchor="w")
        
        val_frame = tk.Frame(card, bg=self.theme.CARD)
        val_frame.pack(fill="x", pady=(10,0))
        tk.Label(val_frame, text=value, bg=self.theme.CARD, fg=self.theme.TEXT_DARK, font=("Inter", 18, "bold")).pack(side="left")
        tk.Label(val_frame, text=badge, bg=self.theme.CARD, fg="#4ade80", font=("Inter", 9)).pack(side="right")
        return card