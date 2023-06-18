

class TournamentView:

    def getInfoTournament(self):
        name = input('Veuillez saisir le nom du tournoi : ')
        place = input('Ou se déroule le tournoi : ')
        start_date = input('Quand le tournoi commence-t-il : ')
        end_date = input('Quand le tournoi se termine-t-il : ')
        description = input('Description complémentaire : ')
        numbers_turn = input('En combien de tour se déroulera le tournoi : ')

        dict_response = {
            'name': name,
            'place': place,
            'start_date': start_date,
            'end_date': end_date,
            'description': description,
            'numbers_turn': numbers_turn
        }

        return dict_response
