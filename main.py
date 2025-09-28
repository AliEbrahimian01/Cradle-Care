# In the name of God

import time
from sensor import dht22, camera, mlx90614

def main():
    while True:
        dht22.log()
        camera.capture()
        mlx90614.log()
        time.sleep(5)



if __name__ == "__main__":
    main()
