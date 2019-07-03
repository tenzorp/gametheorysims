from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)

"""
Sim for 11-20 game
"""


class Constants(BaseConstants):
    name_in_url = 'eleven'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'eleven/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    request = models.CurrencyField(min=11, max=20, label='Please enter an amount from 11 to 20.')

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.request == self.other_player().request - 1:
            self.payoff = self.request + c(20)
        else:
            self.payoff = self.request
