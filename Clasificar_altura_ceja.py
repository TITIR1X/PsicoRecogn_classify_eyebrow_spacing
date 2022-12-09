import cv2
import os
import shutil
import webbrowser
from collections import Counter
import operator
import numpy as np

from mediapipe import solutions as mp

try:
 os.system('color 6')
 os.system('cls')
except:os.system('clear')

print("""
 ./Clasificar_altura_ceja.py
  ____              _______ _   ______ _       ___ __    __
 |  _ \            /__   __(_)/__   __(_) _ __|_| |\ \\  / /
 | |_) |_   _         | |   _    | |   _ | '__| | | \ \\/ /
 |  _ <| | | |        | | 0| |   | |  | || |    | |  \  \\
 | |_) | |_| |        | | /| |   | |  | || |    | | / /\ \\
 |____/ \__, |        |_| /|_|   |_|  |_||_|    |_|/_/  \_\\
         __/ |                                               
        |___/                           
""")


mp_face_mesh = mp.face_mesh
mp_drawing = mp.drawing_utils

# Para evitar errores en el path de la carpeta con las imágenes
def parse_path(imagesPath):
    imagesPath = imagesPath.replace("\\", '/')
    imagesPath = imagesPath.replace('"', '')
    imagesPath = imagesPath.replace('\'', '')
    imagesPath = imagesPath.replace('& ', '')
    return imagesPath

# Se pregunta al usuario por la carpeta con las imágenes
imagesPath = input('Arrastre la carpeta con rostros a capturar: ')
imagesPath = parse_path(imagesPath)

# Se crea la carpeta de salida si no existe
carpeta_salida = 'Clasificado_de_altura_cejas'
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

# Se crean las subcarpetas para clasificar las imágenes en diferentes alturas de cejas
subcarpetas = ['C1', 'C1-C2', 'C2',
           'C3', 'Otros']
for subcarpeta in subcarpetas:
    try:
        os.makedirs(os.path.join(carpeta_salida, subcarpeta))
    except FileExistsError:pass

# Lista de índices para localizar los puntos de interés en las imágenes
index_list=[70,63,105,66,107,  46,53,52,65,55,  130,247,29,27,28,190,243,   244]

# Se carga el clasificador de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
confianza = 0.1

# Se recorren todas las imágenes de la carpeta
imagesPathList = os.listdir(imagesPath)

