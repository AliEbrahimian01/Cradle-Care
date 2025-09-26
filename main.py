# In the name of God

import time
from sensor import dht22

def main():
    while True:
        dht22.log()
        #mlx90614.log()
        time.sleep(30)



if __name__ == "__main__":
    main()
