from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)
import random

"""
Sim for 'Acquiring a Company' game
"""


class Constants(BaseConstants):
    name_in_url = 'company'
    players_per_group = 2
    num_rounds = 2

    instructions_template = 'company/instructions.html'


class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly()
        for group in self.get_groups():
            group.value = c(random.uniform(0, 100))


class Group(BaseGroup):
    value = models.CurrencyField(initial=0)


class Player(BasePlayer):
    price = models.CurrencyField(min=0, initial=0, label='')

    def role(self):
        if self.round_number == 1:
            return 'Buyer' if self.id_in_group == 1 else 'Seller'
        else:
            return 'Buyer' if self.in_round(1).role() == 'Seller' else 'Seller'

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        buyer = self.group.get_player_by_role('Buyer')
        seller = self.group.get_player_by_role('Seller')
        if buyer.price >= seller.price:
            buyer.payoff = 1.5 * self.group.value - buyer.price
            seller.payoff = buyer.price
        else:
            buyer.payoff = 0
            seller.payoff = self.group.value

