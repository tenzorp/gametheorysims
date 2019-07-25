from ._builtin import Page, WaitPage


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['price']

    def vars_for_template(self):
        if self.player.role() == 'Seller':
            return {
                'value': self.group.value
            }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        opponent = self.player.get_others_in_group()[0]
        return {
            'opponent': opponent,
            'sold': self.group.get_player_by_role('Buyer').price >= self.group.get_player_by_role('Seller').price
        }


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
