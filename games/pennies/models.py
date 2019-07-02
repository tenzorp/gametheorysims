from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


"""
Sim for 'Matching Pennies' game
"""


class Constants(BaseConstants):
    name_in_url = 'pennies'
    players_per_group = 2
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
