import cv2

# Ensure the correct path to the Haar Cascade XML file
car_cascade = cv2.CascadeClassifier('cars.xml')

# Open video file or capture device
cap = cv2.VideoCapture('vb1.mp4')  # or replace with 0 for webcam

while True:
    ret, frames = cap.read()

    # Check if frame capture was successful or if the video has ended
    if not ret or frames is None:
        print("Video has ended or failed to capture image")
        break  # Exit loop

    # Convert to grayscale
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # Detect cars
    cars = car_cascade.detectMultiScale(gray, 1.1, 9)

    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (51, 51, 255), 2)
        cv2.rectangle(frames, (x, y - 40), (x + w, y), (51, 51, 255), -2)
        cv2.putText(frames, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Resize and display the frame
    frames = cv2.resize(frames, (600, 400))
    cv2.imshow('Car Detection System', frames)

    # Break the loop if 'Esc' key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

