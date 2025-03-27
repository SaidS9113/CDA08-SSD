# Liste des freelances
freelances = [
    {"prenom": "Alice", "nom": "Durand", "email": "alice@example.com"},
    {"prenom": "Hugo", "nom": "Leroy", "email": "hugo@example.com"}
]


with open("freelances.xml", "w", encoding="utf-8") as fichier:

    fichier.write("<freelances>\n")
    
   
    for freelance in freelances:
        fichier.write("  <freelance>\n") 

      
        fichier.write(f"    <prenom>{freelance['prenom']}</prenom>\n")
        fichier.write(f"    <nom>{freelance['nom']}</nom>\n")
        fichier.write(f"    <email>{freelance['email']}</email>\n")
        
        fichier.write("  </freelance>\n")  
    fichier.write("</freelances>") 
