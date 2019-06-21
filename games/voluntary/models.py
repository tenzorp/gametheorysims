from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)


"""
Sim for Voluntary Contribution Game.
"""


class Constants(BaseConstants):
    name_in_url = 'voluntary'
    players_per_group = 5
    num_rounds = 10

    instructions_template = 'voluntary/instructions.html'
    endowment = 50


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    group_tokens = models.IntegerField(initial=0)


class Player(BasePlayer):
    gp = models.IntegerField(min=0, max=Constants.endowment, label='Group Project')
    ip = models.IntegerField(min=0, max=Constants.endowment, label='Individual Project')

    def set_payoff(self):
        self.payoff = self.ip + (0.5 * self.group.group_tokens)
