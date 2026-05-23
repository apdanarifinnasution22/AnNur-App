import cv2
import numpy as np

def compress_image(image, path, quality):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    cv2.imwrite(
        path,
        cv2.cvtColor(image, cv2.COLOR_RGB2BGR),
        encode_param
    )


def compress_preview(image, quality):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    success, encoded = cv2.imencode(
        ".jpg",
        cv2.cvtColor(image, cv2.COLOR_RGB2BGR),
        encode_param
    )

    if not success:
        return image

    decoded = cv2.imdecode(encoded, cv2.IMREAD_COLOR)
    return cv2.cvtColor(decoded, cv2.COLOR_BGR2RGB)
