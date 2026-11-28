from pathlib import Path
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

PALETTE = {
    "bg_app": ("#eaf3f6", "#0f172a"),
    "sidebar_bg": ("#dceef3", "#13222b"),
    "card_bg": ("#ffffff", "#1e293b"),
    "border": ("#d5e2e7", "#334155"),
    "text_dark": ("#1e293b", "#f1f5f9"),
    "text_muted": ("#64748b", "#94a3b8"),
    "teal_dark": ("#0b6e78", "#0e7490"),
    "teal_hover": ("#095860", "#155e75"),
}


class VehicleRentalApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("system")

        self.title("Vehicle Rental Management System")
        self.geometry("1280x740")
        self.minsize(1050, 620)
        self.configure(fg_color=PALETTE["bg_app"])

        self.selected_item_id = None
        self.active_nav_key = "Vehicles"
        self.nav_buttons = {}

        self._style = ttk.Style(self)
        self._style.theme_use("clam")

        self._build_header()
        self._build_body()
        self._populate_sample_data()
        self.apply_theme()

        icon_path = Path(__file__).resolve().parent / "img" / "icon" / "vrs.ico"
        if icon_path.exists():
            self.after(300, lambda p=str(icon_path): self.iconbitmap(p))

    def _is_dark(self) -> bool:
        return self._get_appearance_mode() == "Dark"

    def _c(self, key: str) -> str:
        light_hex, dark_hex = PALETTE[key]
        return dark_hex if self._is_dark() else light_hex

    def apply_theme(self, mode: str | None = None):
        if mode is not None:
            ctk.set_appearance_mode(mode.lower())

        dark = self._is_dark()
        row_odd = "#1e293b" if dark else "#ffffff"
        row_even = "#16202c" if dark else "#f3f6f8"
        selected_bg = "#164e63" if dark else "#d8f0f4"
        selected_fg = "#f8fafc" if dark else "#0f172a"

        self._style.configure(
            "Vehicles.Treeview",
            background=row_odd,
            fieldbackground=row_odd,
            foreground=self._c("text_dark"),
            rowheight=38,
            font=("Segoe UI", 10),
            borderwidth=0,
        )
        self._style.configure(
            "Vehicles.Treeview.Heading",
            background=self._c("teal_dark"),
            foreground="#ffffff",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padding=(8, 10),
        )
        self._style.map(
            "Vehicles.Treeview.Heading",
            background=[("active", self._c("teal_hover"))],
        )
        self._style.map(
            "Vehicles.Treeview",
            background=[("selected", selected_bg)],
            foreground=[("selected", selected_fg)],
        )

        if hasattr(self, "tree"):
            self.tree.tag_configure("odd", background=row_odd)
            self.tree.tag_configure("even", background=row_even)

        self._refresh_nav_styles()

    def _build_header(self):
        header = ctk.CTkFrame(
            self,
            fg_color=PALETTE["teal_dark"],
            corner_radius=0,
            height=64,
        )
        header.pack(side="top", fill="x")
        header.pack_propagate(False)

        ctk.CTkLabel(
            header,
            text="Manage Vehicles",
            font=("Segoe UI", 22, "bold"),
            text_color="#ffffff",
        ).pack(side="left", padx=24, pady=12)

        right_controls = ctk.CTkFrame(header, fg_color="transparent")
        right_controls.pack(side="right", padx=24, pady=12)

        ctk.CTkLabel(
            right_controls,
            text="Welcome Sherwin Dave (Admin)",
            font=("Segoe UI", 12, "bold"),
            text_color="#e6f7fa",
        ).pack(side="left", padx=(0, 14))

        self.theme_selector = ctk.CTkSegmentedButton(
            right_controls,
            values=["System", "Light", "Dark"],
            command=self.apply_theme,
            font=("Segoe UI", 11, "bold"),
            fg_color=PALETTE["teal_hover"],
            selected_color="#ffffff",
            selected_hover_color="#eef7f9",
            unselected_color=PALETTE["teal_hover"],
            unselected_hover_color=PALETTE["teal_dark"],
            text_color=PALETTE["teal_dark"],
        )
        self.theme_selector.set("System")
        self.theme_selector.pack(side="left")

    def _build_body(self):
        body = ctk.CTkFrame(self, fg_color=PALETTE["bg_app"], corner_radius=0)
        body.pack(side="top", fill="both", expand=True)

        # --- Sidebar ---
        sidebar = ctk.CTkFrame(
            body,
            fg_color=PALETTE["sidebar_bg"],
            corner_radius=0,
            width=215,
        )
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        nav_items = [
            ("Dashboard", "⊞"),
            ("Vehicles", "🚗"),
            ("Users", "👥"),
        ]
        for label, icon in nav_items:
            self._add_nav_button(sidebar, label, f"{icon}   {label}")

        # Divider
        ctk.CTkFrame(
            sidebar,
            fg_color=PALETTE["border"],
            height=1,
        ).pack(fill="x", padx=22, pady=16)

        for label, icon in [("Rent & Return", "📋"), ("History", "🕒")]:
            self._add_nav_button(sidebar, label, f"{icon}   {label}")

        # Logout button at bottom
        ctk.CTkButton(
            sidebar,
            text="Logout",
            font=("Segoe UI", 11, "bold"),
            fg_color=PALETTE["card_bg"],
            hover_color=PALETTE["bg_app"],
            text_color=PALETTE["teal_dark"],
            border_color=PALETTE["teal_dark"],
            border_width=1.5,
            corner_radius=8,
            height=34,
            width=120,
            command=self.destroy,
        ).pack(side="bottom", pady=28)

        # --- Main Content Area ---
        content = ctk.CTkFrame(body, fg_color=PALETTE["bg_app"], corner_radius=0)
        content.pack(side="left", fill="both", expand=True, padx=22, pady=22)

        content.grid_rowconfigure(0, weight=1)
        content.grid_columnconfigure(0, weight=0, minsize=340)
        content.grid_columnconfigure(1, weight=1)

        # Left Card: Vehicle Details Form
        form_card = ctk.CTkFrame(
            content,
            fg_color=PALETTE["card_bg"],
            corner_radius=16,
            border_color=PALETTE["border"],
            border_width=1,
        )
        form_card.grid(row=0, column=0, sticky="ns", padx=(0, 18))

        ctk.CTkLabel(
            form_card,
            text="Vehicle Details",
            font=("Segoe UI", 18, "bold"),
            text_color=PALETTE["text_dark"],
        ).pack(anchor="w", padx=24, pady=(24, 14))

        self.name_entry = self._add_field(form_card, "Vehicle Name", "Vehicle Name")
        self.brand_entry = self._add_field(form_card, "Brand / Type", "Sedan / SUV")
        self.plate_entry = self._add_field(form_card, "License Plate", "License Plate")
        self.status_entry = self._add_field(form_card, "Status", "Available / Rented")
        self.rate_entry = self._add_field(form_card, "Rental Rate", "Rental / Day")

        btn_row = ctk.CTkFrame(form_card, fg_color="transparent")
        btn_row.pack(fill="x", padx=24, pady=(14, 24))
        btn_row.grid_columnconfigure(0, weight=1)
        btn_row.grid_columnconfigure(1, weight=1)

        ctk.CTkButton(
            btn_row,
            text="Save Vehicle",
            font=("Segoe UI", 11, "bold"),
            fg_color=PALETTE["teal_dark"],
            hover_color=PALETTE["teal_hover"],
            text_color="#ffffff",
            corner_radius=8,
            height=38,
            command=self.save_vehicle,
        ).grid(row=0, column=0, sticky="ew", padx=(0, 6))

        ctk.CTkButton(
            btn_row,
            text="Update",
            font=("Segoe UI", 11, "bold"),
            fg_color=PALETTE["teal_dark"],
            hover_color=PALETTE["teal_hover"],
            text_color="#ffffff",
            corner_radius=8,
            height=38,
            command=self.update_vehicle,
        ).grid(row=0, column=1, sticky="ew", padx=(6, 0))

        # Right Card: Table
        table_card = ctk.CTkFrame(
            content,
            fg_color=PALETTE["card_bg"],
            corner_radius=16,
            border_color=PALETTE["border"],
            border_width=1,
        )
        table_card.grid(row=0, column=1, sticky="nsew")

        columns = ("id", "name", "type", "status", "price")
        self.tree = ttk.Treeview(
            table_card,
            columns=columns,
            show="headings",
            style="Vehicles.Treeview",
        )
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Vehicle Name")
        self.tree.heading("type", text="Type")
        self.tree.heading("status", text="Status")
        self.tree.heading("price", text="Price / Day")

        self.tree.column("id", width=65, anchor="center")
        self.tree.column("name", width=190, anchor="w")
        self.tree.column("type", width=120, anchor="w")
        self.tree.column("status", width=120, anchor="w")
        self.tree.column("price", width=120, anchor="w")

        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)
        self.tree.pack(fill="both", expand=True, padx=18, pady=18)

    def _add_nav_button(self, parent, key, display_text):
        btn = ctk.CTkButton(
            parent,
            text=display_text,
            anchor="w",
            corner_radius=18,
            height=38,
            command=lambda k=key: self.set_active_nav(k),
        )
        btn.pack(fill="x", padx=16, pady=6)
        self.nav_buttons[key] = btn

    def _refresh_nav_styles(self):
        inactive_hover = "#1e3a46" if self._is_dark() else "#cbe4ec"
        for key, btn in self.nav_buttons.items():
            is_active = key == self.active_nav_key
            btn.configure(
                fg_color=PALETTE["teal_dark"] if is_active else "transparent",
                hover_color=PALETTE["teal_hover"] if is_active else inactive_hover,
                text_color="#ffffff" if is_active else PALETTE["text_dark"],
                font=("Segoe UI", 12, "bold" if is_active else "normal"),
            )

    def set_active_nav(self, active_key):
        self.active_nav_key = active_key
        self._refresh_nav_styles()

    def _add_field(self, parent, label_text, placeholder):
        ctk.CTkLabel(
            parent,
            text=label_text,
            font=("Segoe UI", 11, "bold"),
            text_color=PALETTE["text_dark"],
        ).pack(anchor="w", padx=24, pady=(4, 3))

        entry = ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            placeholder_text_color=PALETTE["text_muted"],
            font=("Segoe UI", 11),
            fg_color=PALETTE["card_bg"],
            text_color=PALETTE["text_dark"],
            border_color=PALETTE["border"],
            border_width=1.2,
            corner_radius=8,
            height=36,
        )
        entry.pack(fill="x", padx=24, pady=(0, 8))
        return entry

    def _set_entry(self, entry, value):
        entry.delete(0, tk.END)
        if value:
            entry.insert(0, str(value))

    def _populate_sample_data(self):
        rows = [
            ("1", "Toyota Vios", "Sedan", "Available", "1500"),
            ("2", "Mitsubishi Montero", "SUV", "Available", "2800"),
            ("3", "Honda Civic", "Sedan", "Rented", "1800"),
            ("4", "Ford Ranger", "SUV", "Available", "3000"),
        ]
        for idx, row in enumerate(rows):
            tag = "even" if idx % 2 else "odd"
            self.tree.insert("", "end", values=row, tags=(tag,))

    def _reapply_row_stripes(self):
        for idx, item_id in enumerate(self.tree.get_children()):
            tag = "even" if idx % 2 else "odd"
            self.tree.item(item_id, tags=(tag,))

    def on_row_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        self.selected_item_id = selected[0]
        _, name, v_type, status, price = self.tree.item(self.selected_item_id, "values")

        self._set_entry(self.name_entry, name)
        self._set_entry(self.brand_entry, v_type)
        self._set_entry(self.status_entry, status)
        self._set_entry(self.rate_entry, price)

    def save_vehicle(self):
        name = self.name_entry.get().strip()
        v_type = self.brand_entry.get().strip() or "Sedan"
        status = self.status_entry.get().strip() or "Available"
        price = self.rate_entry.get().strip() or "0"
        if not name:
            return

        next_id = str(len(self.tree.get_children()) + 1)
        self.tree.insert("", "end", values=(next_id, name, v_type, status, price))
        self._reapply_row_stripes()

    def update_vehicle(self):
        if not self.selected_item_id:
            return
        current_id = self.tree.item(self.selected_item_id, "values")[0]
        name = self.name_entry.get().strip()
        v_type = self.brand_entry.get().strip()
        status = self.status_entry.get().strip()
        price = self.rate_entry.get().strip()
        if not name:
            return

        self.tree.item(
            self.selected_item_id,
            values=(current_id, name, v_type, status, price),
        )
        self._reapply_row_stripes()


if __name__ == "__main__":
    app = VehicleRentalApp()
    app.mainloop()