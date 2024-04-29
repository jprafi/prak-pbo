import tkinter as tk
from tkinter import messagebox
import random

class SudokuGrid(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.board = [[0]*3 for _ in range(3)]
        self.selected = None
        self.create_widgets()
        self.generate_board()
        self.draw_board()

    def create_widgets(self):
        self.grid_cells = [[tk.Entry(self, width=5, font=('Arial', 20), justify="center") for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.grid_cells[i][j].grid(row=i, column=j, padx=3, pady=3)
                self.grid_cells[i][j].bind('<FocusIn>', lambda event, i=i, j=j: self.select_cell(i, j))

        self.check_button = tk.Button(self, text="Check", command=self.check_solution)
        self.check_button.grid(row=3, column=0, columnspan=2, padx=3, pady=3)

        self.new_game_button = tk.Button(self, text="New Game", command=self.new_game)
        self.new_game_button.grid(row=3, column=2, columnspan=2, padx=3, pady=3)

    def generate_board(self):
        # Mengosongkan papan
        self.board = [[0]*3 for _ in range(3)]

        # Mengisi beberapa kotak secara acak dengan angka yang harus ditebak oleh pengguna
        filled_cells = random.sample(range(9), random.randint(1, 5))
        for cell in filled_cells:
            row = cell // 3
            col = cell % 3
            num = random.randint(1, 3)
            self.board[row][col] = num

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    self.grid_cells[i][j].insert(0, str(self.board[i][j]))
                else:
                    self.grid_cells[i][j].delete(0, tk.END)

    def select_cell(self, i, j):
        self.selected = (i, j)

    def check_solution(self):
        user_solution = []
        for i in range(3):
            row = []
            for j in range(3):
                value = self.grid_cells[i][j].get()
                if not value.isdigit():
                    messagebox.showerror("Error", "Please fill all cells with numbers.")
                    return
                row.append(int(value))
            user_solution.append(row)

        if self.validate_solution(user_solution):
            messagebox.showinfo("Congratulations", "You solved the Sudoku puzzle correctly!")
        else:
            messagebox.showerror("Oops!", "Your solution is incorrect. Please try again.")

    def validate_solution(self, solution):
        # Implementasi logika validasi solusi Sudoku
        return True  # Implementasikan logika sesuai kebutuhan

    def new_game(self):
        self.generate_board()
        self.draw_board()

class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku")
        self.grid_frame = SudokuGrid(master)
        self.grid_frame.pack(padx=10, pady=10)

def main():
    root = tk.Tk()
    sudoku_game = SudokuGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
