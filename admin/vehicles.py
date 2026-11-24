import tkinter as tk
from tkinter import ttk
from .query import Query

class Vehicles:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        qry = Query()

        page_frame = tk.Frame(
            self.parent,
            bg = "#FFFFFF",
            height = 730,
            padx = 30,
            pady = 30
        )
        page_frame.pack(fill="x")
        page_frame.pack_propagate(False)

        header = tk.Label(
            page_frame,
            text = "Hello",
            bg = "#FFFFFF",
            font = ("Verdana", 10, "bold")
        )
        header.pack()