from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)


"""
Sim for "Beauty Contest" game. Each player guesses a number from 0 to 100, up to 3 decimal places.
After all guesses are submitted, the winner is the player whose guess was closest to 2/3 of
the value of the average guess.
"""


class Constants(BaseConstants):
    name_in_url = 'beauty'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'beautyContest/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    winning = models.FloatField()


class Player(BasePlayer):
    guess = models.FloatField(min=0, label='')
    winner = models.BooleanField()

    def guess_max(self):
        return self.session.config['endowment']

    def guess_error_message(self, value):
        if str(value)[::-1].find('.') > 3:
            return 'Up to 3 decimal places are allowed'