for count, imageName in enumerate(imagesPathList):
    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=1,
        min_detection_confidence=confianza) as face_mesh:

        # Se leen las imágenes
        image = cv2.imread(os.path.join(imagesPath, imageName))
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        height, width, _ = image.shape

        # Se procesan las imágenes con la solución de face_mesh de MediaPipe
        result = face_mesh.process(image_rgb)
       
        # Si se detecta al menos un rostro en la imagen
        if result.multi_face_landmarks is not None:
            font = cv2.FONT_HERSHEY_SIMPLEX
            
            for face_landmarks in result.multi_face_landmarks:
                # Se dibujan los puntos de interés en la imagen
                for index in index_list:
                    x = int(face_landmarks.landmark[index].x * width)
                    y = int(face_landmarks.landmark[index].y * height)

                    cv2.circle(image, (x, y), 1, (0, 0, 255), 1)
                    cv2.putText(image, f'{index}', (x,y), font, 0.3, (26, 127, 239),1, cv2.LINE_AA)

                    # Obtener coordenadas de los puntos de interés:
                    # Ceja izquierda superior
                    x_70 = int(face_landmarks.landmark[70].x * width)
                    y_70 = int(face_landmarks.landmark[70].y * height)
                    y_63 = int(face_landmarks.landmark[63].y * height)
                    y_105 = int(face_landmarks.landmark[105].y * height)
                    y_66 = int(face_landmarks.landmark[66].y * height)
                    y_107 = int(face_landmarks.landmark[107].y * height)

                    # Ceja inferior
                    y_46 = int(face_landmarks.landmark[46].y * height)
                    y_53 = int(face_landmarks.landmark[53].y * height)
                    x_52 = int(face_landmarks.landmark[52].x * width)
                    y_52 = int(face_landmarks.landmark[52].y * height)
                    y_65 = int(face_landmarks.landmark[65].y * height)
                    y_55 = int(face_landmarks.landmark[55].y * height)

                    # Ojos
                    y_130 = int(face_landmarks.landmark[130].y * height)
                    x_130 = int(face_landmarks.landmark[130].x * width)
                    y_247 = int(face_landmarks.landmark[247].y * height)
                    y_29 = int(face_landmarks.landmark[29].y * height)
                    x_27 = int(face_landmarks.landmark[27].x * width)
                    y_27 = int(face_landmarks.landmark[27].y * height)
                    y_28 = int(face_landmarks.landmark[28].y * height)
                    y_190 = int(face_landmarks.landmark[190].y * height)
                    x_243 = int(face_landmarks.landmark[243].x * width)
                    x_244 = int(face_landmarks.landmark[244].x * width)

                    cv2.line(image, (x_130, 0), (x_130, 500), (0, 0, 255  ), 1)
                    cv2.line(image, (0, y_27), (500, y_27), (0, 0, 255  ), 1)
                    cv2.line(image, (x_243, 0), (x_243, 500), (0, 0, 255  ), 1)

                    # Secuencia Fibonacci 4 distancias [(13,21), (34), (55)] [bajas, medias, altas]
                    cv2.line(image, (65, y_27-0), (250, y_27-0), (0, 0, 255), 1)
                    cv2.putText(image, '0', (65-5,y_27-0), font, 0.3, (0, 0, 255),1, cv2.LINE_AA)
                    # 13, 21
                    cv2.line(image, (65, y_27-13), (250, y_27-13), (26, 127, 239), 1)
                    cv2.putText(image, '13', (65-5,y_27-13), font, 0.3, (26, 127, 239),1, cv2.LINE_AA)
                    cv2.line(image, (65, y_27-21), (250, y_27-21), (26, 127, 239), 1)
                    cv2.putText(image, '21', (65-5,y_27-21), font, 0.3, (26, 127, 239),1, cv2.LINE_AA)
                    # 34
                    cv2.line(image, (65, y_27-34), (250, y_27-34), (26, 127, 239), 1)
                    cv2.putText(image, '34', (65-5,y_27-34), font, 0.3, (26, 127, 239),1, cv2.LINE_AA)
                    # 55
                    cv2.line(image, (65, y_27-55), (250, y_27-55), (26, 127, 239), 1)
                    cv2.putText(image, '55', (65-5,y_27-55), font, 0.3, (26, 127, 239),1, cv2.LINE_AA)

            print(f'\n\n[{count + 1} de {len(imagesPathList)}] {imagesPathList[count]}\n')
            # desc_altura: cejas bajas
            if y_52 >= (y_27-13) or y_65 >= (y_27-13) or y_52 >= (y_27-13) and y_65 >= (y_27-13):
                cv2.line(image, (65, y_27-0), (250, y_27-0), (33, 255, 0), 1)
                cv2.putText(image, '0', (65-5,y_27-0), font, 0.3, (33, 255, 0),1, cv2.LINE_AA)
                cv2.line(image, (65, y_27-13), (250, y_27-13), (33, 255, 0), 1)
                cv2.putText(image, '13', (65-5,y_27-13), font, 0.3, (33, 255, 0),1, cv2.LINE_AA)

                resultado = (f'{carpeta_salida}/C1/{imagesPathList[count]}')

                cv2.imwrite(resultado, image)
                print(f'    -> {carpeta_salida}/C1')

            # desc_altura: cejas bajas
            elif y_52 >= (y_27-21) or y_65 >= (y_27-21) or y_52 >= (y_27-21) and y_65 >= (y_27-21):
                cv2.line(image, (65, y_27-13), (250, y_27-13), (33, 255, 0), 1)
                cv2.putText(image, '13', (65-5,y_27-13), font, 0.3, (33, 255, 0),1, cv2.LINE_AA)
                cv2.line(image, (65, y_27-21), (250, y_27-21), (33, 255, 0), 1)
                cv2.putText(image, '21', (65-5,y_27-21), font, 0.3, (33, 255, 0),1, cv2.LINE_AA)
    
                resultado = (f'{carpeta_salida}/C1-C2/{imagesPathList[count]}')

                cv2.imwrite(resultado,image)
                print(f'    -> {carpeta_salida}/C1-C2')
                
    
            # desc_altura: cejas altura media al ojo
            elif y_52 >= (y_27-34) or y_65 >= (y_27-34) or y_52 >= (y_27-34) and y_65 >= (y_27-34):
                cv2.line(image, (65, y_27-21), (250, y_27-21), (33, 255, 0), 1)
                cv2.putText(image, '21', (65-5,y_27-21), font, 0.3, (33, 255, 0),1, cv2.LINE_AA)
                cv2.line(image, (65, y_27-34), (250, y_27-34), (33, 255, 0), 1)
                cv2.putText(image, '34', (65-5,y_27-34), font, 0.3, (33, 255, 0),1, cv2.LINE_AA)

                resultado = (f'{carpeta_salida}/C2/{imagesPathList[count]}')
        
                cv2.imwrite(resultado,image)
                print(f'    -> {carpeta_salida}/C2')
                    
            # desc_altura: cejas lejos del ojo
            elif y_52 >= (y_27-55) or y_65 >= (y_27-55) or y_52 >= (y_27-55) and y_65 >= (y_27-55):
                cv2.line(image, (65, y_27-34), (250, y_27-34), (33, 255, 0), 1)
                cv2.putText(image, '34', (65-5,y_27-34), font, 0.3, (33, 255, 0),1, cv2.LINE_AA)
                cv2.line(image, (65, y_27-55), (250, y_27-55), (33, 255, 0), 1)
                cv2.putText(image, '55', (65-5,y_27-55), font, 0.3, (33, 255, 0),1, cv2.LINE_AA)

                resultado = (f'{carpeta_salida}/C3/{imagesPathList[count]}')

                cv2.imwrite(resultado,image)
                print(f'    -> {carpeta_salida}/C3')

            else:
                resultado = (f'{carpeta_salida}/Otros/{imagesPathList[count]}')
                cv2.imwrite(f'{carpeta_salida}/Otros/{imagesPathList[count]}',image)
                
            count+= 1
            
        else:
            count += 1

webbrowser.open(os.path.realpath(carpeta_salida))

print('clasificar_altura_ceja.py: Programa finalizado.')
exit()
