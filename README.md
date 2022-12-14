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
In this case, I will use images from Pexels to illustrate the examples.

### [C1] Eyebrow close to the eye: Important: C1 can be improved, but I have to extract calculations from another program. But I must rest first.
Expresses emotions.
Dreamer who shares his dreams.
Spontaneous.
Good ability to concentrate on activities.
<div style="width:100px";>
  <img src="https://user-images.githubusercontent.com/115203597/206662304-7cb7664b-4db0-48a7-a87d-ce9b5f0ab411.jpg" width="100" height="100" style="float:left;">
  <img src="https://user-images.githubusercontent.com/115203597/206662309-dc06dfed-d7c0-46c4-9b4a-a8ac93a6f9e5.jpg" width="100" height="100" style="float:left;">
  <img src="https://user-images.githubusercontent.com/115203597/206662310-1aa4e7ff-eb6a-4883-a0bc-4b5f55e2562f.jpg" width="100" height="100" style="float:left;">
  <img src="https://user-images.githubusercontent.com/115203597/206662312-681866a7-bec8-45f3-85e6-a50e3b81048b.jpg" width="100" height="100" style="float:left;">
  <img src="https://user-images.githubusercontent.com/115203597/206662316-675b23ee-8a59-44c2-bff8-d0eb543cdac8.jpg" width="100" height="100" style="float:left;">
</div>

### [C2] Eyebrow with middle distance from the eye: 
Spontaneous.
Flexible.
Balance between what he says and what he thinks.
Lacks a little tolerance.
<div style="width:100px";>
  <img src="https://i.ibb.co/P6PJtXm/0-85-rostro-2160.jpg" width="100" height="100" style="float:left;">
  <img src="https://i.ibb.co/1vFfDdk/0-8-rostro-436.jpg" width="100" height="100" style="float:left;">
  <img src="https://i.ibb.co/XZgCLwb/0-8-rostro-746.jpg" width="100" height="100" style="float:left;">
  <img src="https://i.ibb.co/4465KLR/0-82-rostro-959.jpg" width="100" height="100" style="float:left;">
  <img src="https://i.ibb.co/vHjDTPp/0-82-rostro-2086.jpg" width="100" height="100" style="float:left;">
</div>

### [C3] Eyebrow away from the eye:
Reserved person.
Introverted person.
Does not transmit much his ideas, does not tell the things he did or did not do, keeps his ideas/thoughts to himself more.
May show dispersion, reverie or distraction.

<div style="width:100px";>
  <img src="https://user-images.githubusercontent.com/115203597/206661732-9877e0d8-8cc6-44f1-815a-3bf833870477.jpg" width="100" height="100" style="float:left;">
  <img src="https://user-images.githubusercontent.com/115203597/206661738-565a938c-17d7-44d8-96d8-13a06c7729ac.jpg" width="100" height="100" style="float:left;">
  <img src="https://user-images.githubusercontent.com/115203597/206661743-9b5ac9d7-ab0c-44d2-ba81-09281df2a854.jpg" width="100" height="100" style="float:left;">
  <img src="https://user-images.githubusercontent.com/115203597/206661746-e811d1e6-6a51-4924-8eb3-ff54e1ebd47c.jpg" width="100" height="100" style="float:left;">
  <img src="https://user-images.githubusercontent.com/115203597/206661747-b4c4e6ff-2597-4f8c-8c9a-f85880ce3720.jpg" width="100" height="100" style="float:left;">
</div>

This program was created for a project called PsicoRecogn. The purpose of this project is to capture and analyze the morphopsychology of any user in order to create a detailed profile of their characteristics and provide ultra-personalization in the readings that the user makes. The project will be released gradually and the first mission is to obtain enough data to validate the usefulness of morphopsychology, as there is currently not enough data to prove it.

The programs I created for the project were designed to analyze on a massive scale.

If the PsicoRecogn project proves effective in capturing and analyzing morphopsychology, it could be used in dating applications to match people with complementary psychological profiles.
