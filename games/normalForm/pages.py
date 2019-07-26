from ._builtin import Page, WaitPage


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['choice']

    def vars_for_template(self):
        return self.player.vars_for_template()


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        return self.player.vars_for_template()


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
