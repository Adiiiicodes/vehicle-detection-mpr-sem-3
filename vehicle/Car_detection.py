import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, Label, Button, Frame

# Function to detect cars in the selected video or webcam stream
def detect_cars(video_path=None, use_webcam=False):
    # Placeholder for car detection logic
    pass  # Implement your detection logic here

# Function to handle file upload and car detection
def upload_and_detect():
    video_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=(("MP4 files", "*.mp4"), ("AVI files", "*.avi"), ("All files", "*.*"))
    )
    if video_path:
        detect_cars(video_path=video_path)
    else:
        messagebox.showwarning("Warning", "No file selected!")

# Function to handle live webcam detection
def webcam_and_detect():
    detect_cars(use_webcam=True)

# Main window setup
root = tk.Tk()
root.title("Car Detection System")

# Set window size and styling
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")
root.configure(bg="#34495e")  # Dark theme

# Define custom font
font_style = ("Arial", 14)

# Create a header label
header = Label(
    root,
    text="Car Detection System",
    fg="#ecf0f1",  # Light color for contrast
    bg="#34495e",
    font=("Arial", 24, "bold"),
)
header.pack(pady=20)

# Create a frame to hold the buttons
button_frame = Frame(root, bg="#34495e")
button_frame.pack(pady=40)

# Create buttons with styling
btn_upload = Button(
    button_frame,
    text="Upload Video",
    command=upload_and_detect,
    fg="white",
    bg="#2980b9",
    font=font_style,
    width=15,
    height=2,
    relief="raised",
    bd=3,
)
btn_upload.pack(padx=10, pady=5)

btn_webcam = Button(
    button_frame,
    text="Use Webcam",
    command=webcam_and_detect,
    fg="white",
    bg="#27ae60",
    font=font_style,
    width=15,
    height=2,
    relief="raised",
    bd=3,
)
btn_webcam.pack(padx=10, pady=5)

btn_exit = Button(
    button_frame,
    text="Exit",
    command=root.quit,
    fg="white",
    bg="#c0392b",
    font=font_style,
    width=10,
    height=2,
    relief="raised",
    bd=3,
)
btn_exit.pack(padx=10, pady=5)

# Create a label with styling
lbl = Label(
    root,
    text="Choose input method for car detection",
    fg="#ecf0f1",
    bg="#34495e",
    font=font_style,
)
lbl.pack(pady=20)

# Run the GUI loop
root.mainloop()
