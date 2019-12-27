from Network.socketClasses.tcpSocket.tcpSocketClass import TCPSocket

server = TCPSocket(('localhost', 4444))
server.listenForConnection()
server.sendData(open("testData.txt", "r").read())
server.closeConnectionServer()
