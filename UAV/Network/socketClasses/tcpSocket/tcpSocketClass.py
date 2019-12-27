"""
Class for a TCP connection server/client
Since TCP does transfer all data without any package loss
After send and get data functions received msg can be processed w/ worry
"""

import pickle
import socket


class TCPSocket():

    def __init__(self, Server_address):
        self.headerSize = 20  # Can be changed depending on msg length
        self.buffSize = 1024  # Independent
        self.Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('starting up on {} port {}'.format(*Server_address))
        self.Server.bind(Server_address)
        """Connection must be established
        For Server listenForConnection must be called
        For Client connectToServer must be called"""

    def listenForConnection(self):
        print('waiting for conection...')
        self.Server.listen(1)  # 1 = number of que requests non is que since 1
        self.conn, self.addr = self.Server.accept()
        print('Connection address: {}'.format(self.addr))

    def connectToServer(self, ServerAddress):
        self.Server.connect(ServerAddress)
        print('Connection established w/: {}'.format(ServerAddress))

    def sendData(self, data):
        print('sending data...')
        data = pickle.dumps(data)  # Data is converted to bytes
        data = bytes(f"{len(data):<{self.headerSize}}",
                     'utf-8') + data  # A header is added inorder to know the len of the upcoming msg
        self.conn.send(data)
        print("data sent len: {}".format(len(data)))

    def getData(self):
        print('waiting to receive message...')
        self.fullData = b''
        newData = True
        while True:
            data = self.Server.recv(self.buffSize)  # Receive buffSize len of bytes not the whole msg
            if newData:
                dataLen = int(data[:self.headerSize])  # From header msg len is taken
                print("new msg len:", data[:self.headerSize])
                newData = False
            self.fullData += data  # As new parts of msg is received it is added to fullData

            if len(self.fullData) - self.headerSize == dataLen:  # When fullmsg len is achieved break loop
                print("full msg received")
                self.fullData = pickle.loads(self.fullData[self.headerSize:])
                print("received data len without header: {}".format(len(self.fullData)))
                break

    def closeConnectionServer(self):  # Connection can be brokendown via only server
        self.conn.close()

    def endSocket(self):  # in case of need
        self.Server.close()
