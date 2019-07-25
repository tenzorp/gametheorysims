from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
import random

"""
Sim for O'Neill game.
"""


class Constants(BaseConstants):
    name_in_url = 'oneill'
    players_per_group = 2
    num_rounds = 5

    instructions_template = 'oneill/instructions.html'
    role = random.choice([1, 2])


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.StringField(
        choices=['Joker', 'Ace', 'Two', 'Three'],
        widget=widgets.RadioSelect,
        label="Please choose your card.")

    def role(self):
        if self.id_in_group == Constants.role:
            return 'Row'
        else:
            return 'Column'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.role() == 'Row':
            payoff = {
                'Joker':
                    {
                        'Joker': 5,
                        'Ace': -5,
                        'Two': -5,
                        'Three': -5
                    },
                'Ace':
                    {
                        'Joker': -5,
                        'Ace': -5,
                        'Two': 5,
                        'Three': 5
                    },
                'Two':
                    {
                        'Joker': -5,
                        'Ace': 5,
                        'Two': -5,
                        'Three': 5
                    },
                'Three':
                    {
                        'Joker': -5,
                        'Ace': 5,
                        'Two': 5,
                        'Three': -5
                    }
            }
            self.payoff = payoff[self.choice][self.other_player().choice]
        else:
            payoff = {
                'Joker':
                    {
                        'Joker': -5,
                        'Ace': 5,
                        'Two': 5,
                        'Three': 5
                    },
                'Ace':
                    {
                        'Joker': 5,
                        'Ace': 5,
                        'Two': -5,
                        'Three': -5
                    },
                'Two':
                    {
                        'Joker': 5,
                        'Ace': -5,
                        'Two': 5,
                        'Three': -5
                    },
                'Three':
                    {
                        'Joker': 5,
                        'Ace': -5,
                        'Two': -5,
                        'Three': 5
                    }
            }
            self.payoff = payoff[self.choice][self.other_player().choice]
