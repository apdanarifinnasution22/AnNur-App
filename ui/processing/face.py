import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def to_gray(img):
    if len(img.shape) == 3:
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img

def detect_face(img):
    gray = to_gray(img)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    result = img.copy()
    for x,y,w,h in faces:
        cv2.rectangle(result, (x,y), (x+w,y+h), (255,0,0), 2)
    return result, faces

def auto_crop_face(img):
    gray = to_gray(img)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces)==0:
        return img
    x,y,w,h = max(faces, key=lambda f:f[2]*f[3])
    return img[y:y+h, x:x+w]
