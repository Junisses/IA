# 🖐️ Control de Volumen y Navegador con Gestos de la Mano

Este proyecto permite **controlar el volumen del sistema** y **abrir el navegador Microsoft Edge** mediante **gestos de la mano** detectados por la cámara web, utilizando `OpenCV`, `MediaPipe` y `pycaw`.

---

## 📷 Funcionalidades

- 🔊 **Control de volumen**: Junta o separa el pulgar e índice para bajar o subir el volumen del sistema.
- 🌐 **Apertura del navegador**: Detecta la mano completamente abierta y abre automáticamente Microsoft Edge con Google.

---

## 🛠️ Tecnologías Usadas

- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/) – Procesamiento de imágenes y cámara.
- [MediaPipe](https://google.github.io/mediapipe/) – Detección de manos.
- [pycaw](https://github.com/AndreMiras/pycaw) – Control de volumen en Windows.
- Otros: `numpy`, `math`, `comtypes`, `subprocess`, `time`

---

## 🧩 Instalación

1. Clona este repositorio:
   
    ```git clone https://[github.com/tuusuario/tu-repo.git](https://github.com/Junisses/IA)```

   ```cd tu-repo```
   
3. (Opcional) Crea y activa un entorno virtual:
   
    ```python -m venv venv```
   
    ```venv\Scripts\activate```

5. Instala las dependencias:
   
    ```pip install opencv-python mediapipe pycaw comtypes numpy```

## ▶️ Cómo Ejecutar
1. Asegúrate de tener una cámara web conectada.
   
2. Ejecuta el script para verificar la camara:
   
   ```python camara.py```
   
### Iniciar control por gestos
1. Ejecutamos el archivo principal:
   
   ```python volumen.py```
   
2. Interactúa con la cámara:
   
    🤏 Junta pulgar e índice → volumen bajo.
   
    ✌️ Sepáralos → volumen alto.
   
    🖐️ Mano completamente abierta → se abre Edge con Google.

4. Presiona q para salir del programa.

--- 

## Detalles Técnicos
- Se detectan 21 landmarks de la mano usando MediaPipe.
- La distancia entre los dedos controla el volumen con pycaw.
- Una mano completamente abierta (todos los dedos separados) lanza Microsoft Edge en modo ventana.

### ❗ Notas
- Este proyecto es compatible solo con Windows (por pycaw).
- Requiere buena iluminación para un reconocimiento preciso.
- Si tienes varias cámaras, ajusta el índice de cv2.VideoCapture().
- Asegúrate de tener Microsoft Edge instalado en tu sistema para abrir el navegador correctamente.
- Aún falta perfeccionamiento de la función para subir y bajar el volumen.
