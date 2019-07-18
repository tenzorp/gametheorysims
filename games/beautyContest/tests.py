from . import pages
from ._builtin import Bot


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Introduction)
        if self.player.id_in_group == 1:
            yield (pages.Main, {'guess': 90.0})
            assert not self.player.winner
            yield (pages.Results)
        else:
            yield (pages.Main, {'guess': 50.0})
            assert self.player.winner
            yield (pages.Results)
