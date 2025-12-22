from gametheorylab.axelrod_interactive.strategy import Strategy
from gametheorylab.axelrod_interactive import get_payoffs
from gametheorylab.axelrod_interactive.result import Result
import random

class Arena:
    """Class that simulates a head-to-head match between two strategies.

    Args:
        s1 (Strategy): One of the strategies playing the match.
        s2 (Strategy): The other strategies playing the match.
        num_rounds (int): The number of rounds in the match. Defaults to 10.
    """
    payoffs = get_payoffs()
    def __init__(self, s1: Strategy, s2: Strategy, num_rounds: int=10):
        # Validation
        if not isinstance(s1, Strategy):
            raise ValueError("Parameter 's1' is not a Strategy.")
        if not isinstance(s2, Strategy):
            raise ValueError("Parameter 's2' is not a Strategy.")
        if not isinstance(num_rounds, int):
            raise ValueError(f"Parameter 'num_rounds' must be an integer! (You entered {num_rounds}).")

        self.s1 = s1
        self.s2 = s2
        self.num_rounds = num_rounds
        self.s1_history = []
        self.s2_history = []
        self.s1_score = 0
        self.s2_score = 0

    def run(self, faulty: bool=False):
        """This simulates the two players going at it for the specified number of times. Who's going to win this round?
        Args:
            faulty (float): Boolean flag tht determines whether or not a player's decision is flipped. Defaults to False.
        """
        # Validation
        if not isinstance(faulty, bool):
            raise ValueError(f"Parameter 'faulty' must be a boolean! (You entered {faulty}.)")

        # Determining each player's choice
        choice1 = self.s1.play(self.s2_history, self.s1_history, self.s2_score, self.s1_score)
        choice2 = self.s2.play(self.s1_history, self.s2_history, self.s1_score, self.s2_score)

        # Implementing noise
        if faulty:
            if random.choice([True, False]):
                choice1 = not choice1
            else:
                choice2 = not choice2

        # Saving each player's choice
        self.s1_history.append(choice1)
        self.s2_history.append(choice2)

        # Adding points to each player as appropriate
        if choice1 and choice2:
            self.s1_score += self.payoffs["Reward"]
            self.s2_score += self.payoffs["Reward"]

        elif choice1:
            self.s1_score += self.payoffs["Sucker"]
            self.s2_score += self.payoffs["Temptation"]

        elif choice2:
            self.s1_score += self.payoffs["Temptation"]
            self.s2_score += self.payoffs["Sucker"]

        else:
            self.s1_score += self.payoffs["Punishment"]
            self.s2_score += self.payoffs["Punishment"]

    def play_round(self, noise: float=0, num_rounds: int=None, show_results: bool=True):
        """This simulates the two players going at it for the specified number of times. Who's going to win this round?
        Args:
            noise (float): The level of noise in the match (this is the chance that any intended move is flipped). Note that 'noise' must be in (0, 1). Defaults to 0.
            num_rounds (int): The number of rounds in the match (if a change in match length is desired). If not provided, the original num_rounds provided when initializing the class would be used.
            show_results (bool): show_results: Flag that determines whether the results of the match should be printed onto the console. Defaults to True.
        """
        # Validation
        if not (0 <= noise < 1):
            if noise < 0:
                string = f"({noise} < 0)"
            else:
                string = f"({noise} >= 1)"
            raise ValueError("Parameter 'noise' is out of range! " + string)
        if not isinstance(show_results, bool):
            raise ValueError(f"Parameter 'show_results' must be a boolean! (You entered {show_results}).")

        # Preparation:
        if num_rounds is not None: self.num_rounds = num_rounds
        self.s1.prep_for_match()
        self.s2.prep_for_match()
        self.s1_history = []
        self.s2_history = []
        self.s1_score = 0
        self.s2_score = 0

        num_faults = int(1 / noise)
        # Simulating the match
        for k in range(self.num_rounds):
            if self.s1_score < 0 or self.s2_score < 0:
                break
            should_flip = k > 0 and k % num_faults == 0
            self.run(should_flip)

        if show_results:
            print(f"{self.s1}'s moves: ")
            print(["C" if move else "D" for move in self.s1_history])

            print(f"{self.s2}'s moves: ")
            print(["C" if move else "D" for move in self.s2_history])

            print(f"Results: {self.s1_score} - {self.s2_score}")
            print("\n")

        result_dict = {"Move": list(range(1, self.num_rounds + 1)) + ["SCORE"],
                       self.s1.name: ["C" if move else "D" for move in self.s1_history] + [self.s1_score],
                       self.s2.name: ["C" if move else "D" for move in self.s2_history] + [self.s2_score]}
        return Result(result_dict)
