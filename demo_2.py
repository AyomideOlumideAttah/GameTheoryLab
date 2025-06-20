# Demonstrating creating a custom strategy!
from gametheorylab import axelrod_interactive as axl
from gametheorylab.axelrod_interactive.strategy import Strategy

axl.set_payoffs()

class CustomStrategy(Strategy):
    """Class that demonstrates how to create a custom strategy. See the provided documentation for details."""
    def __init__(self):
        super().__init__()
        self.name = "Echo"
        self.counter = 0
        self.__doc__ = ("This is a demonstration of creating a custom strategy for use in GameTheoryLab's "
                        "axelrod-interactive package. It serves as a blueprint for all custom strategies to follow to "
                        "be compatible with the package. The strategy shown is the 'Echo' strategy, which cooperates "
                        "for the first two rounds, and then repeats the opponent's move from two moves ago.")

    def additional_prep(self):
        self.counter = 0

    def move(self, opp_history, self_history, opp_score, self_score):
        if self.counter == 0:
            self.counter += 1
            return True
        elif self.counter == 1:
            self.counter += 1
            return False
        return opp_history[-2]

# Demonstrating playing matches with the strategy and saving the results
from gametheorylab.axelrod_interactive.arena import Arena

# Let's test against a forgiving and stochastic player
from gametheorylab.axelrod_interactive.strategies.adaptive_gtft import AdaptiveGTFT

echo = CustomStrategy()
player = AdaptiveGTFT(base_generosity=0.4, delta_p=0.15)
match = Arena(echo, player, num_rounds=25, show_results=True)
match.play_round().to_csv(f"custom_strategy_demo1.csv")

# Now let's try a random player that defects more often
from gametheorylab.axelrod_interactive.strategies.coin_flip import CoinFlip

player = CoinFlip(prob_of_cooperation=0.5)
match = Arena(echo, player, num_rounds=25, show_results=True)
match.play_round().to_csv(f"custom_strategy_demo2.csv")

# Now let's see how it performs in an R16
from gametheorylab.axelrod_interactive.strategies import STRATEGIES
from gametheorylab.axelrod_interactive.tournament import Tournament
from random import sample

players = [s() for s in sample(list(STRATEGIES.values()), k=15)]
players.append(echo)
r16 = Tournament(players, mode='round of 16')
r16.play(show_results=True).to_csv("r16_results.csv")