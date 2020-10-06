import face_recognition


def get_faces_from_image(unknown):
    unknown_picture = face_recognition.load_image_file(unknown)
    return face_recognition.face_encodings(unknown_picture)


def is_identified(known, unknown):
    picture_of_me = face_recognition.load_image_file(known)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    results = face_recognition.compare_faces([my_face_encoding], unknown)

    if results[0]:
        return True
    else:
        return False
