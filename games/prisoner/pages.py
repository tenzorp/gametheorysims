from ._builtin import Page, WaitPage


class Introduction(Page):
    pass


class Main(Page):
    form_model = 'player'
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        opponent = self.player.other_player()
        return {
            'opponent': opponent,
            'same_choice': self.player.decision == opponent.decision,
            'player_payoff': int(self.player.payoff),
            'opponent_payoff': int(opponent.payoff)
        }


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
