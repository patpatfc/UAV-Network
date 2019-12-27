import threading

from GroundStation.Network.groundStationNetworkClass.groundStationNetworkClass import GroundStationSocketsClass

GrounStationNetwork = GroundStationSocketsClass("192.168.1.101")

dataReqThread = threading.Thread(target=GrounStationNetwork.grounStationReqData)
dataSendToRasPiThread = threading.Thread(target=GrounStationNetwork.grounStationSendData,
                                         args=(4321, ("192.168.1.108", 10000)))
dataSendToSihaThread = threading.Thread(target=GrounStationNetwork.grounStationSendData,
                                        args=(1234, ("192.168.1.108", 7777)))

dataReqThread.start()
dataSendToRasPiThread.start()
dataSendToSihaThread.start()

while 1:
    try:
        pass
    except KeyboardInterrupt:
        GrounStationNetwork.grounStationEndReqSocket()
        GrounStationNetwork.grounStationEndSendSocket()
        break
