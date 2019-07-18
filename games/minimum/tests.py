from . import pages
from ._builtin import Bot


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        if self.player.id_in_group == 1:
            yield (pages.Main, {'effort': 3})
            assert self.player.payoff == 2
        else:
            yield (pages.Main, {'effort': 1})
            assert self.player.payoff == 4
        yield (pages.Results)

