import cv2
import os

name = input("Enter your name: ").strip()
dataset_path = "dataset"
person_path = os.path.join(dataset_path, name)

if not os.path.exists(person_path):
    os.makedirs(person_path)

camera = cv2.VideoCapture(0)
count = 0

print("Press 'C' to capture image, 'Q' to quit")

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to open camera")
        break

    cv2.imshow("Capture Faces", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        count += 1
        img_path = os.path.join(person_path, f"{count}.jpg")
        cv2.imwrite(img_path, frame)
        print(f"Image {count} saved")

    elif key == ord('q'):
        break

    if count >= 25:
        print("Image capture completed")
        break

camera.release()
cv2.destroyAllWindows()
