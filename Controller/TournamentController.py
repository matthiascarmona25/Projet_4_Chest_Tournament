from Model.Tournament import Tournament
from View.TournamentView import TournamentView

class TournamentController():

    def create(self):
        create_view = TournamentView()
        create_view = create_view.createView()
        tournament_01 = Tournament(
            name=create_view['name'],
            place=create_view['place'],
            start_date=create_view['start_date'],
            end_date=create_view['end_date'],
            description=create_view['description'],
            numbers_turns=create_view['numbers_turn']
        )
        return tournament_01.__dict__
