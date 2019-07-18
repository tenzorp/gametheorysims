from . import pages
from ._builtin import Bot


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        for i in range(4):
            yield (pages.Main, {'choice': 'Heads'})
            assert self.player.payoff == 1 if self.player.role() == 'Row' else self.player.payoff == 0
            yield (pages.Results)
        assert self.player.participant.vars['total'] == 4 if self.player.role() == 'Row' else self.player.participant.vars['total'] == 0
        yield (pages.Final)
        # TODO: assert fails :(
