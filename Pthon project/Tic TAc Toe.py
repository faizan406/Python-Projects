import tkinter as tk
from tkinter import messagebox

# Global variables
current_player = "X"
winner = False
buttons = [] # This will hold the Tkinter Button objects

def check_winner():
    global winner
    # Define all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]   # Diagonals
    ]

    for combo in winning_combinations:
        # Check if the text in the buttons of the current combination are the same and not empty
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            winner = True
            # Highlight the winning buttons in green
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")
            return # Exit after finding a winner

    # Check for a draw if no winner is found and all buttons are filled
    if not winner and all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        winner = True # Set winner to True to prevent further moves

def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner: # Only toggle player if no winner yet
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O" # Corrected '0' to 'O'
    label.config(text=f"Player {current_player}'s turn")

def reset_game():
    global current_player, winner
    current_player = "X"
    winner = False
    label.config(text=f"Player {current_player}'s turn")
    for button in buttons:
        button.config(text="", bg="SystemButtonFace") # Reset text and background color

# Main window setup
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons and add them to the 'buttons' list
for i in range(9):
    button = tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Label to display current player's turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("normal", 16), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
