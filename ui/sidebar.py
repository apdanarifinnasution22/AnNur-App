import customtkinter as ctk
from tkinter import filedialog, messagebox

from processing.filter import grayscale, blur, edge
from processing.color import adjust_brightness, adjust_contrast
from processing.crop import crop_center
from processing.face import detect_face, auto_crop_face

class Sidebar(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app, width=220)
        self.app = app

        ctk.CTkLabel(self, text="AnNur App", font=("Arial",16,"bold")).pack(pady=15)

        self.btn("▶ Start Camera", app.camera.start)
        self.btn("⏹ Stop Camera", app.camera.stop, color="red")
        self.btn("📸 Capture Photo", app.camera.capture)
        self.btn("🔄 Reset Image", app.camera.reset)

        ctk.CTkLabel(self, text="──── Filter ────").pack(pady=5)
        self.btn("Grayscale", lambda: app.camera.apply(grayscale))
        self.btn("Blur", lambda: app.camera.apply(blur))
        self.btn("Edge", lambda: app.camera.apply(edge))
        self.btn("Crop Center", lambda: app.camera.apply(crop_center))

        ctk.CTkLabel(self, text="── Face Detection ──").pack(pady=5)
        self.btn("Detect Face", lambda: app.camera.apply(lambda f: detect_face(f)[0]))
        self.btn("Auto Crop Face", lambda: app.camera.apply(auto_crop_face))

        ctk.CTkLabel(self, text="Brightness").pack()
        ctk.CTkSlider(self, from_=-100, to=100,
            command=lambda v: app.camera.apply(lambda f: adjust_brightness(f,int(v)))
        ).pack()

        ctk.CTkLabel(self, text="Contrast").pack()
        ctk.CTkSlider(self, from_=1, to=100,
            command=lambda v: app.camera.apply(lambda f: adjust_contrast(f,int(v)))
        ).pack()

        self.btn("💾 Save Image", self.save)

    def btn(self, text, cmd, color=None):
        ctk.CTkButton(self, text=text, fg_color=color, command=self.safe(cmd)).pack(pady=4)

    def safe(self, func):
        def wrap():
            try:
                func()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        return wrap

    def save(self):
        path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if path:
            self.app.camera.save_image(path)
