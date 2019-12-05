import face_recognition
import base64
from PIL import Image
import io

def isIdent(known, unknown):

        convertBase64ToFile(known, "knownImg.jpeg")
        convertBase64ToFile(unknown, "unknownImg.jpeg")

        picture_of_me = face_recognition.load_image_file("/home/denis/Documents/templates/knownImg.jpeg") #"/home/denis/Documents/face-rec/DenisMartynov.jpg"
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

        unknown_picture = face_recognition.load_image_file("/home/denis/Documents/templates/unknownImg.jpeg") #"/home/denis/Documents/face-rec/Unknown.jpg"
        face_recognition.load_image_file
        
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

        if results[0] == True:
            return True
        else:
            return False

def convertBase64ToFile(base64Str, imgName):
    image = base64.b64decode(str(base64Str))       

    imagePath = ('/home/denis/Documents/templates/' + imgName)
    img = Image.open(io.BytesIO(image))
    img.save(imagePath, 'jpeg')
    