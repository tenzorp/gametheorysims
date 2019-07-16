from ._builtin import Page, WaitPage


class Introduction(Page):

    def is_displayed(self):
        return self.player.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['effort']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        players = self.group.get_players()
        self.group.min = min([p.effort for p in players])
        for p in players:
            p.set_payoff()


class Results(Page):
    timeout_seconds = 30

    def vars_for_template(self):
        return {
            'my_payoff': int(self.player.payoff)
        }


class Final(Page):

    def is_displayed(self):
        return self.round_number == 3

    def vars_for_template(self):
        return {
            'my_total': self.player.total(),
            'winner': self.group.winner(),
            'winner_payoff': self.group.get_player_by_id(self.group.winner()).total()
        }


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results,
    Final
]
