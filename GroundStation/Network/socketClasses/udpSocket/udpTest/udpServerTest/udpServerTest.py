from Network.socketClasses.udpSocket.udpSocketClass import UDPSocket

server = UDPSocket(('localhost', 4444))
server.sendData(open("testData.txt", "r").read(), ('localhost', 5555))
