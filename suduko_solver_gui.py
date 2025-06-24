import tkinter as tk
from tkinter import messagebox

# ---------- Solver Logic ----------
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# ---------- GUI Logic ----------
def get_board_from_gui():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            if val == "":
                row.append(0)
            else:
                try:
                    row.append(int(val))
                except:
                    row.append(0)
        board.append(row)
    return board

def display_board_to_gui(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(board[i][j]))

def solve_gui():
    board = get_board_from_gui()
    if solve(board):
        display_board_to_gui(board)
        messagebox.showinfo("Solved!", "Sudoku has been solved successfully! 🎉")
    else:
        messagebox.showerror("No solution", "No solution exists for the given puzzle.")

# ---------- UI Setup ----------
window = tk.Tk()
window.title("🧩 Sudoku Solver GUI")

entries = [[None for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        entry = tk.Entry(window, width=2, font=('Arial', 18), justify='center')
        entry.grid(row=i, column=j, padx=2, pady=2)
        entries[i][j] = entry

solve_button = tk.Button(window, text="Solve Sudoku", font=("Arial", 14), command=solve_gui)
solve_button.grid(row=9, column=0, columnspan=9, pady=10)

window.mainloop()
