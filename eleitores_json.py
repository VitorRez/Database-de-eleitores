import json

eleitor = {
    "nome":["Vitor","jorge","lucas","mateus","arthur"],
    "chave-pub":[0,1,2,3,4],
    "cpf":["12373075628","12345678900","23456789001","34567890012","45678900123"]
}

def readDB(filename="eleitores.json"):

    with open(filename, mode="r") as jsonFile:
        data = json.load(jsonFile)
    return data


def writeDB(obj, filename="eleitores.json"):

    with open(filename, mode="r") as jsonFile:
        data = json.load(jsonFile)
        temp = data["nome"]
        for i in obj["nome"]:
            if i not in temp:
                temp.append(i)
        temp1 = data["chave-pub"]
        for i in obj["chave-pub"]:
            if i not in temp1:
                temp1.append(i)
        temp2 = data["cpf"]
        for i in obj["cpf"]:
            if i not in temp2:
                temp2.append(i)

    with open(filename, mode="w") as jsonFile:
        json.dump(data, jsonFile)

writeDB(obj = eleitor)
data = readDB()
print(data)
