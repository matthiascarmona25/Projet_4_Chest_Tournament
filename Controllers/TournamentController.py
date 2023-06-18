from Models.Tournament import Tournament
from Views.TournamentView import TournamentView


class TournamentController:
    def createTournament(self):
        create_view = TournamentView()
        create_view = create_view.getInfoTournament()
        tournament_01 = Tournament(
            name=create_view['name'],
            place=create_view['place'],
            start_date=create_view['start_date'],
            end_date=create_view['end_date'],
            description=create_view['description'],
            # numbers_turns=create_view['numbers_turn']
        )
        if create_view['numbers_turn'] != '':
            tournament_01.numbers_turns = create_view['numbers_turn']

        return tournament_01
