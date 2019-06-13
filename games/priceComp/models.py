from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)


"""
Sim for 3x3 'Price Competition' game. Each player is matched with a partner and 
"""


class Constants(BaseConstants):
    name_in_url = 'priceComp'
    players_per_group = 2
    num_rounds = 5

    instructions_template = 'priceComp/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.IntegerField(
        choices=[
            [1, c(1)],
            [2, c(2)],
            [3, c(3)],
        ], widget=widgets.RadioSelect)

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff = {
            1:
                {
                    1: 6,
                    2: 15,
                    3: 15
                },
            2:
                {
                    1: 0,
                    2: 9,
                    3: 18
                },
            3:
                {
                    1: 0,
                    2: 0,
                    3: 12
                }
        }

        self.payoff = c(payoff[self.choice][self.other_player().choice])
