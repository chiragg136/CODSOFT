import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("400x300")

        self.user_score = 0
        self.computer_score = 0

        self.result_text = tk.StringVar()
        self.score_text = tk.StringVar()
        self.score_text.set(f"Score: User {self.user_score} - Computer {self.computer_score}")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Rock, Paper, Scissors", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(self.root, textvariable=self.result_text, font=("Helvetica", 12)).pack(pady=10)
        tk.Label(self.root, textvariable=self.score_text, font=("Helvetica", 12)).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Button(frame, text="Rock", command=lambda: self.user_choice("rock"), width=10).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Paper", command=lambda: self.user_choice("paper"), width=10).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Scissors", command=lambda: self.user_choice("scissors"), width=10).grid(row=0, column=2, padx=5)

        tk.Button(self.root, text="Reset", command=self.reset_game, width=10).pack(pady=10)

    def user_choice(self, choice):
        computer_action = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(choice, computer_action)

        if result == "user":
            self.user_score += 1
            self.result_text.set(f"You win! {choice.capitalize()} beats {computer_action}.")
        elif result == "computer":
            self.computer_score += 1
            self.result_text.set(f"Computer wins! {computer_action.capitalize()} beats {choice}.")
        else:
            self.result_text.set(f"It's a tie! Both chose {choice}.")

        self.score_text.set(f"Score: User {self.user_score} - Computer {self.computer_score}")

    def determine_winner(self, user_action, computer_action):
        if user_action == computer_action:
            return "tie"
        elif (user_action == "rock" and computer_action == "scissors") or \
             (user_action == "paper" and computer_action == "rock") or \
             (user_action == "scissors" and computer_action == "paper"):
            return "user"
        else:
            return "computer"

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_text.set("")
        self.score_text.set(f"Score: User {self.user_score} - Computer {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
