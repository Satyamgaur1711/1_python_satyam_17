
import csv
import os
from datetime import datetime

import cv2
import face_recognition
import numpy as np

KNOWN_DIR = "known_faces"
ATTENDANCE_FILE = "attendance.csv"
TOLERANCE = 0.5  # kam = zyada strict (0.4-0.6 try karein)


def load_known_faces():
    encodings, names = [], []
    for file in os.listdir(KNOWN_DIR):
        if not file.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        image = face_recognition.load_image_file(os.path.join(KNOWN_DIR, file))
        faces = face_recognition.face_encodings(image)
        if not faces:
            print(f"[WARNING] {file} mein face nahi mila, skip kiya.")
            continue
        encodings.append(faces[0])
        names.append(os.path.splitext(file)[0])
    print(f"[INFO] {len(names)} students load hue.")
    return encodings, names


def load_marked_today():
    """Aaj jin ki attendance lag chuki hai unka set return karta hai."""
    today = datetime.now().strftime("%Y-%m-%d")
    marked = set()
    if os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, newline="") as f:
            for row in csv.reader(f):
                if len(row) >= 2 and row[1] == today:
                    marked.add(row[0])
    return marked


def mark_attendance(name):
    now = datetime.now()
    new_file = not os.path.exists(ATTENDANCE_FILE)
    with open(ATTENDANCE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["Name", "Date", "Time"])
        writer.writerow([name, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")])
    print(f"[ATTENDANCE] {name} present - {now.strftime('%H:%M:%S')}")


def main():
    known_encodings, known_names = load_known_faces()
    if not known_encodings:
        print("known_faces folder mein photos daaliye.")
        return

    marked_today = load_marked_today()
    cap = cv2.VideoCapture(0)

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        # Speed ke liye frame chhota karte hain
        small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small = np.ascontiguousarray(small[:, :, ::-1])

        locations = face_recognition.face_locations(rgb_small)
        encodings = face_recognition.face_encodings(rgb_small, locations)

        for (top, right, bottom, left), enc in zip(locations, encodings):
            distances = face_recognition.face_distance(known_encodings, enc)
            best = int(np.argmin(distances))
            name = "Unknown"

            if distances[best] <= TOLERANCE:
                name = known_names[best]
                if name not in marked_today:
                    mark_attendance(name)
                    marked_today.add(name)

            # Box wapas original size mein
            top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4
            color = (0, 200, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        cv2.imshow("Attendance System (q = quit)", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()