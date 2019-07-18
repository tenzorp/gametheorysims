from . import pages
from ._builtin import Bot


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        if self.player.role() == 'Row':
            yield (pages.Main, {'choice': 'Extreme'})
            assert self.player.payoff == 10
        else:
            yield (pages.Main, {'choice': 'Challenge'})
            assert self.player.payoff == -10
        yield (pages.Results)
        if self.round_number == 5:
            assert 'You won' in self.html if self.player.role() == 'Row' else 'You did not win' in self.html
            yield (pages.Final)
