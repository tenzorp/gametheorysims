from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
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
    value = models.CurrencyField(min=0)


class Player(BasePlayer):
    price = models.CurrencyField(min=0)

    def role(self):
        if self.round_number == 1:
            if self.id_in_group == 1:
                return 'Buyer'
            else:
                return 'Seller'
        else:
            if self.id_in_group == 2:
                return 'Buyer'
            else:
                return 'Seller'

    def set_payoff(self):
        buyer = self.group.get_player_by_role('Buyer')
        seller = self.group.get_player_by_role('Seller')
        if buyer.price >= seller.price:
            buyer.payoff = 1.5 * self.group.value
            seller.payoff = buyer.price
        else:
            buyer.payoff = 0
            seller.payoff = self.group.value

