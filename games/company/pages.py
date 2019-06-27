from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['price']

    def vars_for_template(self):
        if self.player.role() == 'Seller':
            return {
                'value': self.group.value
            }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        opponent = self.player.get_others_in_group()[0]
        return {
            'player_payoff': self.player.payoff,
            'opponent': opponent,
            'value': self.group.value
        }


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
