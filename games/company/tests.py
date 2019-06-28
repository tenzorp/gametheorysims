from otree.api import Currency as c, SubmissionMustFail
from . import pages
from ._builtin import Bot


class PlayerBot(Bot):
    # TODO: this aint workin
    def play_round(self):
        other = self.player.other_player()
        yield (pages.Introduction)
        yield SubmissionMustFail(pages.Main, {'price': -50})

        if self.player.role() == 'Buyer':
            yield (pages.Main, {'price': 80})
            # if the company is bought successfully
            if self.player.price >= other.price:
                assert self.player.payoff == c(self.group.value * 1.5)
            # if bid was below reserve
            else:
                assert self.player.payoff == c(0)
            yield (pages.Results)
            assert self.player.role() == 'Seller'  # check if roles switched
        else:  # seller
            yield (pages.Main, {'price': self.group.value * 2})
            if self.player.price <= other.price:
                assert self.player.payoff == c(other.price)
            else:
                assert self.player.payoff == c(self.group.value)
            yield (pages.Results)
            assert self.player.role() == 'Buyer'

