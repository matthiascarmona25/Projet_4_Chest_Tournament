
class PlayerView:
    def getInfoPlayer(self):
        lastname = input('Quel est le nom du joueur : ')
        firstname = input('Quel est le prénom du joueur : ')
        birth_date = input('Quel est votre date de naissance : ')
        ine = input('Quel est votre identifiant national d\'échec (format : AB1234) : ')

        info_player = {
            'lastname': lastname,
            'firstname': firstname,
            'birth_date': birth_date,
            'ine': ine
        }

        return info_player