import json
import hashlib

hasher = hashlib.sha256()

with open('users.json') as archivo:
    data = json.load(archivo)

for x in range(0, len(data), 1):
    hasher.update(data[x]["password"].encode('utf-8'))
    data[x]["password"] = hasher.hexdigest()

with open("secure-users.json", 'w') as archivo:
    archivo.write(json.dumps(data, ensure_ascii= False, indent= 4))
