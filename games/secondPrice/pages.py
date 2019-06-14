from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    # TODO: oTree collects participant ip addresses by default and I think that's
    #  creepy and unnecessary

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
    timeout_seconds = 30

    def vars_for_template(self):
        group = self.group
        winner = group.get_player_by_id(group.winner)
        values = [winner.round_1, winner.round_2, winner.round_3]
        return {
            'winner': winner.participant.id_in_session,
            'winnerPayoff': winner.payoff,
            'winnerVal': values[group.round_number - 1]
        }


class Final(Page):
    def is_displayed(self):
        return self.player.round_number == 3


page_sequence = [
    Introduction,
    Values,
    Main,
    ResultsWaitPage,
    Results,
    Final
]
