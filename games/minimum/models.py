from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)


"""
Sim for "Minimum Effort Game"
"""


class Constants(BaseConstants):
    name_in_url = 'minimum'
    players_per_group = 5
    num_rounds = 3

    instructions_template = 'minimum/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    min = models.IntegerField()


class Player(BasePlayer):
    effort = models.IntegerField(min=1, max=5)

    def set_payoff(self):
        self.payoff = 5 * self.group.min - self.effort
