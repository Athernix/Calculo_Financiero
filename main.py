import tkinter as tk
from UI.Views.main_ui import MainUI

if __name__ == "__main__":
    root = tk.Tk()
    app = MainUI(root)
    root.mainloop()