from ._builtin import Page, WaitPage


class Introduction(Page):
    timeout_seconds = 100


class Main(Page):
    form_model = 'player'
    form_fields = ['guess']


"""
class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()
"""


class Result(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return {
            'my_decision': me.decision,
            'opponent_decision': opponent.decision,
            'same_choice': me.decision == opponent.decision,
        }


page_sequence = [
    Introduction,
    Main,
    Result
]
