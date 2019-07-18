from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot


class PlayerBot(Bot):
    cases = ['diff', 'same']

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        if self.case == 'diff':
            if self.player.id_in_group == 1:
                yield (pages.Main, {'choice': 1})
                assert self.player.payoff == c(15)
            else:
                yield (pages.Main, {'choice': 3})
                assert self.player.payoff == 0
            yield (pages.Results)
            if self.round_number == 5:
                assert 'You won' in self.html if self.player.id_in_group == 1 else 'You did not win' in self.html
                yield (pages.Final)
        else:
            yield (pages.Main, {'choice': 2})
            assert self.player.payoff == 9
            yield (pages.Results)
            if self.round_number == 5:
                assert 'You tied' in self.html
                yield (pages.Final)
