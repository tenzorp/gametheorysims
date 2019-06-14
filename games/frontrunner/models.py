from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)

import random

"""
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'frontrunner'
    players_per_group = 2
    num_rounds = 3

    instructions_template = 'frontrunner/instructions.html'
    role = random.choice([1, 2])


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.StringField(
        widget=widgets.RadioSelect)

    def choice_choices(self):
        if self.role() == 'Row':
            return ['Extreme', 'Moderate', 'Vague']
        else:
            return ['Challenge', 'Ignore', 'Praise']

    def role(self):
        if self.id_in_group == Constants.role:
            return 'Row'
        if self.id_in_group != Constants.role:
            return 'Column'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.role() == 'Column':
            payoff = {
                'Challenge':
                    {
                        'Extreme': -10,
                        'Moderate': 0,
                        'Vague': -4
                    },
                'Ignore':
                    {
                        'Extreme': 5,
                        'Moderate': -7,
                        'Vague': -3
                    },
                'Praise':
                    {
                        'Extreme': 0,
                        'Moderate': -1,
                        'Vague': -2
                    }
            }
            self.payoff = payoff[self.choice][self.other_player().choice]
        else:
            payoff = {
                'Extreme':
                    {
                        'Challenge': 10,
                        'Ignore': -5,
                        'Praise': 0
                    },
                'Moderate':
                    {
                        'Challenge': 0,
                        'Ignore': 7,
                        'Praise': 1
                    },
                'Vague':
                    {
                        'Challenge': 4,
                        'Ignore': 3,
                        'Praise': 2
                    }
            }
            self.payoff = payoff[self.choice][self.other_player().choice]
