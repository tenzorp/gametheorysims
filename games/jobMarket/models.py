from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
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
            return 'Applicant' if self.in_round(1).role() == 'Employer' else 'Employer'

    def choice_choices(self):
        if self.role() == 'Applicant':
            return ['Easy Courses', 'Difficult Courses']
        else:
            return ['Managerial Job', 'Clerical Job']

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.group.type == 'Slacker':
            if self.role() == 'Employer':
                payoff = {
                    'Managerial Job':
                        {
                            'Easy Courses': 0,
                            'Difficult Courses': 0
                        },
                    'Clerical Job':
                        {
                            'Easy Courses': 60,
                            'Difficult Courses': 60
                        }
                }
                self.payoff = payoff[self.choice][self.other_player().choice]
            else:
                payoff = {
                    'Managerial Job':
                        {
                            'Easy Courses': 100,
                            'Difficult Courses': 50
                        },
                    'Clerical Job':
                        {
                            'Easy Courses': 60,
                            'Difficult Courses': 10
                        }
                }
                self.payoff = payoff[self.other_player().choice][self.choice]
        else:  # go-getter
            if self.role() == 'Employer':
                payoff = {
                    'Managerial Job':
                        {
                            'Easy Courses': 100,
                            'Difficult Courses': 100
                        },
                    'Clerical Job':
                        {
                            'Easy Courses': 60,
                            'Difficult Courses': 60
                        }
                }
                self.payoff = payoff[self.choice][self.other_player().choice]
            else:
                payoff = {
                    'Managerial Job':
                        {
                            'Easy Courses': 100,
                            'Difficult Courses': 80
                        },
                    'Clerical Job':
                        {
                            'Easy Courses': 60,
                            'Difficult Courses': 40
                        }
                }
                self.payoff = payoff[self.other_player().choice][self.choice]
