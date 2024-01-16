class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0

    def __str__(self):
        result = self.name + ": "
        result += str(self.wins) + " wins and "
        result += str(self.losses) + " losses"
        return result

    def set_record(self, wins, losses):
        self.wins = wins
        self.losses = losses

nationals = Team("Washington National")
nationals.set_record(93,69)
print(nationals)

astros = Team("Houston Astros")
print(astros)

