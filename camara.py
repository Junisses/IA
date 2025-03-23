import cv2

webcam = cv2.VideoCapture(1)

if not webcam.isOpened():
    print("No se pudo abrir la cámara.")
else:
    print("La cámara está funcionando correctamente.")
    webcam.release()
