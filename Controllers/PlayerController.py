from Models.Player import Player
from Views.PlayerView import PlayerView

class PlayerController:

    def createPlayer(self):
        player_view = PlayerView()
        player_view = player_view.getInfoPlayer()
        player = Player(
            lastname=player_view['lastname'],
            firstname=player_view['firstname'],
            birth_date=player_view['birth_date'],
            ine=player_view['ine']
        )

        return player

