# In the name of God

import os
import time
from picamera2 import Picamera2


# Settings Logs and Path for save Images
LOG_PATH = "data/camera/"
CAMERA_FILE_NAME = "capture.jpg"

picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)

def capture():
    """Take a picture with OV5647 camera and save it."""
    os.makedirs(LOG_PATH, exist_ok=True)

    timestamp = time.strftime("%Y-%m-%d_%-%M-%S")
    file_path = os.path.join(LOG_PATH, f"{timestamp}_{CAMERA_FILE_NAME}")

    picam2.start()
    time.sleep(2)
    picam2.capture_file(file_path)
    picam2.stop()

    print(f"Image captured and saved to {file_path}")
    return file_path

