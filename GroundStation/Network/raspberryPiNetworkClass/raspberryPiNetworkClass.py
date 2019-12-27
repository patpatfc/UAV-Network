"""
Udp kullanılacak ve sadece data alımı yapılacak
"""
from GroundStation.Network.socketClasses.udpSocket.udpSocketClass import UDPSocket


class raspberryPiDataRequest():

    def __init__(self, clientIP):
        self.RasPiUdpSocket = UDPSocket((clientIP, 10000))

    def rasPiReqData(self):
        while True:
            self.RasPiUdpSocket.getData()
            self.groundStationWriteData()

    def groundStationWriteData(self):
        t = open("text.txt", "w")
        t.write(str(self.groundStationDataReqSocket.fullData))
        t.close()

    def rasPiEndSocket(self):
        self.RasPiUdpSocket.endSocket()
