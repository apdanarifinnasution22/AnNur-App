import os
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

from processing.histogram import show_histogram
from processing.morphology import erosion, dilation, opening, closing
from processing.compare import before_after, difference_image
from processing.compress import compress_image
from processing.color_space import to_hsv, to_hsi, to_ycbcr, to_cmyk
from processing.channel_split import channel_r, channel_g, channel_b


class MenuBar:
    def __init__(self, app):
        menubar = tk.Menu(app)


       # =====================
        # FILE
        # =====================
        file_menu = tk.Menu(menubar, tearoff=0)

        file_menu.add_command(
            label="📂 Open Image",
            command=lambda: self.open(app)
        )

        file_menu.add_command(
            label="🗜 Compress & Save Image",
            command=lambda: self.compress(app)
        )

        file_menu.add_separator()

        file_menu.add_command(
            label="❌ Exit",
            command=app.quit
        )

        menubar.add_cascade(label="File", menu=file_menu)

        # =====================
        # TRANSFORM
        # =====================
        transform_menu = tk.Menu(menubar, tearoff=0)

        transform_menu.add_command(
            label="Rotate 90°",
            command=lambda: app.camera.rotate(90)
        )
        transform_menu.add_command(
            label="Rotate 180°",
            command=lambda: app.camera.rotate(180)
        )
        transform_menu.add_command(
            label="Rotate 270°",
            command=lambda: app.camera.rotate(270)
        )

        menubar.add_cascade(label="Transform", menu=transform_menu)

        app.config(menu=menubar)
        # =====================
        # VIEW / THEME
        # =====================
        view_menu = tk.Menu(menubar, tearoff=0)
        theme_menu = tk.Menu(view_menu, tearoff=0)
        theme_menu.add_command(label="🌞 Light", command=lambda: self.set_theme("Light"))
        theme_menu.add_command(label="🌙 Dark", command=lambda: self.set_theme("Dark"))
        theme_menu.add_command(label="💻 System", command=lambda: self.set_theme("System"))
        view_menu.add_cascade(label="Theme", menu=theme_menu)
        menubar.add_cascade(label="View", menu=view_menu)

        # =====================
        # MORFOLOGI
        # =====================
        morph_menu = tk.Menu(menubar, tearoff=0)
        morph_menu.add_command(label="Erosion", command=lambda: app.camera.apply(erosion))
        morph_menu.add_command(label="Dilation", command=lambda: app.camera.apply(dilation))
        morph_menu.add_command(label="Opening", command=lambda: app.camera.apply(opening))
        morph_menu.add_command(label="Closing", command=lambda: app.camera.apply(closing))
        menubar.add_cascade(label="Morfologi", menu=morph_menu)

        # =====================
        # KOMPARASI
        # =====================
        compare_menu = tk.Menu(menubar, tearoff=0)
        compare_menu.add_command(label="🔍 Before vs After", command=lambda: app.camera.apply_camera(before_after))
        compare_menu.add_command(label="Difference Image", command=lambda: app.camera.apply_camera(difference_image))
        menubar.add_cascade(label="Komparasi", menu=compare_menu)

        # =====================
        # ANALISIS
        # =====================
        analysis_menu = tk.Menu(menubar, tearoff=0)
        analysis_menu.add_command(label="📊 Histogram", command=lambda: self.histogram(app))
        menubar.add_cascade(label="Analisis", menu=analysis_menu)

        # =====================
        # MANIPULASI WARNA
        # =====================
        color_menu = tk.Menu(menubar, tearoff=0)
        color_menu.add_command(label="HSV", command=lambda: app.camera.apply(to_hsv))
        color_menu.add_command(label="HSI", command=lambda: app.camera.apply(to_hsi))
        color_menu.add_command(label="YCbCr", command=lambda: app.camera.apply(to_ycbcr))
        color_menu.add_command(label="CMY / CMYK", command=lambda: app.camera.apply(to_cmyk))
        menubar.add_cascade(label="Manipulasi Warna", menu=color_menu)

        # =====================
        # CHANNEL SPLIT
        # =====================
        channel_menu = tk.Menu(menubar, tearoff=0)
        channel_menu.add_command(label="R Channel", command=lambda: app.camera.apply_rgb_channel(channel_r))
        channel_menu.add_command(label="G Channel", command=lambda: app.camera.apply_rgb_channel(channel_g))
        channel_menu.add_command(label="B Channel", command=lambda: app.camera.apply_rgb_channel(channel_b))
        menubar.add_cascade(label="Channel Split (RGB)", menu=channel_menu)

        app.config(menu=menubar)

    # =====================
    # OPEN IMAGE
    # =====================
    def open(self, app):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if path:
            app.camera.open_image(path)

    # =====================
    # COMPRESS IMAGE
    # =====================
    def compress(self, app):
        if app.camera.current_frame is None:
            messagebox.warning("Warning", "Tidak ada gambar untuk dikompres")
            return

        quality = simpledialog.askinteger(
            "Compress Image",
            "Masukkan kualitas (1–100)",
            minvalue=1,
            maxvalue=100
        )
        if quality is None:
            return

        path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg")])
        if not path:
            return

        compress_image(app.camera.current_frame, path, quality)
        size_kb = os.path.getsize(path) / 1024

        messagebox.showinfo(
            "Compress Selesai",
            f"Kualitas    : {quality}\n"
            f"Ukuran File : {size_kb:.2f} KB\n\n"
            f"Lokasi:\n{path}"
        )

    # =====================
    # HISTOGRAM
    # =====================
    def histogram(self, app):
        if app.camera.current_frame is None:
            messagebox.warning("Warning", "Tidak ada gambar untuk dianalisis")
            return

        show_histogram(app.camera.current_frame)

    # =====================
    # THEME
    # =====================
    def set_theme(self, mode):
        ctk.set_appearance_mode(mode)
