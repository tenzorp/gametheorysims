from ._builtin import Page, WaitPage


class Introduction(Page):

    def is_displayed(self):
        return self.player.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['claim']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    timeout_seconds = 30

    def vars_for_template(self):
        opponent = self.player.other_player()
        return {
            'player_payoff': int(self.player.payoff),
            'opponent_claim': opponent.claim,
            'opponent_payoff': int(opponent.payoff)
        }


class Final(Page):

    def is_displayed(self):
        return self.round_number == 10

    def vars_for_template(self):
        opponent = self.player.other_player()
        my_total = int(sum([p.payoff for p in self.player.in_all_rounds()]))
        opponent_total = int(sum([p.payoff for p in opponent.in_all_rounds()]))
        return {
            'my_payoff': my_total,
            'opponent_payoff': opponent_total
        }


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results,
    Final
]
