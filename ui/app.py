import customtkinter as ctk
from ui.canvas_view import CanvasView
from ui.sidebar import Sidebar
from ui.menubar import MenuBar
from processing.camera import Camera

class AnNurApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("AnNur App")
        self.geometry("1200x700")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # MENU
        MenuBar(self)

        # CANVAS
        self.canvas_view = CanvasView(self)
        self.canvas_view.grid(row=0, column=1, sticky="nsew")

        # CAMERA
        self.camera = Camera(self.canvas_view, self)

        # SIDEBAR
        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # =====================
        # STATUS BAR (🔥 DI SINI TEMPATNYA)
        # =====================
        self.status_var = ctk.StringVar()
        self.status_var.set("Ready")

        self.status_bar = ctk.CTkLabel(
            self,
            textvariable=self.status_var,
            anchor="w",
            height=28
        )
        self.status_bar.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10)

    # =====================
    # UPDATE STATUS BAR
    # =====================
    def update_status(self, source="None"):
        if self.camera.current_frame is None:
            self.status_var.set("No Image")
            return

        h, w = self.camera.current_frame.shape[:2]
        mode = "Camera" if self.camera.mode == "camera" else "Image"

        self.status_var.set(
            f"Resolution: {w}×{h} | Mode: {mode} | Source: {source}"
        )
