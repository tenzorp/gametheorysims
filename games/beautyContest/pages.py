from ._builtin import Page, WaitPage


class Introduction(Page):
    pass


class Main(Page):
    form_model = 'player'
    form_fields = ['guess']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):  # not a great practice to have this much in pages but it felt easiest
        players = self.group.get_players()
        self.group.winning = round((sum([p.guess for p in players]) / len(players)) * 2/3, 3)
        winner = min([p.guess for p in players], key=lambda  x:abs(x-self.group.winning))
        for p in players:
            p.winner = True if p.guess == winner else False


class Results(Page):

    def vars_for_template(self):
        return {
            'mean': round(self.group.winning * (3/2), 3)
        }


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
