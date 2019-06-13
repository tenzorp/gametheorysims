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
    choice = models.CurrencyField(
        choices=[c(1), c(2), c(3)],
        widget=widgets.RadioSelect)

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff = {
            c(1):
                {
                    c(1): c(6),
                    c(2): c(15),
                    c(3): c(15)
                },
            c(2):
                {
                    c(1): c(0),
                    c(2): c(9),
                    c(3): c(18)
                },
            c(3):
                {
                    c(1): c(0),
                    c(2): c(0),
                    c(3): c(12)
                }
        }

        self.payoff = payoff[self.choice][self.other_player().choice]