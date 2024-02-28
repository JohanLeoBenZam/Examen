import json

with open('secure-users.json') as archivo:
    data = json.load(archivo)

libreriasId = []
for user in data:
    for books in user["books"]:
        repetido = False
        for x in libreriasId:
            if x == books['libraryId']:
                repetido = True
                break
        if not repetido:
            libreriasId.append(books['libraryId'])
book = []

librerias = []
for x in libreriasId:
    libreria = {
        'libraryId': x,
        'books': []
    }

    librerias.append(libreria)

for user in data:
    for books in user["books"]:
        for x in range(0,len(libreriasId),1):
            if libreriasId[x] == books['libraryId']:
                book ={
                    'bookId': books['bookId'],
                    'bookTitle': books['bookTitle'],
                    'bookEditorial': books['bookEditorial'],
                    'bookPublication': books['bookPublication'],
                }
                librerias[x]['books'].append(book)

with open('libreria.json', 'w') as archivo:
    json.dump(librerias, archivo, indent=4, ensure_ascii= False)







