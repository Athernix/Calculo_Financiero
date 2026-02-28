class Personaliza:
    THEMES = {
        "dark": {
            "PRIMARY": "#121212",
            "SECONDARY": "#1a1a1a",
            "BG_LIGHT": "#1e1e1e",
            "CARD": "#252525",
            "TEXT_DARK": "#ffffff",
            "TEXT_MUTED": "#a0a0a0",
            "TEXT_LOW": "#666666",
            "BORDER": "#333333",
            "ACCENT": "#5d5fef"
        },
        "light": {
            "PRIMARY": "#ffffff",
            "SECONDARY": "#f0f2f5",
            "BG_LIGHT": "#f8f9fa",
            "CARD": "#ffffff",
            "TEXT_DARK": "#1a1a1a",
            "TEXT_MUTED": "#6c757d",
            "TEXT_LOW": "#adb5bd",
            "BORDER": "#dee2e6",
            "ACCENT": "#4e50d1"
        }
    }

    def __init__(self, mode="dark"):
        self.FONT_TITLE = ("Inter", 14, "bold")
        self.FONT_BUTTON = ("Inter", 10)
        self.FONT_LABEL = ("Inter", 9)
        self.set_theme(mode)

    def set_theme(self, mode):
        # Selecciona el diccionario de colores o dark por defecto
        data = self.THEMES.get(mode, self.THEMES["dark"])
        
        # Asignación dinámica (Asegura que todos los atributos existan en ambos temas)
        self.PRIMARY = data["PRIMARY"]
        self.SECONDARY = data["SECONDARY"]
        self.BG_LIGHT = data["BG_LIGHT"]
        self.CARD = data["CARD"]
        self.TEXT_DARK = data["TEXT_DARK"]
        self.TEXT_MUTED = data["TEXT_MUTED"]
        self.TEXT_LOW = data["TEXT_LOW"]
        self.BORDER = data["BORDER"]
        self.ACCENT = data["ACCENT"]