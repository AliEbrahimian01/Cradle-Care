# In the name of God

import time
from sensors import dht22


while True:
    dht22.log()
    time.sleep(30)
