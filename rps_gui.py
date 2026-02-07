import tkinter as tk
import random

def play(user_choice):
    choices = {"Rock": "r", "Paper": "p", "Scissors": "s"}
    user = choices[user_choice]
    system = random.choice(["r", "p", "s"])

    result_text = ""

    if user == system:
        result_text = "Result: Tie"
    elif (user == "r" and system == "s") or \
         (user == "p" and system == "r") or \
         (user == "s" and system == "p"):
        result_text = "Result: You Win!"
    else:
        result_text = "Result: You Lost"

    # Display choices
    user_label.config(text=f"You: {user}")
    system_label.config(text=f"System: {system}")
    result_label.config(text=result_text)


def reset_game():
    user_label.config(text="You: -")
    system_label.config(text="System: -")
    result_label.config(text="Result: -")


# GUI window
root = tk.Tk()
root.title("Rock - Paper - Scissors Game")
root.geometry("350x300")

# Buttons
tk.Label(root, text="Choose one:", font=("Arial", 14)).pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Result labels
user_label = tk.Label(root, text="You: -", font=("Arial", 12))
user_label.pack(pady=10)

system_label = tk.Label(root, text="System: -", font=("Arial", 12))
system_label.pack(pady=5)

result_label = tk.Label(root, text="Result: -", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Reset button
tk.Button(root, text="Reset", width=12, command=reset_game).pack(pady=10)

root.mainloop()
