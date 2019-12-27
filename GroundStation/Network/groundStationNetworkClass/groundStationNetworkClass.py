from GroundStation.Network.socketClasses.udpSocket.udpSocketClass import UDPSocket
from GroundStation.Network.teknofestNetworkClass.teknofestNetworkClass import API


class GroundStationSocketsClass():

    def __init__(self, GroundStationIPAddress):
        self.groundStationDataReqSocket = UDPSocket((GroundStationIPAddress, 8888))
        self.groundStationDataPubSocket = UDPSocket((GroundStationIPAddress, 7777))
        self.TeknofestNetworkObj = API()  # buna ayri methodlar define etmelimiyim emin değilim kodu çok karıştırabilir

    def grounStationReqData(self):
        while True:
            self.groundStationDataReqSocket.getData()
            self.groundStationWriteData()

    def groundStationWriteData(self):
        t = open("text.txt", "w")
        t.write(str(self.groundStationDataReqSocket.fullData))
        t.close()

    def grounStationSendData(self, data, client):
        while True:
            self.groundStationDataPubSocket.sendData(data, client)

    def grounStationEndReqSocket(self):
        self.groundStationDataReqSocket.endSocket()

    def grounStationEndSendSocket(self):
        self.groundStationDataPubSocket.endSocket()
