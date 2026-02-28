import tkinter as tk
from UI.Components.Personaliza import Personaliza
from UI.Components.Sidebar import Sidebar

class MainUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.current_mode = "dark"
        self.theme = Personaliza(self.current_mode)
        
        self.configure(bg=self.theme.BG_LIGHT)
        self.pack(fill="both", expand=True)
        self._configure_window()

        self.sidebar = None
        self.current_view = None
        
        self.view_container = tk.Frame(self, bg=self.theme.BG_LIGHT)
        self.view_container.pack(side="right", fill="both", expand=True)

        # Carga inicial
        self.mostrar_inicio()

    def _configure_window(self):
        self.master.title("Cálculo Financiero Pro")
        self.master.geometry(f"{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}")
        self.master.minsize(1100, 700)

    def _limpiar_contenedor(self):
        for widget in self.view_container.winfo_children():
            widget.destroy()

    def _actualizar_sidebar(self):
        if self.sidebar:
            self.sidebar.destroy()
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

    def mostrar_inicio(self):
        self._limpiar_contenedor()
        from UI.Views.Inicio import Inicio # Importación dentro para evitar círculos
        self.current_view = Inicio(self.view_container)
        self.current_view.pack(fill="both", expand=True)
        self._actualizar_sidebar()

    def mostrar_configuracion(self):
        self._limpiar_contenedor()
        from UI.Views.Configuracion import Configuracion # Importación crítica de la CLASE
        self.current_view = Configuracion(self.view_container)
        self.current_view.pack(fill="both", expand=True)
        self._actualizar_sidebar()

    def toggle_theme(self):
        self.current_mode = "light" if self.current_mode == "dark" else "dark"
        self.theme.set_theme(self.current_mode)
        
        # Refrescar colores base
        self.configure(bg=self.theme.BG_LIGHT)
        self.view_container.configure(bg=self.theme.BG_LIGHT)
        
        # Recargar vista actual
        from UI.Views.Configuracion import Configuracion
        if isinstance(self.current_view, Configuracion):
            self.mostrar_configuracion()
        else:
            self.mostrar_inicio()