from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)


"""
Sim for "Beauty Contest" game. Each player guesses a number from 0 to 100, up to 3 decimal places.
After all guesses are submitted, the winner is the player whose guess was closest to 2/3 of
the value of the average guess.
"""


class Constants(BaseConstants):
    name_in_url = 'beauty'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'beautycontest/instructions.html'




class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess = models.IntegerField()