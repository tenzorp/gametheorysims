from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)
import random

"""
Sim for 'Repeated Game of Random Length'
 """


class Constants(BaseConstants):
    name_in_url = 'repeatedFlip'
    players_per_group = 2
    num_rounds = 99

    instructions_template = 'repeatedFlip/instructions.html'


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.group.new_round:
            pass
        else:
            self.group_randomly()


class Group(BaseGroup):
    new_round = models.BooleanField()

    def newRound(self):
        num = random.random() >= 0.51
        if num:
            self.new_round = True
        else:
            self.new_round = False


class Player(BasePlayer):
    choice = models.IntegerField(
        choices=[1, 2],
        widget=widgets.RadioSelect
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff = {
            1:
                {
                    1: 32,
                    2: 12
                },
            2:
                {
                    1: 50,
                    2: 25
                }
        }
        self.payoff = payoff[self.choice][self.other_player().choice]
