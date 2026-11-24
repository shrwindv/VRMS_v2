import tkinter as tk
from tkinter import ttk
from .query import Query

class Dashboard:

    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        qry = Query()
        page_title = tk.Label(
            self.parent,
            text = "Dashboard",
            font = ("Verdana", 20, "bold"),
            bg = "#FFFFFF",
            fg = "#676D6F"
        )
        page_title.pack(pady=(30,0), padx=(50, 0), side="top", anchor="w")

        card_holder = tk.Frame(
            self.parent,
            width=800,
            height=160,
            bg="#FFFFFF",
        )
        card_holder.pack(fill="x", padx=100, pady=50, side="top")
        card_holder.pack_propagate(False)

        # 1. Configure columns 0, 1, 2 to expand and share space evenly
        card_holder.grid_columnconfigure(0, weight=1)
        card_holder.grid_columnconfigure(1, weight=1)
        card_holder.grid_columnconfigure(2, weight=1)
        
        usr = qry.count_users()
        vhs = qry.count_vehicles()
        unr = qry.count_unreturned()

        # 2. Loop from 0 to 2 so they center neatly inside the configured columns
        for i in range(3):
            card = tk.Frame(
                card_holder,
                bg="#FFFFFF",
                bd=2,
                relief="ridge",
                height=140,  # Adjusted slightly to fit comfortably inside the 160px height card_holder
                width=200,
            )
            card.grid(row=0, column=i, padx=10, pady=10, sticky="n")
            card.pack_propagate(False) # Optional: if you want the card dimensions strictly locked
            tk.Label(
                card,
                text = usr if i == 0 else (vhs if i == 1 else unr),
                fg = "#676D6F",
                bg = "#FFFFFF",
                font =("Verdana", 30, "bold")
            ).pack(expand=True, pady=(30, 0))
            tk.Label(
                card,
                text = "Users" if i == 0 else ("Total No. of Vehicles" if i == 1 else "Unreturned Vehicle/s"),
                pady = 0,
                bg = "#FFFFFF",
                font = ("Verdana", 10, "bold")
            ).pack(expand=True)

        tk.Label(self.parent, text="Recently Rented:", bg="#FFFFFF").pack(padx=100, anchor="nw")

        history = qry.dashboard_tb()
        count = len(history)

        thead = ["Username", "Vehicle", "Rented - Return"]

        table = tk.Frame(
            self.parent,
            height=50 * (count + 1),
            bg="#FFFFFF",
            bd=2,
            relief="ridge"
        )

        table.pack(fill="x", padx=100, pady=20)
        table.pack_propagate(False)

        # Configure columns
        for index in range(len(thead)):
            table.grid_columnconfigure(index, weight=1)

        # Header
        for index, th in enumerate(thead):
            head = tk.Frame(
                table,
                height=43,
                bg="#FFFFFF",
                bd=1,
                relief="solid"
            )

            head.grid(row=0, column=index, sticky="nsew", padx=1, pady=1)
            head.grid_propagate(False)

            tk.Label(
                head,
                text=th,
                bg="#FFFFFF",
                font=("Verdana", 10, "bold")
            ).pack(fill="both", expand=True)

        # Data rows
        for row_index, record in enumerate(history, start=1):

            values = [
                record[1] + " " + record[3],
                record[5],
                record[8]
            ]

            for column_index, value in enumerate(values):

                cell = tk.Frame(
                    table,
                    height=42,
                    bg="#FFFFFF",
                    bd=1,
                    relief="solid"
                )

                cell.grid(
                    row=row_index,
                    column=column_index,
                    sticky="nsew",
                    padx=1,
                    pady=1
                )

                cell.grid_propagate(False)

                tk.Label(
                    cell,
                    text=value,
                    bg="#FFFFFF",
                    font=("Verdana", 10)
                ).pack(fill="both", expand=True)
