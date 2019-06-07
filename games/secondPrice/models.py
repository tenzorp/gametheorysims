from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)
import random


"""
Sim for "Second Price Auction" game. Small groups of a configurable size are formed
to participate in a series of auctions. In each round, each group member will
enter a bid for a fictitious item. The person with the highest bid wins and earns
their "value" for the item - and they must pay a value equivalent to the second highest 
bid in the group. Thus, the winner's payoff is equal to their value minus the second 
highest bid. The payoff for all other players is 0. 

1st round - value is equal to the last two digits of cellphone number
2nd round - value is equal to DOB (day of the month)
3rd round - value is equal to last two digits of campus mailbox/street number
"""


class Constants(BaseConstants):
    name_in_url = 'secondPrice'
    players_per_group = None
    num_rounds = 3
    instructions_template = 'secondPrice/instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        group_matrix = []
        players = self.get_players()
        ppg = self.session.config['players_per_group']
        for i in range(0, len(players), ppg):
            group_matrix.append(players[i:i+ppg])
        self.set_group_matrix(group_matrix)


class Group(BaseGroup):
    highestBid = models.CurrencyField()
    secondHighest = models.CurrencyField()
    winner = models.StringField()

    def set_winner(self):
        players = self.get_players()
        bids = [p.bid for p in players]
        bids.sort()
        self.highestBid = bids[-1]
        self.secondHighest = bids[-2]
        tiedWinners = [p.participant for p in players if p.bid == self.highestBid]
        self.winner = random.choice(tiedWinners)
        self.winner.isWinner = True


class Player(BasePlayer):
    round_1 = models.CurrencyField(min=0, max=99)
    round_2 = models.CurrencyField(min=0, max=31)
    round_3 = models.CurrencyField(min=0, max=99)
    bid = models.CurrencyField(min=0)
    isWinner = models.BooleanField(initial=False)

    def set_payoff(self):
        if self.isWinner:
            if self.round_number == 1:
                self.payoff = self.round_1 - self.group.secondHighest
            elif self.round_number == 2:
                self.payoff = self.round_2 - self.group.secondHighest
            elif self.round_number == 3:
                self.payoff = self.round_3 - self.group.secondHighest
        else:
            self.payoff = c(0)
