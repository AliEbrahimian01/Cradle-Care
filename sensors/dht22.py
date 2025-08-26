# In the name of God
import os
import time
import board
import adafruit_dht


# Define Sensore
DHT_PIN = board.D17
dht_device = adafruit_dht.DHT22(DHT_PIN)


LOG_PATH = "logs/sensors/"
DHT22_FILE_NAME_LOGS = "dht_log.csv"
DHT22_HEADER_LOG = "Date, Time, Temperature , Humidity\r\n"


def read():
    """Reade data from DHT22 sensor. Returns (humidity, temperature) or (None, None)."""
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        return humidity, temperature
    except RuntimeError as err:
        print(f"Sensor error: {err}")
        return None, None
    except Exception as err:
        print(f"DHT22 failed: {err}")
        return None, None

def log():
    f"""Save read data from DHT22 in '{DHT22_FILE_NAME_LOGS}'."""

    humidity, temperature = read()

    # If no data exist, don't save.
    if humidity is None or temperature is None:
        return False

    # Cheking is exist log directory
    os.makedirs(LOG_PATH, exist_ok=True)

    file_path = os.path.join(LOG_PATH, DHT22_FILE_NAME_LOGS)
    file_exist = os.path.isfile(file_path)

    with open(file_path, "a+") as f:
        if not file_exist or os.stat(file_path).st_size == 0:
            f.write(DHT22_HEADER_LOG)

        Date = time.strftime("%Y-%m-%d")
        Time = time.strftime("%H:%M:%S")
        f.write(f"{Date}, {Time}, {temperature:.2f}, {humidity:.2f}\r\n")

    
    print(f"Logged DHT22: Temp={temperature:.1f}°C - Hum={humidity:.1f}%")
    return True
