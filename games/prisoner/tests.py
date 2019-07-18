from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    cases = ['oneBetray', 'bothSilent']

    def play_round(self):
        yield (pages.Introduction)
        if self.case == 'oneBetray':
            if self.player.id_in_group == 1:
                yield (pages.Main, {'decision': 'Confess'})
                assert self.player.sentence == 0
            else:
                yield (pages.Main, {'decision': 'Remain silent'})
                assert self.player.sentence == 10
            yield (pages.Results)

