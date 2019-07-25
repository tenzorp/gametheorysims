from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
import random

"""
Sim for 'Matching Pennies' game
"""


class Constants(BaseConstants):
    name_in_url = 'pennies'
    players_per_group = 2
    num_rounds = 12

    instructions_template = 'pennies/instructions.html'
    role = random.choice([1, 2])  # randomly choose 'Row' player


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
            for p in self.get_players():
                p.participant.vars['total'] = 0
        else:
            if self.round_number % 4 == 1:
                self.group_randomly()
            else:
                self.group_like_round(self.round_number - 1)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.StringField(
        choices=['Heads', 'Tails'],
        widget=widgets.RadioSelect,
        label="Please make your choice."
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def role(self):
        return 'Row' if self.id_in_group == Constants.role else 'Column'

    def set_payoff(self):
        if self.choice == 'Heads' and self.other_player().choice == 'Heads':
            if self.role() == 'Column':
                self.payoff = 0
            else:  # Row
                if self.round_number == 1:
                    self.payoff = 1
                elif self.round_number == 2:
                    self.payoff = 9
                else:
                    self.payoff = 0.5
        else:
            payoff = {
                'Heads': {'Tails': [0, 1]},
                'Tails': {
                    'Tails': [1, 0],
                    'Heads': [0, 1]
                }
            }
            r = 0 if self.role() == 'Row' else 1  # position of payoff in list
            self.payoff = payoff[self.group.get_player_by_role('Row').choice][self.group.get_player_by_role('Column').choice][r]
