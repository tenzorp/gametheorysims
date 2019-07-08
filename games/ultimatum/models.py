from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Currency as c
)
import random

"""
Sim for Ultimatum/Two-Stage Bargaining Game
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum'
    players_per_group = 2
    num_rounds = 4

    instructions_template = 'ultimatum/instructions.html'
    role = random.choice([1, 2])
    endowment = c(100)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    offer = models.CurrencyField(min=0, max=Constants.endowment, label='')
    responder_choice = models.BooleanField(
        widget=widgets.RadioSelect,
        choices=[[True, 'Accept'], [False, 'Reject']],
        label='')
    counter = models.CurrencyField(min=0, max=25, label='')
    proposer_choice = models.BooleanField(
        widget=widgets.RadioSelect,
        choices=[[True, 'Accept'], [False, 'Reject']],
        label='')


class Player(BasePlayer):

    def role(self):
        if self.round_number == 1:
            return 'proposer' if self.id_in_group == Constants.role else 'responder'
        else:
            return 'proposer' if self.in_round(self.round_number - 1).role() == 'responder' else 'responder'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        if self.group.responder_choice:
            self.group.get_player_by_role('responder').payoff = self.group.offer
            self.group.get_player_by_role('proposer').payoff = Constants.endowment - self.group.offer
        else:
            if self.round_number > 2 and self.group.proposer_choice:
                self.group.get_player_by_role('proposer').payoff = self.group.counter
                self.group.get_player_by_role('responder').payoff = 25 - self.group.counter
            else:
                self.payoff = 0
                self.other_player().payoff = 0
