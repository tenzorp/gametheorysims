from . import pages
from ._builtin import Bot


class PlayerBot(Bot):
    cases = ['betray', 'bothSilent', 'bothConfess']

    def play_round(self):
        yield (pages.Introduction)
        if self.case == 'betray':
            if self.player.id_in_group == 1:
                yield (pages.Main, {'decision': 'Confess'})
                assert self.player.payoff == 0
            else:
                yield (pages.Main, {'decision': 'Remain silent'})
                assert self.player.payoff == 10
        elif self.case == 'bothSilent':
            yield (pages.Main, {'decision': 'Remain silent'})
            assert self.player.payoff == 1
        else:
            yield (pages.Main, {'decision': 'Confess'})
            assert self.player.payoff == 5
        yield (pages.Results)


