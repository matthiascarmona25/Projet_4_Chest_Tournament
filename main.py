from Model.Player import Player
from Model.Tournament import Tournament

# player_01 = Player('DUPOND', 'Jean', '25/10/1997')
tournament_01 = Tournament(name='Championnat de France', place='Marseille', start_date='17/06/2023 08:30:00', end_date='17/06/2023 08:30:00', numbers_turns=12)
print(tournament_01.numbers_turns)
# print(player_01.firstname)