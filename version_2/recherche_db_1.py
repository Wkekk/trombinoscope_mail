from connexion import Connexion
from apprenant import apprenant

# Fonction de requête SQL
def requete_sql(nom_colonne, prenom_colonne, genre_colonne, statut_colonne, photo_path):
    # Connection à la db
    Connexion.ouvrir()

    query = "SELECT nom_personne, prenom_personne, genre, qualification_statut, mail_personne, photo_personne FROM personnes NATURAL JOIN genres NATURAL JOIN statut WHERE " + nom_colonne + prenom_colonne + genre_colonne + statut_colonne + ";"

    resultat = []
    cnt = 0

    for enregistrement in Connexion.execute(query) :
        resultat.append(apprenant(enregistrement[0], enregistrement[1], enregistrement[2], enregistrement[3], enregistrement[4], photo_path+enregistrement[5]))
        cnt += 1
    
    Connexion.fermer()

    return resultat