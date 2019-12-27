from GroundStation.Network.socketClasses.tcpSocket.tcpSocketClass import TCPSocket


class sihaTcpNetworkSocketClass:

    def __init__(self, clientAddress, serverAddress):
        self.sihaTcpSocketSend = TCPSocket(clientAddress)
        self.sihaTcpSocketGet = TCPSocket(serverAddress)

    def sihaDataPublish(self, data):
        self.sihaTcpSocketSend.sendData(data)

    def sihaDataSubscribe(self):
        self.sihaTcpSocketGet.getData()

    def buildSihaGroundStationConnection(self, groundStationIp):
        self.sihaUdpSocketSend.connectToServer(groundStationIp)

    def closeSihaGroundStationIpSend(self):
        self.sihaTcpSocketSend.endSocket()

    def closeSihaGroundStationIpGet(self):
        self.sihaTcpSocketGet.endSocket()
