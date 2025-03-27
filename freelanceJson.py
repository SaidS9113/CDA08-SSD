import json


with open('freelances.json', 'r') as file:
    data = json.load(file)


for freelance in data:
    print(freelance["prenom"], freelance["email"])
