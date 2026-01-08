import face_recognition
import os
import pickle

dataset_path = "dataset"
known_encodings = []
known_names = []

print("Training started...")

for person in os.listdir(dataset_path):
    person_dir = os.path.join(dataset_path, person)

    if not os.path.isdir(person_dir):
        continue

    for image_name in os.listdir(person_dir):
        image_path = os.path.join(person_dir, image_name)
        image = face_recognition.load_image_file(image_path)

        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(person)

data = {
    "encodings": known_encodings,
    "names": known_names
}

with open("encodings.pkl", "wb") as file:
    pickle.dump(data, file)

print("Training completed successfully")
