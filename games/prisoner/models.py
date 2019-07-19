from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)


"""
Sim for "Prisoner's Dilemma" game. Each player is matched with another and do not know their
partner. Each must choose to confess or remain silent in the face of jail time. If both choose
to remain silent, then each serves one year. If both choose to confess then each serve 5 years.
If one player chooses to remain silent and the other chooses to confess, then the former serves
10 years while the latter serves 0. Players will learn of their partner's choices and their 
outcome at the end.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'prisoner/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(
        choices=['Confess', 'Remain silent'],
        widget=widgets.RadioSelect,
        label='Please choose to confess or remain silent.'
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff = {
            'Confess':
                {
                    'Confess': 5,
                    'Remain silent': 0
                },
            'Remain silent':
                {
                    'Confess': 10,
                    'Remain silent': 1
                }
        }

        self.payoff = payoff[self.decision][self.other_player().decision]
