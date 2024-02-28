import random
from rich.panel import Panel
from rich import print
from rich.console import Console
from rich.prompt import Prompt


def word_contains_number(word):
    for char in word:
        if char.isdigit():
            return True
    return False


class Termdle():
    def __init__(self, word_list_path):
        self.word_list_path = word_list_path
        self.console = Console()
        self.reset()

    def end_game(self, guess_word):
        self.draw_board()
        self.game_ended = True
        if guess_word == self.word:
            print(f"[green]You won word was '{ self.word }'")
        else:
            print(f"[red]You lost word was '{ self.word }'")

        action = Prompt.ask(
            "Press 'R/Enter' to reset, 'Q' to quit.",
            choices=["R", "Q",],
            default="R"
        )

        if action == "R":
            self.reset()
        elif action == "Q":
            quit()

    def guess(self):
        self.draw_board()
        guess_word = self.console.input("[blue]Guess a word [white]> ")
        if len(guess_word) == 5 and guess_word in self.word_list and not word_contains_number(guess_word):
            self.previous_guesses.append(guess_word)
            self.guess_count += 1
            if self.guess_count == 6 or guess_word == self.word:
                self.end_game(guess_word)

    def reset(self):
        self.game_ended = False
        self.console.clear()
        self.guess_count = 0
        self.previous_guesses = []
        with open(self.word_list_path, 'r') as file:
            self.word_list = file.readlines()
            self.word_list = [word.strip().lower() for word in self.word_list]
            self.word = random.choice(self.word_list)

    def draw_board(self):
        self.console.clear()
        pretty_guesses = ""
        for guess in self.previous_guesses:
            for i, char in enumerate(guess):
                if self.word[i] == char:
                    pretty_guesses += f"[green][{char.upper()}]"
                elif char in self.word:
                    pretty_guesses += f"[yellow][{char.upper()}]"
                else:
                    pretty_guesses += f"[red][{char.upper()}]"
            pretty_guesses += "\n"

        subtitle = f"[blue]Guesses: {self.guess_count}/6" if self.guess_count != 0 else None

        panel = Panel.fit(
            pretty_guesses[:-1],
            title="[blue]Termdle",
            subtitle=subtitle,
        )
        print(panel)

    def start(self):
        while not self.game_ended:
            self.guess()
