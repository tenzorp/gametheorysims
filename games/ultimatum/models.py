from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)
import random

"""
Sim for Ultimatum/Two-Stage Bargaining Game
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'ultimatum/instructions.html'
    role = random.choice([1, 2])


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def role(self):
        if self.id_in_group == Constants.role:
            return 'proposer'
        else:
            return 'responder'

    def other_player(self):
        return self.get_others_in_group()[0]
