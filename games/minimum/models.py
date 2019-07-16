from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer)


"""
Sim for "Minimum Effort Game"
"""


class Constants(BaseConstants):
    name_in_url = 'minimum'
    players_per_group = 5
    num_rounds = 3

    instructions_template = 'minimum/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    min = models.IntegerField()

    def winner(self):
        val = 0
        winner = ''
        for p in self.get_players():
            if p.total() > val:
                val = p.total()
                winner = p.id_in_group
        return winner


class Player(BasePlayer):
    effort = models.IntegerField(min=1, max=5)

    def set_payoff(self):
        self.payoff = 5 * self.group.min - self.effort

    def total(self):
        return int(sum([p.payoff for p in self.in_all_rounds()]))
