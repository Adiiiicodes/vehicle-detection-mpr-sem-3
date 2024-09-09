import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, Label, Button

# Function to detect cars in the selected video
def detect_cars(video_path):
    car_cascade = cv2.CascadeClassifier('D:\\New folder\\Car_Detection_System\\vehicle\\cars.xml')
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frames = cap.read()

        if not ret or frames is None:
            print("Video has ended or failed to capture image")
            break

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 9)

        for (x, y, w, h) in cars:
            cv2.rectangle(frames, (x, y), (x + w, y + h), (51, 51, 255), 2)
            cv2.rectangle(frames, (x, y - 40), (x + w, y), (51, 51, 255), -2)
            cv2.putText(frames, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        frames = cv2.resize(frames, (600, 400))
        cv2.imshow('Car Detection System', frames)

        k = cv2.waitKey(30) & 0xff
        if k == 27:  # Esc key to stop
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to handle file upload and car detection
def upload_and_detect():
    video_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=(("MP4 files", "*.mp4"), ("AVI files", "*.avi"), ("All files", "*.*"))
    )
    
    if video_path:
        detect_cars(video_path)
    else:
        messagebox.showwarning("Warning", "No file selected!")

# Function to toggle full-screen mode
def toggle_fullscreen(event=None):
    state = not root.attributes('-fullscreen')
    root.attributes('-fullscreen', state)
    if state:
        center_widgets()
    else:
        reset_layout()

# Function to center widgets in full-screen mode
def center_widgets():
    lbl.pack_forget()  # Remove default layout
    btn_upload.pack_forget()  # Remove default layout
    btn_exit.pack_forget()  # Remove default layout

    lbl.place(relx=0.5, rely=0.45, anchor='center')  # Adjusted lower
    btn_upload.place(relx=0.5, rely=0.55, anchor='center')  # Adjusted lower
    btn_exit.place(relx=0.5, rely=0.65, anchor='center')  # Adjusted lower

# Function to reset the layout when exiting full-screen mode
def reset_layout():
    lbl.place_forget()  # Remove custom layout
    btn_upload.place_forget()  # Remove custom layout
    btn_exit.place_forget()  # Remove custom layout

    lbl.pack(pady=10)
    btn_upload.pack(pady=10)
    btn_exit.pack(pady=10)

# Main window setup
root = tk.Tk()
root.title("Car Detection System")
root.geometry("300x150")
root.configure(bg="#2c3e50")

# Bind the F11 key to toggle full-screen mode
root.bind('<F11>', toggle_fullscreen)

# GUI components
lbl = Label(root, text="Upload a video to detect cars", fg="white", bg="#2c3e50", font=("Helvetica", 14))
lbl.pack(pady=10)

btn_upload = Button(root, text="Upload Video", command=upload_and_detect, fg="white", bg="#3498db", font=("Helvetica", 12))
btn_upload.pack(pady=10)

btn_exit = Button(root, text="Exit", command=root.quit, fg="white", bg="#e74c3c", font=("Helvetica", 12))
btn_exit.pack(pady=10)

# Run the GUI loop
root.mainloop()
