# PsicoRecogn_classify_eyebrow_spacing
The program allows to detect and classify eyebrow-to-eye distances in three categories: near, medium and far. With exceptional accuracy, the program saves the worked images in separate folders according to their classification and provides a document describing the personality trait associated with each folder of faces.

## Installation: tested in python 3.10.0 | Windows 10

- pip install mediapipe==0.8.11

- pip install opencv-python==4.6.0.66


The present program is designed to scan a folder of face images with a size of 500px x 500px. To generate these 500x500px size images, it is recommended to use any of these tools:
- https://github.com/TITIR1X/capture_face_live

- https://github.com/TITIR1X/large_scale_face_capturer

If you choose to use "large_scale_face_capturer", you need to correct the angles of the captured faces with the following program:

- https://github.com/TITIR1X/profile_angles_of_captured_faces

## Brief description of the analyzed faces
### "[C1], [C2], [C3]" Represents the name of the folder where it stores the faces with the detected features.

### [C1] Eyebrow close to the eye:
Expresses emotions.
Dreamer who shares his dreams.
Spontaneous.
Good ability to concentrate on activities.

### [C2] Eyebrow with middle distance from the eye:
Spontaneous.
Flexible.
Balance between what he says and what he thinks.
Lacks a little tolerance.
![0 85_rostro_2160](https://user-images.githubusercontent.com/115203597/206658393-d117d1ee-d971-4723-92a4-ad35ba788d02.jpg=50x50)
![0 8_rostro_436](https://user-images.githubusercontent.com/115203597/206658399-bccb2337-5bc1-4490-a3dc-3a3ce3c8e354.jpg=50x50)
![0 8_rostro_746](https://user-images.githubusercontent.com/115203597/206658402-9638999f-4e90-403e-abb3-42beacd9605c.jpg=50x50)
![0 82_rostro_959](https://user-images.githubusercontent.com/115203597/206658406-0cc28be4-78e2-4198-b70a-2abe4408ba21.jpg=50x50)
![0 82_rostro_2086](https://user-images.githubusercontent.com/115203597/206658410-71fea970-0c0b-4653-a9b9-d88b4acc5e0d.jpg=50x50)


### [C3] Eyebrow away from the eye:
Reserved person.
Introverted person.
Does not transmit much his ideas, does not tell the things he did or did not do, keeps his ideas/thoughts to himself more.
May show dispersion, reverie or distraction.
