# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from random import randint

#  Create the main window
root = tk.Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

# Create a welcome message label
welcome_label = tk.Label(root, text="Welcome to the Rock Paper Scissors Game!", font=("Helvetica", 18), bg="#9b59b6", fg="white")
welcome_label.pack(pady=20)

# Function to start the game
def start_game():
    welcome_label.pack_forget()  # Hide the welcome message
    start_button.pack_forget()   # Hide the start button

    # Load and display images for Rock, Paper, Scissors
    rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
    paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
    scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
    rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
    paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
    scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

    # Create labels for user and computer choices
    user_label = tk.Label(root, image=scissor_img, bg="#9b59b6")
    comp_label = tk.Label(root, image=scissor_img_comp, bg="#9b59b6")
    comp_label.grid(row=1, column=0)
    user_label.grid(row=1, column=4)

    # Create labels for scores
    playerScore = tk.Label(root, text=0, font=("Helvetica", 24), bg="#9b59b6", fg="white")
    computerScore = tk.Label(root, text=0, font=("Helvetica", 24), bg="#9b59b6", fg="white")
    computerScore.grid(row=1, column=1)
    playerScore.grid(row=1, column=3)

    # Create labels for indicators (USER and COMPUTER)
    user_indicator = tk.Label(root, text="USER", font=("Helvetica", 18), bg="#9b59b6", fg="white")
    comp_indicator = tk.Label(root, text="COMPUTER", font=("Helvetica", 18), bg="#9b59b6", fg="white")
    user_indicator.grid(row=0, column=3)
    comp_indicator.grid(row=0, column=1)

    # Create a label for messages (game results)
    msg = tk.Label(root, text="", font=("Helvetica", 18), bg="#9b59b6", fg="white")
    msg.grid(row=3, column=2)

    # Function to update the game message
    def updateMessage(x):
        msg['text'] = x

    # Function to update user's score
    def updateUserScore():
        score = int(playerScore["text"])
        score += 1
        playerScore["text"] = str(score)

    # Function to update computer's score
    def updateCompScore():
        score = int(computerScore["text"])
        score += 1
        computerScore["text"] = str(score)

    # Function to check and announce the winner
    def checkWin(player, computer):
        if player == computer:
            updateMessage("It's a tie!")
        elif player == "rock":
            if computer == "paper":
                updateMessage("You lose. Paper covers rock.")
                updateCompScore()
            else:
                updateMessage("You win. Rock smashes scissors.")
                updateUserScore()
        elif player == "paper":
            if computer == "scissor":
                updateMessage("You lose. Scissors cut paper.")
                updateCompScore()
            else:
                updateMessage("You win. Paper covers rock.")
                updateUserScore()
        elif player == "scissor":
            if computer == "rock":
                updateMessage("You lose. Rock smashes scissors.")
                updateCompScore()
            else:
                updateMessage("You win. Scissors cut paper.")
                updateUserScore()

    # Function to update choices (user and computer)
    choices = ["rock", "paper", "scissor"]

    def updateChoice(x):
        # For computer
        compChoice = choices[randint(0, 2)]
        if compChoice == "rock":
            comp_label.configure(image=rock_img_comp)
        elif compChoice == "paper":
            comp_label.configure(image=paper_img_comp)
        else:
            comp_label.configure(image=scissor_img_comp)

        # For user
        if x == "rock":
            user_label.configure(image=rock_img)
        elif x == "paper":
            user_label.configure(image=paper_img)
        else:
            user_label.configure(image=scissor_img)

        checkWin(x, compChoice)

    # Create styled buttons for user choices
    style = ttk.Style()
    style.configure("Game.TButton", font=("Helvetica", 14))
    style.configure("Rock.TButton", background="#FF3E4D", foreground="white")
    style.configure("Paper.TButton", background="#FAD02E", foreground="white")
    style.configure("Scissor.TButton", background="#0ABDE3", foreground="white")

    rock_button = ttk.Button(root, text="ROCK", style="Game.TButton", width=10, command=lambda: updateChoice("rock"))
    paper_button = ttk.Button(root, text="PAPER", style="Game.TButton", width=10, command=lambda: updateChoice("paper"))
    scissor_button = ttk.Button(root, text="SCISSOR", style="Game.TButton", width=10, command=lambda: updateChoice("scissor"))

    rock_button.grid(row=2, column=1, padx=10, pady=10)
    paper_button.grid(row=2, column=2, padx=10, pady=10)
    scissor_button.grid(row=2, column=3, padx=10, pady=10)

# Start Game button
start_button = tk.Button(root, text="Start Game", font=("Helvetica", 16), bg="#4CAF50", fg="white", command=start_game)
start_button.pack()

# Start the Tkinter main loop
root.mainloop()
