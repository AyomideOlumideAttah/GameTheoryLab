from gametheorylab.axelrod_interactive.strategy import Strategy

class ContriteTitForTat(Strategy):
    def __init__(self):
        super().__init__()
        self.is_contrite = False
        self.name = "Contrite Tit for Tat"
        self.__doc__ = ("This is a strategy similar to Tit for Tat... except that it cooperates if it defected in the"
                        "previous round but the opponent cooperated. This is a subtle modification but it's crucial for "
                        "the strategy's stability during noisy matches.")

    def additional_prep(self):
        self.is_contrite = False

    def update_history(self, opp_history, self_history):
        if opp_history:
            if opp_history[-1] and not self_history[-1]:
                self.is_contrite = True
            elif opp_history[-1]:
                self.is_contrite = False

    def move(self, opp_history, self_history, opp_score, self_score):
        if self.is_contrite:
            return True
        return not opp_history or opp_history[-1]
