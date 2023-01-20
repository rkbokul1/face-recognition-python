import face_recognition

known_image = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
Known_face_encoding = face_recognition.face_encodings(known_image)[0]

unknown_image = face_recognition.load_image_file('./img/unknown/d-trump.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces
results = face_recognition.compare_faces(
    [Known_face_encoding], unknown_face_encoding)

print(results)

if results[0]:
    print('This is Bill Gates')
else:
    print('This is NOT Bill Gates')