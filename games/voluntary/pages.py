from ._builtin import Page, WaitPage


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['gp']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.group_tokens = sum([p.gp for p in self.group.get_players()])
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        return {
            'player_payoff': float(self.player.payoff),
            'ip': 50 - self.player.gp
        }


class Final(Page):

    def is_displayed(self):
        return self.round_number == 10

    def vars_for_template(self):
        return {
            'my_payoff': float(self.participant.payoff)
        }


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results,
    Final
]
