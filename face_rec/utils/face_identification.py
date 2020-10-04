import face_recognition


def isIdent(known, unknown):

    picture_of_me = face_recognition.load_image_file(known)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    unknown_picture = face_recognition.load_image_file(unknown)

    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

    if results[0]:
        return True
    else:
        return False
