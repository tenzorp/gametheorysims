from ._builtin import Page, WaitPage


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1


class ProposerOffer(Page):
    form_model = 'group'
    form_fields = ['offer']

    def is_displayed(self):
        return self.player.role() == 'proposer'


class ResponderWaitPage(WaitPage):

    def is_displayed(self):
        return self.player.role() == 'responder'


class ResponderChoice(Page):
    form_model = 'group'
    form_fields = ['responder_choice']

    def is_displayed(self):
        return self.player.role() == 'responder'


class ResponderCounter(Page):
    form_model = 'group'
    form_fields = ['counter']

    def is_displayed(self):
        return not self.group.responder_choice and self.round_number > 2 and self.player.role() == 'responder'


class ProposerWaitPage(WaitPage):

    def is_displayed(self):
        return not self.group.responder_choice and self.round_number > 2 and self.player.role() == 'proposer'


class ProposerChoice(Page):
    form_model = 'group'
    form_fields = ['proposer_choice']

    def is_displayed(self):
        return not self.group.responder_choice and self.round_number > 2 and self.player.role() == 'proposer'


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        opponent = self.player.other_player()
        choice = 'accept' if self.group.responder_choice else 'reject'
        counter = 'accept' if self.group.proposer_choice else 'reject'
        return {
            'opponent': opponent,
            'choice': choice,
            'counter': counter
        }


page_sequence = [
    Introduction,
    ProposerOffer,
    ResponderWaitPage,
    ResponderChoice,
    ResponderCounter,
    ProposerWaitPage,
    ProposerChoice,
    ResultsWaitPage,
    Results
]
