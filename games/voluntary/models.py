from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


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
    pass


class Player(BasePlayer):
    pass
