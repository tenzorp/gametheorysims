from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)


"""
Sim for Voluntary Contributions with Punishment game - code pulled from first VC game
"""


class Constants(BaseConstants):
    name_in_url = 'punishment'
    players_per_group = None
    num_rounds = 10

    instructions_template = 'punishment/instructions.html'


class Subsession(BaseSubsession):

    def creating_session(self):
        group_matrix = []
        players = self.get_players()
        ppg = self.session.config['players_per_group']
        for i in range(0, len(players), ppg):
            group_matrix.append(players[i:i + ppg])
        self.set_group_matrix(group_matrix)


class Group(BaseGroup):
    group_project = models.CurrencyField()


class Player(BasePlayer):
    contribution = models.CurrencyField()
    deductions = models.IntegerField()

    def contribution_max(self):
        return self.session.config['endowment']

