from PIL import Image, ImageTk
import customtkinter as ctk
import numpy as np
import cv2


class CanvasView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#2b2b2b")

        self.label = ctk.CTkLabel(self, text="")
        self.label.pack(expand=True, fill="both", padx=10, pady=10)

        self.photo = None

    def update_frame(self, frame):
        if frame is None:
            return

        # =====================
        # HANDLE GRAYSCALE
        # =====================
        if len(frame.shape) == 2:
            frame = np.stack((frame,) * 3, axis=-1)

        # =====================
        # ADD BORDER (FINISHING UI)
        # =====================
        frame = cv2.copyMakeBorder(
            frame,
            5, 5, 5, 5,
            cv2.BORDER_CONSTANT,
            value=(80, 80, 80)  # abu-abu gelap
        )

        # =====================
        # CONVERT TO IMAGE
        # =====================
        image = Image.fromarray(frame)

        self.photo = ImageTk.PhotoImage(image)
        self.label.configure(image=self.photo)
        self.label.image = self.photo  # prevent garbage collection
