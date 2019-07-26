from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
from random import choice
"""
Sim for Repeated Normal Form game
"""


class Constants(BaseConstants):
    name_in_url = 'normalForm'
    players_per_group = 2
    num_rounds = 50

    instructions_template = 'normalForm/instructions.html'
    role = choice([1, 2])


class Subsession(BaseSubsession):
    end_round = models.BooleanField()

    def creating_session(self):
        self.end_round = True if self.round_number == self.session.config['number_of_rounds'] else False


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.StringField(widget=widgets.RadioSelect, label='Please make your choice.')

    def choice_choices(self):
        return ['One', 'Two'] if self.role() == 'Row' else ['Aay', 'Bee']

    def role(self):
        return 'Row' if self.id_in_group == Constants.role else 'Column'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff = {
            'One': {
                'Aay': [6, 2],
                'Bee': [3, 5]
            },
            'Two': {
                'Aay': [3, 5],
                'Bee': [5, 3]
            }
        }
        i = 0 if self.role() == 'Row' else 1
        self.payoff = payoff[self.group.get_player_by_role('Row').choice][self.group.get_player_by_role('Column').choice][i]

    def table_body(self):
        my_choices = [p.choice for p in self.in_all_rounds()]
        other_choices = [p.choice for p in self.other_player().in_all_rounds()]
        my_payoffs = [p.payoff for p in self.in_all_rounds()]
        body = ''
        for i in range(self.round_number):
            row = '<tr> <td>%s</td> <td>%s</td> <td>%s</td> </tr>' % (my_choices[i], other_choices[i], my_payoffs[i])
            body += row
        return body


    def vars_for_template(self):
        if self.session.config['display_all_history']:
            return {
                'body': self.table_body(),
                'other': self.other_player()
            }
        else:
            if self.round_number == 1:
                return {
                    'other': self.other_player()
                }
            else:
                return {
                    'p1_last': self.in_round(self.round_number - 1),
                    'p2_last': self.other_player().in_round(self.round_number - 1),
                    'other': self.other_player()
                }
