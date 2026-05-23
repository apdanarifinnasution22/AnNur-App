import cv2
import numpy as np


def draw_label(img, text):
    img = img.copy()
    cv2.rectangle(img, (0, 0), (img.shape[1], 40), (0, 0, 0), -1)
    cv2.putText(
        img,
        text,
        (10, 28),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )
    return img


def before_after(camera):
    if camera.original_frame is None:
        return camera.current_frame
    """
    Tampilkan BEFORE dan AFTER berdampingan
    """
    if camera.original_frame is None or camera.current_frame is None:
        return camera.current_frame

    before = camera.original_frame.copy()
    after = camera.current_frame.copy()

    if before.shape != after.shape:
        after = cv2.resize(after, (before.shape[1], before.shape[0]))

    if len(before.shape) == 2:
        before = cv2.cvtColor(before, cv2.COLOR_GRAY2RGB)
    if len(after.shape) == 2:
        after = cv2.cvtColor(after, cv2.COLOR_GRAY2RGB)

    before = draw_label(before, "BEFORE")
    after = draw_label(after, "AFTER")

    return np.hstack((before, after))


def difference_image(camera):
    return camera.current_frame
    """
    Hitung selisih absolut antara BEFORE dan AFTER
    """
    if camera.original_frame is None or camera.current_frame is None:
        return camera.current_frame

    before = camera.original_frame.copy()
    after = camera.current_frame.copy()

    if before.shape != after.shape:
        after = cv2.resize(after, (before.shape[1], before.shape[0]))

    if len(before.shape) == 3:
        before = cv2.cvtColor(before, cv2.COLOR_RGB2GRAY)
    if len(after.shape) == 3:
        after = cv2.cvtColor(after, cv2.COLOR_RGB2GRAY)

    diff = cv2.absdiff(before, after)
    return diff
