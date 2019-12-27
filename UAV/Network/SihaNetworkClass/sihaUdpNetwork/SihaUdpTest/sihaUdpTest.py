import threading

from UAV.Network.SihaNetworkClass.sihaUdpNetwork.sihaUdpNetworkClass import sihaUdpNetworkSocketClass

sihaUdpSockets = sihaUdpNetworkSocketClass("192.168.1.108")
dataReqThread = threading.Thread(target=sihaUdpSockets.sihaReqData)
dataSendThread = threading.Thread(target=sihaUdpSockets.sihaSendData, args=(10707, ("192.168.1.101", 8888)))

dataReqThread.start()
dataSendThread.start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        sihaUdpNetworkSocketClass.sihaEndGetSocket()
        sihaUdpNetworkSocketClass.sihaEndSendSocket()
        break
