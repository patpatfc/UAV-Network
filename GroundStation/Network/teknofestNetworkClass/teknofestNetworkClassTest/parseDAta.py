import json

#result = json.loads("B23072019_V1_K1.json")
f = open("T190619_V4_K1.json", "r")
result = f.read()
f.close()
result = json.loads(result)
tosend = []
print(len(result))
for i in range(len(result)):
    if i % 2 == 0:
        tosend.append(result[i])

with open("T190619_V4_K1_final.json", "w") as f:
    json.dump(tosend, f)