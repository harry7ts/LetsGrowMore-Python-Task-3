## LetsGrowMore Python Developer Virtual Internship Program

## Task-III

## Creating a RockPaperScissors Game using GUI Programming i.e. Tkinter Module


import tkinter as tk
from random import *

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("400x300")
        self.window.config(bg="#f0f0f0")

        self.player_score = 0
        self.computer_score = 0

        tk.Label(self.window, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333333").pack(pady=10)

        score_frame = tk.Frame(self.window, bg="#f0f0f0")
        score_frame.pack(pady=10)
        self.player_score_label = tk.Label(score_frame, text="Player Score: 0", font=("Arial", 12), bg="#f0f0f0")
        self.player_score_label.grid(row=0, column=0, padx=20)
        self.computer_score_label = tk.Label(score_frame, text="Computer Score: 0", font=("Arial", 12), bg="#f0f0f0")
        self.computer_score_label.grid(row=0, column=1, padx=20)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 14), bg="#f0f0f0", fg="#007700")
        self.result_label.pack(pady=10)

        choice_frame = tk.Frame(self.window, bg="#f0f0f0")
        choice_frame.pack(pady=10)
        self.your_choice_label = tk.Label(choice_frame, text="Your Choice: ", font=("Arial", 12), bg="#f0f0f0")
        self.your_choice_label.grid(row=0, column=0, padx=10)
        self.computer_choice_label = tk.Label(choice_frame, text="Computer Choice: ", font=("Arial", 12), bg="#f0f0f0")
        self.computer_choice_label.grid(row=0, column=1, padx=10)

        button_frame = tk.Frame(self.window, bg="#f0f0f0")
        button_frame.pack(pady=10)
        for i, text in enumerate(["Rock", "Paper", "Scissors"], start=0):
            button = tk.Button(button_frame, text=text, font=("Arial", 12), width=10, bg="#e0e0e0")
            button.grid(row=0, column=i, padx=10)
            button.config(command=lambda t=text.lower(): self.play(t))

        control_frame = tk.Frame(self.window, bg="#f0f0f0")
        control_frame.pack(pady=10)
        tk.Button(control_frame, text="Reset", font=("Arial", 12), width=10, command=self.reset, bg="#ffcccb").grid(row=0, column=0, padx=10)
        tk.Button(control_frame, text="Exit", font=("Arial", 12), width=10, command=self.window.quit, bg="#ffcccb").grid(row=0, column=1, padx=10)

    def computer_choice(self):
        return choice(["rock", "paper", "scissors"])

    def update_choice_labels(self, player_choice, computer_choice):
        self.your_choice_label['text'] = f"Your Choice: {player_choice.capitalize()}"
        self.computer_choice_label['text'] = f"Computer Choice: {computer_choice.capitalize()}"

    def play(self, player_choice):
        computer = self.computer_choice()
        self.update_choice_labels(player_choice, computer)
        result = ""
        if computer == player_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and computer == "scissors") or (player_choice == "paper" and computer == "rock") or (player_choice == "scissors" and computer == "paper"):
            self.player_score += 1
            self.player_score_label['text'] = f"Player Score: {self.player_score}"
            result = "Player wins!"
        else:
            self.computer_score += 1
            self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"
            result = "Computer wins!"
        self.result_label['text'] = result

    def reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.player_score_label['text'] = "Player Score: 0"
        self.computer_score_label['text'] = "Computer Score: 0"
        self.result_label['text'] = ""
        self.your_choice_label['text'] = "Your Choice: "
        self.computer_choice_label['text'] = "Computer Choice: "

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
