class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]
    
    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.last_move = None
    
    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)
    
    def move(self, move_string):
        """If the move is valid, reflect that move on the board."""
        move_string = move_string.lower().strip()
        valid_moves_lower = [m.lower() for m in Board.valid_moves]
        
        if move_string not in valid_moves_lower:
            raise TictactoeException("That's not a valid move.")
        
        move_index = valid_moves_lower.index(move_string)
        row, column = divmod(move_index, 3)
        
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        
        self.board_array[row][column] = self.turn
        self.turn = "O" if self.turn == "X" else "X"
    
    def whats_next(self):
        """game over check, and turn check."""
        win = False
        
        # Check rows
        for i in range(3):
            if self.board_array[i][0] != " " and self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]:
                win = True
                break
        
        # Check columns
        if not win:
            for i in range(3):
                if self.board_array[0][i] != " " and self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:
                    win = True
                    break
        
        # Check diagonals
        if not win:
            if self.board_array[1][1] != " ":
                if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]:
                    win = True
                elif self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
                    win = True
        
        if win:
            return (True, f"{'O' if self.turn == 'X' else 'X'} has won!")
        #check if tie
        for row in self.board_array:
            if " " in row:
                return (False, f"{self.turn}'s turn.")
        
        return (True, "Cat's Game.")

def play_tictactoe():
    print("=== TicTacToe Game ===")
    print("Valid moves:", ", ".join(Board.valid_moves))
    
    board = Board()
    
    while True:
        print("\n" + str(board))
        done, status = board.whats_next()
        print(status)
        
        if done:
            break
        
        move = input("Enter your move: ")
        try:
            board.move(move)
        except TictactoeException as e:
            print("Error:", e.message)

if __name__ == "__main__":
    play_tictactoe()