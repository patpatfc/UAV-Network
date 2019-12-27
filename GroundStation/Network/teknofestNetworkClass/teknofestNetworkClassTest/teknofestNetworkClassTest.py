from GroundStation.Network.teknofestNetworkClass.teknofestNetworkClass import API
import json

connection = API()
connection.giris("hisarcs", "teknoyz147")
f = open("final.json", "r")
result = f.read()
f.close()
data = json.loads(result)
t = 0
print(len(data))
for i in data:
    if(t > 3714):
        connection.customPost("http://212.68.57.202:52196/api/cevap_gonder", i)
    t += 1
    print(t)
