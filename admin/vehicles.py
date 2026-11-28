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


# ___________________________________________________________________________________________________
# left & right Frames

        left = tk.LabelFrame(
            page_frame,
            text = "Vehicle Detail",
            fg = "#373D3F",
            bg = "#FFFFFF",
            height = 1000,
            width = 400,
            font = ("Arial", 12, "bold"),
            labelanchor="n",
            padx = 12,
            pady = 12
        )
        left.pack(side="left", padx=(0,15))

        right = tk.Frame(
            page_frame,
            height = 50,
            width = 800,
        )
        right.pack(side="right", padx=(15,0))
        right.pack_propagate()

        right_search = tk.Frame(
            right,
            bg = "#000000",
            height = 50,
            width = 800,
        )
        right_search.pack()

        right_table = tk.Frame(
            right,
            bg = "#0097B2",
            height = 950,
            width = 800,
        )
        right_table.pack()