# GameTheoryLab: Interactive Game Theory Simulation

GameTheoryLab is a Python-based simulation library that brings game theory principles and concepts to life. Through its user-friendly interface and robust functionality, users can directly engage with underlying Game Theory concepts by interacting with various cooperative/competitive games.

The inaugural version of this library includes interfaces for exploring the Iterated Prisoner's Dilemma (IPD), an iterative version of the popular Prisoner's Dilemma game. Users can play with other strategies, simulate matches, replicate tournaments, and create their own strategies! 


---

## ✨ Features
- **Large Library of strategies**: The library features 20 IPD strategies, whose functionality vary from deterministic to stochastic, nice to nasty, forgiving to punishing, and simple to complex.

- **User interface**: A ``User`` class allows the users to play directly with other strategies in matches, thus getting an anecdotal experience of their performance, strengths and weaknesses.

- **Dynamic Match/Tournament Simulation**: Includes functionality for simulating matches and round-robin tournaments (and variants), providing media to access the competitiveness of the different strategies.

- **Dataset Generation**: Users can save the results of concluded matches and round-robin tournaments as .csv files for further data analysis.

---

## 🛠️ Installation

GameTheoryLab is easy to set up on your local machine. All you need to do is:

```pip install game-theory-lab```

Then, import it into your project using:

```import gametheorylab```

And you're all set!

---

## 🚀 Usage

Below is a simple demo utilizing GameTheoryLab to explore the IPD, with the help of the ``axelrod_interactive`` library:

```
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

```

---

## 🤝 Contributing

Contributions are welcome! Please follow the steps to contribute:

1. Fork this repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

---

## 🧑‍💻 Author

**Ayomide Olumide-Attah**

Math & CS Double Major at Fisk University

---

## 📄 License

This project is licensed under the MIT License.