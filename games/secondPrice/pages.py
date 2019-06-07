from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    # oTree collects participant ip addresses by default and I think that's
    # creepy and unnecessary
    def clear(self):
        self.player.participant.ip_address = None

    def is_displayed(self):
        return self.player.round_number == 1


class Values(Page):
    form_model = 'player'
    form_fields = ['round_1', 'round_2', 'round_3']

    def is_displayed(self):
        return self.player.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['bid']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_winner()
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        my = self.player
        group = self.group
        return {
            'bid': my.bid,
            'isWinner': my.isWinner,
            'payoff': my.payoff,
            'winner': group.winner,
            'winningBid': group.highestBid,
            'paidBid': group.secondHighest
        }


page_sequence = [
    Introduction,
    Values,
    Main,
    ResultsWaitPage,
    Results
]
