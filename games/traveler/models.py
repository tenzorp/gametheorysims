from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)


"""
Sim for "Traveler's Dilemma" game. Each player chooses a price and wins or loses money dependent on
their partner's choice.
"""


class Constants(BaseConstants):
    name_in_url = 'traveler'
    players_per_group = 2
    num_rounds = 10

    instructions_template = 'traveler/instructions.html'


class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    claim = models.IntegerField(min=80, max=200, label="Please enter a claim between 80 and 200 cents.")

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.claim == self.other_player().claim:
            self.payoff = self.claim
        elif self.claim > self.other_player().claim:
            self.payoff = self.other_player().claim - 10
        else:
            self.payoff = self.claim + 10
