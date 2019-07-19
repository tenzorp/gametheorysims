from ._builtin import Page, WaitPage


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['choice']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        opponent = self.player.other_player()
        return {
            'player_payoff': int(self.player.payoff),
            'opponent_choice': opponent.choice,
            'opponent_payoff': int(opponent.payoff)
        }

    def before_next_page(self):
        if self.player.id_in_group == 1:
            self.group.coin_flip()  # janky way to flip once


class Rematch(Page):

    def is_displayed(self):
        return not self.group.new_round


class RegroupWaitPage(WaitPage):
    group_by_arrival_time = False

  #  def before_next_page(self):
   #     self.subsession.group_randomly()

    def is_displayed(self):
        return not self.group.new_round


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results,
    Rematch,
    RegroupWaitPage
]
