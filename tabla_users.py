import pandas
import json

userId = []
userName = []
userSurname = []
password = []

with open('secure-users.json', encoding='utf-8') as archivo:
    data = json.load(archivo)

for user in data:
    userId.append(user['userId'])
    userName.append(user['userName'])
    userSurname.append(user['userSurname'])
    password.append(user['password'])

datos = {
    'userId': userId,
    'userName': userName,
    'userSurname': userSurname,
    'password': password
}

df = pandas.DataFrame(datos)
df.to_excel('usuarios.xlsx')
