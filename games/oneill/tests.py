from . import pages
from ._builtin import Bot


class PlayerBot(Bot):
    cases = ['diff', 'same']

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        if self.case == 'diff':
            if self.player.role() == 'Row':
                yield (pages.Main, {'choice': 'Ace'})
                assert self.player.payoff == -5
                yield (pages.Results)
            else:
                yield (pages.Main, {'choice': 'Joker'})
                assert self.player.payoff == 5
                yield (pages.Results)
        if self.case == 'same':
            yield (pages.Main, {'choice': 'Joker'})
            assert self.player.payoff == 5 if self.player.role() == 'Row' else -5
            yield (pages.Results)
        if self.round_number == 5:
            yield (pages.Final)