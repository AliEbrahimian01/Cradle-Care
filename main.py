# In the name of God

import time
from sensor import dht22


while True:
    dht22.log()
    time.sleep(30)



if __name__ == "__main__":
    main()
