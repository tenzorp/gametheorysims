from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['gp', 'ip']

    def error_message(self, values):
        if values['gp'] + values['ip'] != Constants.endowment:
            return 'Your values must add up to ' + str(Constants.endowment) + '.'


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.group_tokens = sum([p.gp for p in self.group.get_players()])
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    timeout_seconds = 30

    def vars_for_template(self):
        return {
            'player_payoff': float(self.player.payoff)
        }


class Final(Page):

    def is_displayed(self):
        return self.round_number == 2

    def vars_for_template(self):
        winner_payoff = max(max([[sum(pl.payoff for pl in p.in_all_rounds())] for p in self.group.get_players()]))
        my_total = sum([p.payoff for p in self.player.in_all_rounds()])
        return {
            'my_payoff': float(my_total),
            'winner_payoff': float(winner_payoff)
        }


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results,
    Final
]
