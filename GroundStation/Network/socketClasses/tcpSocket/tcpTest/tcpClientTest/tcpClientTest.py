from GroundStation.Network.socketClasses.tcpSocket.tcpSocketClass import TCPSocket

client = TCPSocket(('192.168.1.2', 5555))
client.connectToServer(('192.168.1.5', 4444))
client.getData()
f = open("transferedData.txt", "w+")
f.write(client.fullData)
f.close()
server = TCPSocket(('192.168.1.2', 5556))
server.listenForConnection()
server.sendData("Hi mi amigo!")
server.closeConnectionServer()
client.endSocket()
server.endSocket()
