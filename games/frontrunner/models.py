from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
import random

"""
Sim for 'Frontrunner - Challenger' game. Players are matched randomly and must choose a political platform or reaction
to their opponent's political platform.
"""


class Constants(BaseConstants):
    name_in_url = 'frontrunner'
    players_per_group = 2
    num_rounds = 5

    instructions_template = 'frontrunner/instructions.html'
    role = random.choice([1, 2])


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
        else:
            self.group_like_round(1)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.StringField(widget=widgets.RadioSelect, label='')

    def choice_choices(self):
        if self.role() == 'Row':
            return ['Extreme', 'Moderate', 'Vague']
        else:
            return ['Challenge', 'Ignore', 'Praise']

    def role(self):
        if self.id_in_group == Constants.role:
            return 'Row'
        else:
            return 'Column'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff = {
            'Extreme':
                {
                    'Challenge': [10, -10],
                    'Ignore': [-5, 5],
                    'Praise': [0, 0]
                },
            'Moderate':
                {
                    'Challenge': [0, 0],
                    'Ignore': [7, -7],
                    'Praise': [1, -1]
                },
            'Vague':
                {
                    'Challenge': [4, -4],
                    'Ignore': [3, -3],
                    'Praise': [2, -2]
                }
        }
        i = 0 if self.role() == 'Row' else 1
        self.payoff = payoff[self.group.get_player_by_role('Row').choice][self.group.get_player_by_role('Column').choice][i]
