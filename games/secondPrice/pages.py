from ._builtin import Page, WaitPage


class Introduction(Page):

    def is_displayed(self):
        return self.player.round_number == 1


class Values(Page):
    form_model = 'player'
    form_fields = ['value']

    def vars_for_template(self):
        ['Please enter the last two digits of your phone number.', ]


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
        group = self.group
        winner = group.get_player_by_id(group.winner)
        return {
            'winnerPayoff': winner.payoff,
            'winnerVal': winner.value
        }


class Final(Page):

    def is_displayed(self):
        return self.player.round_number == 3

    def vars_for_template(self):
        p = [p for p in self.player.in_all_rounds()]
        w = [g.get_player_by_id(g.winner).payoff for g in self.group.in_all_rounds()]

        return {
            'p': p,
            'w': w
        }


page_sequence = [
    Introduction,
    Values,
    Main,
    ResultsWaitPage,
    Results,
    Final
]
