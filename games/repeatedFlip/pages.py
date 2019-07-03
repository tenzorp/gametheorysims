from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
import random


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['choice']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        opponent = self.player.other_player()
        return {
            'player_payoff': int(self.player.payoff),
            'opponent_choice': opponent.choice,
            'opponent_payoff': int(opponent.payoff)
        }

    def before_next_page(self):
        self.group.newRound()


class Final(Page):
    timeout_seconds = 30

    def is_displayed(self):
        return not self.group.new_round

    def vars_for_template(self):
        opponent = self.player.other_player()
        my_total = int(sum([p.payoff for p in self.player.in_all_rounds()]))
        opponent_total = int(sum([p.payoff for p in opponent.in_all_rounds()]))
        return {
            'my_payoff': my_total,
            'opponent_payoff': opponent_total
        }


class RegroupWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.group_randomly()

    def is_displayed(self):
        return not self.group.new_round


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results,
    Final,
    RegroupWaitPage
]