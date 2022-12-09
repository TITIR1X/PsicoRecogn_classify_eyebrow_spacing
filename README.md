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
<div style="width:100px;">
  <img src="https://i.ibb.co/P6PJtXm/0-85-rostro-2160.jpg" style="float:left;">
  <img src="https://i.ibb.co/1vFfDdk/0-8-rostro-436.jpg" style="float:left;">
  <img src="https://i.ibb.co/XZgCLwb/0-8-rostro-746.jpg" style="float:left;">
  <img src="https://i.ibb.co/4465KLR/0-82-rostro-959.jpg" style="float:left;">
  <img src="https://i.ibb.co/vHjDTPp/0-82-rostro-2086.jpg" style="float:left;">
</div>

### [C3] Eyebrow away from the eye:
Reserved person.
Introverted person.
Does not transmit much his ideas, does not tell the things he did or did not do, keeps his ideas/thoughts to himself more.
May show dispersion, reverie or distraction.
