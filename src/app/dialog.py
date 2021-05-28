import tkinter as tk
from tkinter import ttk

from ttkthemes import ThemedTk

from app.geometry import AppGeometry


class CustomDialog(ThemedTk):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_theme('arc')

        app = AppGeometry()

        h = self.winfo_screenheight() // 2
        w = self.winfo_screenwidth() // 2

        self.geometry(f'{app.dialog_width}x{app.dialog_height}+{w}+{h}')
        self.resizable(width=False, height=False)

        self._layout = ttk.Frame(self)
        self._layout.grid(column=0, row=0, sticky=tk.NSEW)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # self._layout.grid_columnconfigure((0, 1, 2), weight=1)
        # self._layout.grid_rowconfigure((0, 1, 2), weight=3)

        self._save_btn = ttk.Button(self._layout, text='Save')
        self._save_btn.grid(row=10, column=1, sticky=tk.E, pady=5)