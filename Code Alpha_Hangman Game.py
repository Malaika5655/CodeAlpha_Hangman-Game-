import tkinter as tk
import random

class HangmanGUI:
    def __init__(self, root):
        self.words = ["apple", "banana", "orange", "grapes", "mango"]
        self.word = random.choice(self.words)
        self.guessed = ['_'] * len(self.word)
        self.attempts = 6
        self.guessed_letters = []

        self.root = root
        self.root.title("🎯 Hangman Game")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f8ff")

        # Display the guessed word
        self.label_word = tk.Label(root, text=' '.join(self.guessed), font=('Consolas', 30, 'bold'), bg="#f0f8ff", fg="#333")
        self.label_word.pack(pady=20)

        # Canvas for Hangman drawing
        self.canvas = tk.Canvas(root, width=200, height=200, bg="white", highlightthickness=2, highlightbackground="black")
        self.canvas.pack(pady=10)
        self.draw_base()

        # Label for status info
        self.label_info = tk.Label(root, text="Guess a letter (A-Z)", font=('Arial', 14), bg="#f0f8ff", fg="#0F3548")
        self.label_info.pack(pady=5)

        # Entry box
        self.entry = tk.Entry(root, font=('Arial', 16), width=5, justify='center')
        self.entry.pack()

        # Button
        self.button = tk.Button(root, text="Guess", command=self.guess_letter, bg="#43688e", fg="white", font=('Arial', 12, 'bold'))
        self.button.pack(pady=10)

        # Result label
        self.label_result = tk.Label(root, text="", font=('Arial', 14), bg="#f0f8ff", fg="#990000")
        self.label_result.pack()

        # Guessed letters
        self.label_guessed = tk.Label(root, text="Guessed Letters: ", font=('Arial', 12), bg="#f0f8ff", fg="#444")
        self.label_guessed.pack(pady=5)

    def draw_base(self):
        # Draws the gallows
        self.canvas.create_line(20, 180, 180, 180)  # base
        self.canvas.create_line(50, 180, 50, 20)    # pole
        self.canvas.create_line(50, 20, 120, 20)    # top bar
        self.canvas.create_line(120, 20, 120, 40)   # rope

    def draw_hangman(self, stage):
        # Draw hangman parts step by step
        if stage == 5:
            self.canvas.create_oval(100, 40, 140, 80)  # head
        elif stage == 4:
            self.canvas.create_line(120, 80, 120, 130)  # body
        elif stage == 3:
            self.canvas.create_line(120, 90, 90, 110)   # left arm
        elif stage == 2:
            self.canvas.create_line(120, 90, 150, 110)  # right arm
        elif stage == 1:
            self.canvas.create_line(120, 130, 90, 160)  # left leg
        elif stage == 0:
            self.canvas.create_line(120, 130, 150, 160)  # right leg

    def guess_letter(self):
        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not letter.isalpha() or len(letter) != 1:
            self.label_result.config(text="Enter a single letter (A-Z).")
            return

        if letter in self.guessed_letters:
            self.label_result.config(text="You already guessed that letter.")
            return

        self.guessed_letters.append(letter)
        self.label_guessed.config(text=f"Guessed Letters: {', '.join(self.guessed_letters)}")

        if letter in self.word:
            for idx, l in enumerate(self.word):
                if l == letter:
                    self.guessed[idx] = letter
            self.label_word.config(text=' '.join(self.guessed))
            self.label_result.config(text="Correct guess!", fg="green")
        else:
            self.attempts -= 1
            self.draw_hangman(self.attempts)
            self.label_result.config(text=f"Wrong guess! Attempts left: {self.attempts}", fg="red")

        if '_' not in self.guessed:
            self.label_result.config(text=f"You WON! The word was '{self.word}'", fg="blue")
            self.button.config(state='disabled')
        elif self.attempts == 0:
            self.label_word.config(text=self.word)
            self.label_result.config(text=f"Game Over! Word was '{self.word}'", fg="darkred")
            self.button.config(state='disabled')

# Run the GUI
root = tk.Tk()
HangmanGUI(root)
root.mainloop()
