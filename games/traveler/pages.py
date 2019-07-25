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
        return {
            'my_payoff': int(self.participant.payoff)
        }


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results,
    Final
]
