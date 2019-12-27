"""
Bu kodda rcv yerine recvfrom kullandım belli bi amacı yok 2sini denemiş oldum
http://manpages.ubuntu.com/manpages/cosmic/man2/recv.2.html

Class for a UDP connection server/client
Since UDP does not guarantee that the msgs will be received by the client
data must be sent via one package
If a data is lost on its way a previous sent data must be used
Since the update frequency is high because of udp lost data will be quickly replaced
"""

import pickle
import socket


class UDPSocket():

    def __init__(self, server_address):
        self.headerSize = 20  # Can be changed depending on msg length
        self.buffSize = 1024  # Independent
        self.Server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print('starting up on {} port {}'.format(*server_address))
        self.Server.bind(server_address)

    def getData(self):  # No need to specify departure location of the data
        print('waiting to receive message...')
        newData = True
        self.fullData = b''
        while True:
            data, address = self.Server.recvfrom(self.buffSize)
            if newData:
                dataLen = int(data[:self.headerSize])  # From header msg len is taken
                print("first part received from {}, msg len:{}".format(address, dataLen))
                newData = False

            self.fullData += data  # As new parts of msg is received it is added to fullData
            if len(self.fullData) - self.headerSize == dataLen:  # When fullmsg len is achieved break loop
                print("full msg received")
                currentDataLen = len(self.fullData)
                self.fullData = pickle.loads(self.fullData[self.headerSize:])
                print("received data len without header: {}".format(currentDataLen))
                break

    def sendData(self, data, client):
        print('sending data...')
        data = pickle.dumps(data)  # Data is converted to bytes
        data = bytes(f"{len(data):<{self.headerSize}}",
                     'utf-8') + data  # A header is added inorder to know the len of the upcoming msg
        for i in range(int(int(data[:self.headerSize]) / self.buffSize) + 1):
            self.Server.sendto(data[1024 * (i):1024 * (i + 1)], client)
            print(data[1024 * (i):1024 * (i + 1)])
        print("data sent len: {}".format(len(data)))

    def endSocket(self):  # in case of need
        self.Server.close()
