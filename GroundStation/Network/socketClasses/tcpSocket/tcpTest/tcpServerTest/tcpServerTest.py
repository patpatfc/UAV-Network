from GroundStation.Network.socketClasses.tcpSocket.tcpSocketClass import TCPSocket

server = TCPSocket(("192.168.1.101", 6666))
server.listenForConnection()

for i in range(1001):
    server.sendData(i)
server.closeConnectionServer()
server.endSocket()
