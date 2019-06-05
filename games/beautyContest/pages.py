from ._builtin import Page, WaitPage


class Introduction(Page):
    timeout_seconds = 120


class Main(Page):
    form_model = 'player'
    form_fields = ['guess']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        players = self.group.get_players()
        win = [p.guess for p in players]
        self.group.mean = sum(win) / len(players)
        self.group.twothirds = self.group.mean * (2/3)
        self.group.winningval = min(win, key=lambda x: x-self.group.twothirds)
        for p in players:
            if self.group.winningval == p.guess:
                p.winner = True
                self.group.winner = p.id_in_group



class Results(Page):
    pass


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
