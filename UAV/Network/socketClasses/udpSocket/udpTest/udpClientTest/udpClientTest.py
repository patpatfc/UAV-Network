from Network.socketClasses.udpSocket.udpSocketClass import UDPSocket

client = UDPSocket(('localhost', 5555))
client.getData()
f = open("transferedData.txt", "w+")
f.write(client.fullData)
f.close()
