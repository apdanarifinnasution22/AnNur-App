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
        self.cap = cv2.VideoCapture(0)
        self.running = True
        self.mode = "camera"
        self.update()

        # 🔥 STATUS BAR
        self.app.update_status(source="Camera")

    def update(self):
        if self.running and self.mode == "camera":
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.current_frame = frame
                self.canvas.update_frame(frame)

                # 🔥 LIVE UPDATE STATUS
                self.app.update_status(source="Camera")

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

            # 🔥 STATUS BAR
            self.app.update_status(source="Capture")

    def reset(self):
        if self.original_frame is not None:
            self.current_frame = self.original_frame.copy()
            self.canvas.update_frame(self.current_frame)

            # 🔥 STATUS BAR
            self.app.update_status(source="Reset")

    # =====================
    # APPLY FILTER
    # =====================
    def apply(self, func):
        if self.current_frame is not None:
            self.current_frame = func(self.current_frame)
            self.canvas.update_frame(self.current_frame)

            # 🔥 STATUS BAR
            self.app.update_status(source="Processed")

    # =====================
    # APPLY CAMERA (KOMPARASI)
    # =====================
    def apply_camera(self, func):
        if self.current_frame is not None:
            if self.original_frame is None:
                self.original_frame = self.current_frame.copy()

            self.current_frame = func(self)
            self.canvas.update_frame(self.current_frame)

            # 🔥 STATUS BAR
            self.app.update_status(source="Comparison")

    # =====================
    # APPLY RGB CHANNEL
    # =====================
    def apply_rgb_channel(self, func):
        if self.original_frame is None:
            return

        rgb = self.original_frame.copy()
        channel = func(rgb)
        self.current_frame = channel
        self.canvas.update_frame(self.current_frame)

        # 🔥 STATUS BAR
        self.app.update_status(source="RGB Channel")

    # =====================
    # ROTATE IMAGE
    # =====================
    def rotate(self, angle):
        if self.current_frame is None:
            return

        if angle == 90:
            self.current_frame = cv2.rotate(
                self.current_frame,
                cv2.ROTATE_90_CLOCKWISE
            )
        elif angle == 180:
            self.current_frame = cv2.rotate(
                self.current_frame,
                cv2.ROTATE_180
            )
        elif angle == 270:
            self.current_frame = cv2.rotate(
                self.current_frame,
                cv2.ROTATE_90_COUNTERCLOCKWISE
            )

        self.canvas.update_frame(self.current_frame)

        # 🔥 STATUS BAR
        self.app.update_status(source=f"Rotate {angle}°")


    # =====================
    # FILE
    # =====================
    def open_image(self, path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.original_frame = img.copy()
        self.current_frame = img.copy()
        self.mode = "image"
        self.running = False

        self.canvas.update_frame(img)

        # 🔥 STATUS BAR
        self.app.update_status(source="File")

    def save_image(self, path):
        if self.current_frame is not None:
            cv2.imwrite(
                path,
                cv2.cvtColor(self.current_frame, cv2.COLOR_RGB2BGR)
            )
