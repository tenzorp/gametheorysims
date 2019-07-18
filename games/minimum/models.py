from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)


"""
Sim for "Minimum Effort Game"
"""


class Constants(BaseConstants):
    name_in_url = 'minimum'
    players_per_group = None
    num_rounds = 10

    instructions_template = 'minimum/instructions.html'


class Subsession(BaseSubsession):

    def creating_session(self):
        group_matrix = []
        players = self.get_players()
        ppg = self.session.config['players_per_group']
        for i in range(0, len(players), ppg):
            group_matrix.append(players[i:i+ppg])
        self.set_group_matrix(group_matrix)
        self.group_randomly()


class Group(BaseGroup):
    min = models.IntegerField()


class Player(BasePlayer):
    effort = models.IntegerField(min=1, max=5)

    def set_payoff(self):
        self.payoff = 5 * self.group.min - self.effort
