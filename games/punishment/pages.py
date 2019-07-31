from ._builtin import Page, WaitPage
from random import shuffle


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1


class Main(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ContributionsWaitPage(WaitPage):
    pass


class Deductions(Page):
    form_model = 'player'
    form_fields = ['deductions']

    def vars_for_template(self):
        contributions = [(p.contribution, p.id_in_group) for p in self.group.get_players()]
        shuffle(contributions)
        return {
            'contributions': contributions,
            'range': range(1, self.session.config['players_per_group'] + 1)
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Main,
    ContributionsWaitPage,
    Introduction,
    Deductions,
    ResultsWaitPage,
    Results
]
