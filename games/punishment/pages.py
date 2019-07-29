from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from random import shuffle


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['contribution', 'deductions']

    def vars_for_template(self):
        if self.player.contribution is not None:
            return {
                'contributions': shuffle([p.contribution for p in self.group.get_players()])  # randomize
            }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Main,
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
