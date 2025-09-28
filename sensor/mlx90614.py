# In the name of God

import os
import time
import board
import busio
import adafruit_mlx90614

# Define Sensor
i2c = busio.I2C(board.SCL, board.SDA, frequency=100_000)
mlx = adafruit_mlx90614.MLX90614(i2c)

# Log configuration
LOG_PATH = "data/mlx90614/"
MLX_FILE_NAME_LOGS = "mlx90614.csv"
MLX_HEADER_LOG = "Date, Time, AmbientTemp, ObjectTemp\r\n"

def read():
    """Save read data from MLX90614 sensor. Returns(ambbient_temp, object_temp) or (None , None)"""
    try:
        ambient_temp = mlx.ambient_temperature
        object_temp = mlx.object_temperature
        return ambient_temp, object_temp
    except Exception as err:
        print(f"MLX90614 failed: {err}")
        return None, None


def log():
    """Save read data from MLX90614 in `mlx90614`."""
    ambient_temp, object_temp = read()

    # If no data exist, don't save.
    if ambient_temp is None or object_temp is None:
        return False

    # Ensure log directory exists
    os.makedirs(LOG_PATH, exist_ok=True)

    file_path = os.path.join(LOG_PATH, MLX_FILE_NAME_LOGS)
    file_exist = os.path.isfile(file_path)

    with open(file_path, "a+") as f:
        if not file_exist or os.stat(file_path).st_size == 0:
            f.write(MLX_HEADER_LOG)

        Date = time.strftime("%Y-%m-%d")
        Time = time.strftime("%H:%M:%S")
        f.write(f"{Date}, {Time}, {ambient_temp:.2f}, {object_temp:.2f}\r\n")
        print(f"Logged MLX90614: Amient={ambient_temp:.1f}°C - object={object_temp:.1f}°C")
        return True

