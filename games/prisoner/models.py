from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
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

    # payoff if both remain silent or confess
    bothConfess = 5
    bothSilent = 1

    # payoff one betrays the other
    betrayer = 0
    betrayed = 10

    instructions_template = 'prisoner/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.StringField(
        choices=['Confess', 'Remain silent'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )
    sentence = models.IntegerField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        payoff = {
            'Confess':
                {
                    'Confess': Constants.bothConfess,
                    'Remain silent': Constants.betrayed
                },
            'Remain silent':
                {
                    'Confess': Constants.betrayer,
                    'Remain silent': Constants.bothSilent
                }
        }

        self.sentence = payoff[self.decision][self.other_player().decision]
