class apprenant :
	"classe décrivant un.e apprenant.e"

	def __init__(self, nom, prenom, genre, statut, mail, photo) :
		self.nom = nom
		self.prenom = prenom
		self.mail = mail
		self.photo = photo
		self.genre = genre
		self.statut  = statut

	def get_info(self) :
		return self.nom, self.prenom, self.mail, self.photo, self.genre, self.statut