# WordleGame

We have made the game of Wordle in Python along with a Leaderboard System using Tkinter module to make the GUI.

Wordle is a game where players have to guess a secret five-letter word within a limited number of attempts. The game gained widespread popularity particularly in early 2022. Here's how it works:

## Objective:

The objective of Wordle is to guess a five-letter word chosen by the game, typically randomly generated from a dictionary.
Gameplay: The game interface consists of a grid where players input their guesses. After each guess, the game provides feedback in the form of colored blocks:

1. A green block indicates that the guessed letter is both correct in position and in the word.
2. A yellow block indicates that the guessed letter is in the word but not in the correct position.
3. A gray block indicates that the guessed letter is not in the word at all.

Constraints: Players have a limited number of attempts (six in our case) to guess the word correctly. The challenge lies in using deductive reasoning to narrow down the possibilities based on the feedback from previous guesses.
Strategy: Players typically start by guessing words that contain common letters and then adjust their guesses based on the feedback received. As the game progresses and more feedback is provided, players can eliminate letters that are not part of the word and refine their guesses accordingly.

We have also made a Leaderboard System that stores the player name along with the number of guesses he/she needed to guess the word. The top 10 players with the lowest average guess number are displayed in ascending order.
