import yaml


freelances = [
    {"prenom": "Alice", "nom": "Durand", "email": "alice@example.com"},
    {"prenom": "Hugo", "nom": "Leroy", "email": "hugo@example.com"}
]

with open("freelances.yaml", "w", encoding="utf-8") as fichier:


    yaml.dump(freelances, fichier, default_flow_style=False, allow_unicode=True)
