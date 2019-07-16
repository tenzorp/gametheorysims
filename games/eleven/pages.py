from ._builtin import Page, WaitPage


class Introduction(Page):
    pass


class Main(Page):
    form_model = 'player'
    form_fields = ['request']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        return {
            'opponent': self.player.other_player()
        }


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
