import threading
from GroundStation.Network.raspberryPiNetworkClass.raspberryPiNetworkClass import raspberryPiDataRequest

raspiSocket = raspberryPiDataRequest("192.168.1.108")
dataReqThread = threading.Thread(target=raspiSocket.rasPiReqData)

dataReqThread.start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        raspiSocket.rasPiEndSocket()
        break
