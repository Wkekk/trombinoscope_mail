import mysql.connector as msc

class Connexion:
    __user = "ISEN"
    __password = "ISEN"
    __host = "localhost"
    __port = "8081"
    __database = "trombinoscope"
    __cursor = None

    @classmethod
    def ouvrir(cls):
        if cls.__cursor == None:
            cls.__bdd = msc.connect(user = cls.__user, password = cls.__password, host = cls.__host, port = cls.__port, database = cls.__database)
            cls.__cursor = cls.__bdd.cursor()

    @classmethod
    def lister(cls):
        query = "SELECT id_personne, nom_personne, prenom_personne, mail_personne FROM personnes NATURAL JOIN genres NATURAL JOIN statut "
        cls.__cursor.execute(query)
        return cls.__cursor.fetchall()

    @classmethod
    def execute(cls, query):
        cls.__cursor.execute(query)
        if query.split(" ")[0] != "SELECT":
            cls.__bdd.commit()
            
        return cls.__cursor.fetchall()

    @classmethod
    def fermer(cls):
        cls.__cursor.close()
        cls.__bdd.close()
        cls.__cursor = None