import simcar
import time
for i in range(10):
    simcar.forward(1,2)
    simcar.left(1,2)
    time.sleep(1)
    simcar.forward(0,2)
    simcar.left(0,2)
simcar.exit()