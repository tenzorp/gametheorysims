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
        for g in self.get_groups():
            g.coin_flip()
            print(g.new_round)
            if g.new_round:
                self.group_randomly()


class Group(BaseGroup):
    new_round = models.BooleanField()

    def coin_flip(self):
        num = random.random() >= 0.50
        if num:
            self.new_round = True
        else:
            self.new_round = False


class Player(BasePlayer):
    choice = models.IntegerField(
        choices=[1, 2],
        widget=widgets.RadioSelect,
        label='Please make your choice.'
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
