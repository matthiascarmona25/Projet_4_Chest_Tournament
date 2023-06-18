from Models.Tournament import Tournament


class Tour(Tournament):
    def __init__(self, name, start_datetime, end_datetime):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime