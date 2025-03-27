import csv


freelances = [
    {"prenom": "Alice", "nom": "Durand", "email": "alice@example.com"},
    {"prenom": "Hugo", "nom": "Leroy", "email": "hugo@example.com"}
]


with open("freelances.csv", "a", newline="") as f:
   
    fieldnames = ["prenom", "nom", "email"]
    
  
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    
    if f.tell() == 0:
        writer.writeheader()
    
 
    for freelance in freelances:
        writer.writerow(freelance)
