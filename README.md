# Vehicle Detection System

## Overview

The **Vehicle Detection System** is a computer vision-based application designed to detect vehicles in both video files and live webcam feeds. It utilizes OpenCV's Haar Cascade Classifier, which has been trained specifically for vehicle detection. This system provides a user-friendly graphical interface developed using the Tkinter library, allowing users to upload videos or use their webcam for real-time vehicle detection.

## Features

- **Vehicle Detection**: Detects vehicles in video files or live webcam streams.
- **Graphical User Interface (GUI)**: Intuitive interface with options to upload videos or switch to webcam mode.
- **Customizable**: Adjust detection parameters as needed for different scenarios.
- **Cross-Platform**: Compatible with any platform that supports Python and OpenCV.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Dependencies](#dependencies)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Git**: Optional, for cloning the repository.

### Steps

1. **Clone the Repository** (Optional)

   ```bash
   git clone https://github.com/yourusername/vehicle-detection-mpr-sem-3.git
   cd vehicle-detection-mpr-sem-3
   ```

2. **Install Dependencies**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

   Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If `requirements.txt` is not available, manually install the following packages:*

   ```bash
   pip install opencv-python-headless opencv-contrib-python-headless numpy tk
   ```

3. **Download the Haar Cascade XML File**

   The project uses a pre-trained Haar Cascade XML file named `cars.xml`. Ensure this file is placed in the correct directory (`Car_Detection_System/cars.xml`). If missing, you can obtain it from OpenCV's GitHub repository or other trusted sources.

   ```bash
   wget -O Car_Detection_System/cars.xml https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_cars.xml
   ```

   *Note: Replace the URL if a different Haar Cascade is used.*

## Usage

### Running the Application

Navigate to the project directory and execute the main script:

```bash
python Car_Detection_System/Car_detection.py
```

Upon launching, a GUI window titled **"Car Detection System"** will appear, offering the following options:

1. **Upload Video**:
   - Click the "Upload Video" button.
   - Select an MP4 or AVI video file from your local storage.
   - The system will process the video, detecting vehicles and displaying bounding boxes around them.

2. **Use Webcam**:
   - Click the "Use Webcam" button.
   - Your webcam will activate, and the system will perform real-time vehicle detection.
   - Press 'q' or close the window to stop the webcam feed.

3. **Exit**:
   - Click the "Exit" button to close the application.

### Example Commands

- **Using a Specific Video File**:

  ```bash
  python Car_Detection_System/Car_detection.py --video_path path/to/your/video.mp4
  ```

- **Using Webcam**:

  ```bash
  python Car_Detection_System/Car_detection.py --use_webcam
  ```

*Note: Command-line arguments are optional and primarily intended for advanced usage.*

## Project Structure

```
vehicle-detection-mpr-sem-3/
├── Car_Detection_System/
│   ├── Car_detection.py          # Main application script
│   ├── cars.xml                  # Haar Cascade XML for vehicle detection
│   └── README.md                 # Detailed documentation for the subsystem
├── README.md                     # Main project documentation
└── requirements.txt              # List of Python dependencies (optional)
```

### Key Files

- **`Car_detection.py`**: Contains the main logic for vehicle detection, including video processing and GUI setup.
- **`cars.xml`**: Pre-trained Haar Cascade classifier for detecting vehicles.
- **`README.md`**: Comprehensive documentation guiding users through installation, usage, and customization.

## Dependencies

- **OpenCV**: For image processing and object detection.
- **Tkinter**: For creating the graphical user interface.
- **NumPy**: For numerical operations (used internally by OpenCV).

Ensure all dependencies are installed via `pip` as outlined in the [Installation](#installation) section.

## Contributing

We welcome contributions from the community! Whether it's improving the detection accuracy, enhancing the user interface, or adding new features, your input is valuable.

### How to Contribute

1. **Fork the Repository**: Create a fork of this project on GitHub.
2. **Clone Your Fork**: Clone your forked repository to your local machine.
3. **Create a Branch**: Make your changes in a new branch.
4. **Commit Changes**: Commit your changes with clear and concise messages.
5. **Push and Pull Request**: Push your changes to your fork and submit a pull request detailing your enhancements.

### Guidelines

- **Code Quality**: Follow PEP 8 guidelines for Python code.
- **Documentation**: Update documentation accordingly when introducing new features.
- **Testing**: Ensure that existing functionalities remain unaffected.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## Additional Information

### Understanding Haar Cascades

Haar Cascades are machine learning-based approaches where a cascade function is trained from a lot of positive and negative images. They are widely used for object detection tasks, such as face and vehicle detection.

- **Training Custom Cascades**: If you wish to train your own Haar Cascade for improved accuracy or to detect different objects, refer to OpenCV's official documentation on training cascades.

### Enhancements and Future Work

- **Improved Detection Models**: Explore using more advanced models like YOLO or SSD for better accuracy and performance.
- **Additional Features**: Implement features like vehicle tracking, speed estimation, or classification into different vehicle types.
- **User Interface Improvements**: Enhance the GUI with more interactive elements and settings.

---

Feel free to reach out or open issues on the repository if you encounter any problems or have suggestions for improvements!

