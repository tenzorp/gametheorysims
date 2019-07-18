from otree.api import Currency as c, SubmissionMustFail
from . import pages
from ._builtin import Bot


class PlayerBot(Bot):
    cases = ['add20', 'dont']

    def play_round(self):
        yield (pages.Introduction)
        yield SubmissionMustFail(pages.Main, {'request': 80})
        if self.case == 'add20':
            if self.player.id_in_group == 1:
                yield (pages.Main, {'request': 11})
                assert self.player.payoff == c(31)
            else:
                yield (pages.Main, {'request': 12})
                assert self.player.payoff == c(12)
        else:
            yield (pages.Main, {'request': 12})
            assert self.player.payoff == c(12)
        yield (pages.Results)
