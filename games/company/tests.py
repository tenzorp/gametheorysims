from otree.api import SubmissionMustFail
from . import pages
from ._builtin import Bot


class PlayerBot(Bot):
    cases = ['sold', 'unsold']

    def play_round(self):
        if self.round_number == 1:
            yield (pages.Introduction)
        yield SubmissionMustFail(pages.Main, {'price': -50})
        price = {
            'sold': 80,
            'unsold': 30
        }[self.case]
        reserve = {
            'sold': 60,
            'unsold': 90
        }[self.case]
        if self.player.role() == 'Buyer':
            yield (pages.Main, {'price': price})
            assert self.player.payoff == 1.5 * self.group.value if self.case == 'sold' else self.player.payoff == 0
            yield (pages.Results)
        else:
            yield (pages.Main, {'price': reserve})
            assert self.player.payoff == self.player.other_player().price if self.case == 'sold' else self.player.payoff == self.group.value
            yield (pages.Results)
