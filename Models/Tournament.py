class Tournament(object):
    list_turns = []
    list_players = []
    actually_turn = 0

    def __init__(self, name, place, start_date, end_date, description, numbers_turns=4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.numbers_turns = numbers_turns
        self.description = description
