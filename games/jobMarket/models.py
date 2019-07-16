from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
from random import choices

"""
Sim for Job Market Signaling game
"""


class Constants(BaseConstants):
    name_in_url = 'jobMarket'
    players_per_group = 2
    num_rounds = 3

    instructions_template = 'jobMarket/instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for group in self.get_groups():
            group.type = choices(['Slacker', 'Go-getter'], [0.6, 0.4])[0]


class Group(BaseGroup):
    type = models.StringField()


class Player(BasePlayer):
    choice = models.StringField(
        widget=widgets.RadioSelect)

    def role(self):
        if self.round_number == 1:
            return 'Applicant' if self.id_in_group == 1 else 'Employer'
        else:
            return 'Applicant' if self.in_round(self.round_number-1).role() == 'Employer' else 'Employer'

    def choice_choices(self):
        if self.role() == 'Applicant':
            return ['Easy Courses', 'Difficult Courses'] if self.round_number != 3 else [['Slacker', "I'm a Slacker."], ['Go-getter', "I'm a Go-getter."]]
        else:
            return ['Managerial Job', 'Clerical Job']

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        emp = self.group.get_player_by_role('Employer')
        app = self.group.get_player_by_role('Applicant')
        i = 0 if self.role() == 'Employer' else 1

        if self.group.type == 'Slacker':
            if self.round_number != 3:
                payoff = {
                    'Managerial Job': {
                        'Easy Courses': [0, 100],
                        'Difficult Courses': [0, 50]
                    },
                    'Clerical Job': {
                        'Easy Courses': [60, 60],
                        'Difficult Courses': [60, 10]
                    }
                }
                self.payoff = payoff[emp.choice][app.choice][i]
            else:
                payoff = {
                    'Managerial Job': [0, 100],
                    'Clerical Job': [60, 60]
                }
                self.payoff = payoff[emp.choice][i]
        else:  # go-getter
            if self.round_number != 3:
                payoff = {
                    'Managerial Job': {
                        'Easy Courses': [100, 100],
                        'Difficult Courses': [100, 80]
                    },
                    'Clerical Job': {
                        'Easy Courses': [60, 60],
                        'Difficult Courses': [60, 40]
                    }
                }
                self.payoff = payoff[emp.choice][app.choice][i]
            else:
                payoff = {
                    'Managerial Job': [100, 100],
                    'Clerical Job': [60, 60]
                }
                self.payoff = payoff[emp.choice][i]