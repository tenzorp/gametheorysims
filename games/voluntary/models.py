from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)


"""
Sim for Voluntary Contribution Game.
"""


class Constants(BaseConstants):
    name_in_url = 'voluntary'
    players_per_group = None
    num_rounds = 10

    instructions_template = 'voluntary/instructions.html'
    endowment = 50


class Subsession(BaseSubsession):

    def creating_session(self):
        group_matrix = []
        players = self.get_players()
        ppg = self.session.config['players_per_group']
        for i in range(0, len(players), ppg):
            group_matrix.append(players[i:i+ppg])
        self.set_group_matrix(group_matrix)


class Group(BaseGroup):
    group_tokens = models.IntegerField(initial=0)


class Player(BasePlayer):
    gp = models.IntegerField(min=0, max=Constants.endowment, label='Group Project')

    def set_payoff(self):
        ip = 50 - self.gp
        self.payoff = ip + (0.5 * self.group.group_tokens)
