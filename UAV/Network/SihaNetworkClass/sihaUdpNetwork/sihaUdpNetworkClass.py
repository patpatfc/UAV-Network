from UAV.Network.socketClasses.udpSocket.udpSocketClass import UDPSocket


class sihaUdpNetworkSocketClass:

    def __init__(self, sihaIpAddress):
        self.sihaUdpSocketSend = UDPSocket((sihaIpAddress, 8888))
        self.sihaUdpSocketGet = UDPSocket((sihaIpAddress, 7777))

    def sihaSendData(self, data, client):
        while True:
            self.sihaUdpSocketSend.sendData(data, client)

    def sihaReqData(self):
        while True:
            self.sihaUdpSocketGet.getData()
            self.groundStationWriteData()

    def groundStationWriteData(self):
        t = open("text.txt", "w")
        t.write(str(self.groundStationDataReqSocket.fullData))
        t.close()

    def sihaEndSendSocket(self):
        self.sihaUdpSocketSend.endSocket()

    def sihaEndGetSocket(self):
        self.sihaUdpSocketGet.endSocket()
