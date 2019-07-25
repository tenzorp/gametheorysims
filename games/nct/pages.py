from ._builtin import Page, WaitPage


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class P1Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        return self.player.role() == 1


class P2WaitPage(WaitPage):

    def is_displayed(self):
        return self.player.role() == 2


class P2Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def is_displayed(self):
        if self.player.role() == 2:
            return self.player.other_player().decision != 'Out'

    def vars_for_template(self):
        opponent = self.player.other_player()
        return {
            'opponent_decision': opponent.decision
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        opponent = self.player.other_player()
        return {
            'opponent': opponent,
            'my_payoff': int(self.player.payoff),
            'opponent_payoff': int(opponent.payoff)
        }


class Final(Page):

    def is_displayed(self):
        return self.round_number == 2

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
    P1Decision,
    P2WaitPage,
    P2Decision,
    ResultsWaitPage,
    Results,
    Final
]
