# UAV Network  

![Network diagram](https://github.com/patpatfc/UAV-Network/blob/master/images/UAVNetworkDiagram.jpeg)

Every UAV entering the competition  is going to be in the air at the same time and compete with each other during the competition. Each UAV will target another and try to lock-on over image. The Goal of the competition is to lock on the opponent UAVs successfully as much as possible and avoid being locked on by performing aggressive maneuvers.

## Semantics

UAV transfers data collected such as location, camera feed, speed, and acceleration via the UDP socket to the ground station. At the same time ground station will receive data from the Teknofest servers about other UAVs, Ground station will perform operations on these data and produce a path for the UAV to follow and send it back to the UAV. Then ground station will send the data received from our UAv to Teknofest servers and the location data to the Raspberry Pi which will be tracking the UAV in order to maintain a stable connection and data transfer. This process will repeat over time.

Except the connection between ground station and Teknofest server all the connetions are established via the UDP sockets, its fast data transfer process exceeds the data loss possiblity in importance since there will a new data arriving every second. The connection with Teknofest servers are based upon RESTfull API that's why UDP socket is not used.

## Syntax & Sturcutre

socketClasses folder forms the basis of the project, it includes 3 different socket types in case team decided to change the sockets. All of these sockets libraries consists of initializing a socket, sending data, and receiving data. All sockets have a test file to make sure they are working. These socket libraries form  more complex elements such as groundStationNetworkClass where one or more sockets form the library including thier more spesific functions like send groundStationSendData. These folders include once again a test case, if all of the test codes are run at the same time and changed to the appropriate IP adress they will be able to send data to each other.
