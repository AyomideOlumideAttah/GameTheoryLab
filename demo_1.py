# Demonstrating using the User class to play against strategies and saving the results

from gametheorylab import axelrod_interactive as axl
from gametheorylab.axelrod_interactive.strategies.user import User
from gametheorylab.axelrod_interactive.strategies import STRATEGIES
from gametheorylab.axelrod_interactive.arena import Arena
from random import choice, sample

axl.set_payoffs()

user = User("Player1")
player = choice(list(STRATEGIES.values()))()
print(player.name + ":", player.__doc__) # Information about the strategy

arena = Arena(user, player, num_rounds=20, show_results=True)
result = arena.play_round() # Returns a Result object!
result.to_csv(f"user_vs_{player.__class__.__name__}") # Saving the result to a .csv file for further analysis

# Demonstrating simulating a round-robin tournament and saving the results
from gametheorylab.axelrod_interactive.tournament import Tournament

players = [s() for s in sample(list(STRATEGIES.values()), k=15)]
tournament = Tournament(players, num_repeats=5, num_rounds=250)
result = tournament.play(show_results=True)
result.to_csv("tournament_results.csv")
