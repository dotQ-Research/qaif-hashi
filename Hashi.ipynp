import tkinter as tk
import random

# Define the grid size
GRID_SIZE = 5

class QuantumHashiGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quantum Hashi - Error Correction")

        # Create a canvas for the game grid
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        # Initialize the grid
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.errors = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        # Generate random errors (red bridges)
        self.generate_random_errors()

        # Draw the initial grid
        self.draw_grid()

        # Bind click event to the canvas
        self.canvas.bind("<Button-1>", self.on_click)

    def generate_random_errors(self):
        for _ in range(GRID_SIZE):
            i, j = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            self.errors[i][j] = True

    def draw_grid(self):
        self.canvas.delete("all")

        # Draw the grid lines
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x0, y0 = i * 80, j * 80
                x1, y1 = (i + 1) * 80, (j + 1) * 80
                self.canvas.create_rectangle(x0, y0, x1, y1)

                # Draw red bridge (error)
                if self.errors[i][j]:
                    self.canvas.create_line(x0, y0, x1, y1, fill="red", width=3)

    def on_click(self, event):
        # Get the clicked cell coordinates
        x, y = event.x // 80, event.y // 80

        # If it's an error cell, correct it
        if self.errors[x][y]:
            self.errors[x][y] = False
            self.draw_grid()

            # Check if all errors are corrected
            if all(not error for row in self.errors for error in row):
                self.show_win_message()

    def show_win_message(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            200, 200, text="Congratulations! You've corrected all errors.", font=("Helvetica", 16)
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumHashiGame(root)
    root.mainloop()
