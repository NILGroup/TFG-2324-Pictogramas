import json

with open('arasaac.json') as f:
    data = json.load(f)

headers = {
    'accept': 'application/octet-stream',
}

params = {
    'download': 'true',
}

for doc in data:
    fileName = "/mnt/host/pictogramTags/" + str(doc.get('_id')) + ".txt"
    tags = doc.get('tags')
    aux = ", ".join(tags)
    aux = "pictogram, " + aux
    with open(fileName, "w") as out:
        out.write(aux)