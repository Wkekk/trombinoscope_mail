from connexion import Connexion

# connexion à la base de données
Connexion.ouvrir()

# Création de la colonne mail_personne
try:
    query = "ALTER TABLE personnes ADD COLUMN mail_personne VARCHAR(255) AFTER prenom_personne;"
    Connexion.execute(query)
except:
    print("La colonne existe déjà ! ")

# Listage des personnes présentes dans la table personnes
liste_mail = open("adresses.txt", 'r').readlines()

liste_personne = []
for i in liste_mail:
    # Décomposition de l'e-mail pour récupération du nom et prenom
    composant = i.split("@")[0]
    prenom, nom = composant.split(".")

    # Commande query pour récupérer l'id correspondant au nom et prenom dans la BDD
    selection = f"SELECT id_personne FROM personnes WHERE prenom_personne = '{prenom}' AND nom_personne = '{nom.replace('-', ' ')}'"
    # print(f"\n {selection} \n") # Affichage de la commande
    id = Connexion.execute(selection) # Récupération de l'id

    # Commande pour update la l'e-mail sur la BDD
    query = f"UPDATE personnes SET mail_personne = '{i}' WHERE id_personne = {id[0][0]};"
    # print(f"\n {query} \n") # Affichage de la commande
    Connexion.execute(query)
    
print("-----------------------------")
print("Requête réalisé !")
print("-----------------------------")

Connexion.fermer()