from Network.socketClasses.tcpSocket.tcpSocketClass import TCPSocket

client = TCPSocket(('localhost', 5555))
client.connectToServer(('localhost', 4444))
client.getData()
f = open("transferedData.txt", "w+")
f.write(client.fullData)
f.close()
