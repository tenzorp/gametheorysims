from ._builtin import Page, WaitPage


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1 or self.round_number == 3


class ApplicantChoice(Page):
    form_model = 'player'
    form_fields = ['choice']

    def is_displayed(self):
        return self.player.role() == 'Applicant'


class ApplicantChoiceWaitPage(WaitPage):
    title_text = ' '
    body_text = 'You are the employer. Please wait for the applicant to make their decision.'

    def is_displayed(self):
        return self.player.role() == 'Employer'


class EmployerChoice(Page):
    form_model = 'player'
    form_fields = ['choice']

    def is_displayed(self):
        return self.player.role() == 'Employer'

    def vars_for_template(self):
        return {
            'applicant_choice': self.player.other_player().choice
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):

    def vars_for_template(self):
        opponent = self.player.other_player()
        return {
            'player_payoff': int(self.player.payoff),
            'opponent_choice': opponent.choice,
            'opponent_payoff': int(opponent.payoff)
        }


page_sequence = [
    Introduction,
    ApplicantChoice,
    ApplicantChoiceWaitPage,
    EmployerChoice,
    ResultsWaitPage,
    Results
]
