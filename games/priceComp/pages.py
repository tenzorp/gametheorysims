from ._builtin import Page, WaitPage


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
            'opponent_price': opponent.choice,
            'opponent_payoff': opponent.payoff,
            'same_price': self.player.choice == opponent.choice
        }


class Final(Page):

    def is_displayed(self):
        return self.round_number == 5

    def vars_for_template(self):
        opponent = self.player.other_player()
        my_total = sum([p.payoff for p in self.player.in_all_rounds()])
        opponent_total = sum([p.payoff for p in opponent.in_all_rounds()])
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
