from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    timeout_seconds = 120


class Main(Page):
    form_model = 'player'
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        my = self.player
        opponent = my.other_player()
        return {
            'my_decision': my.decision,
            'opponent_decision': opponent.decision,
            'same_choice': my.decision == opponent.decision,
        }


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
