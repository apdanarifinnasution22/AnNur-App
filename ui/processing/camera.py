import cv2

class Camera:
    def __init__(self, canvas, app):
        self.canvas = canvas
        self.app = app
        self.cap = cv2.VideoCapture(1)
        self.running = False
        self.mode = "camera"

        self.original_frame = None
        self.current_frame = None

    # =====================
    # CAMERA CONTROL
    # =====================
    def start(self):
        self.cap = cv2.VideoCapture(0)  # 🔥 WAJIB buka ulang kamera
        self.running = True
        self.mode = "camera"
        self.update()


    def update(self):
        if self.running and self.mode == "camera":
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.current_frame = frame
                self.canvas.update_frame(frame)

            self.app.after(33, self.update)

    def stop(self):
        self.running = False
        if self.cap.isOpened():
            self.cap.release()
    # =====================
    # IMAGE STATE
    # =====================
    def capture(self):
        if self.current_frame is not None:
            self.running = False
            self.mode = "image"
            self.original_frame = self.current_frame.copy()

    def reset(self):
        if self.original_frame is not None:
            self.current_frame = self.original_frame.copy()
            self.canvas.update_frame(self.current_frame)

    # =====================
    # APPLY FILTER (NORMAL)
    # =====================
    def apply(self, func):
        if self.current_frame is not None:
            self.current_frame = func(self.current_frame)
            self.canvas.update_frame(self.current_frame)

    # =====================
    # APPLY CAMERA (KOMPARASI)
    # =====================
    def apply_camera(self, func):
        if self.current_frame is not None:

            # 🔥 SIMPAN GAMBAR ASLI PERTAMA KALI
            if self.original_frame is None:
                self.original_frame = self.current_frame.copy()

            self.current_frame = func(self)
            self.canvas.update_frame(self.current_frame)

    # =====================
    # 🔥 APPLY RGB CHANNEL (PENTING)
    # =====================
    def apply_rgb_channel(self, func):
        """
        Channel R/G/B HARUS dari RGB asli,
        bukan dari HSV / HSI / YCbCr / CMYK
        """
        if self.original_frame is None:
            return

        rgb = self.original_frame.copy()
        channel = func(rgb)
        self.current_frame = channel
        self.canvas.update_frame(self.current_frame)

    # =====================
    # FILE
    # =====================
    def open_image(self, path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.original_frame = img.copy()
        self.current_frame = img.copy()
        self.mode = "image"     # ✅ PENTING
        self.running = False    # ✅ HENTIKAN CAMERA

        self.canvas.update_frame(img)


    def save_image(self, path):
        if self.current_frame is not None:
            cv2.imwrite(
                path,
                cv2.cvtColor(self.current_frame, cv2.COLOR_RGB2BGR)
            )
