"""
Memento Design Pattern Example:
Dynamic Chess Game (n x n board) with Undo functionality.

Below code is not complete design of chess game...It just shows that chess can be built efficiently with memento design pattern.
"""

# Memento - stores the chess board state
class ChessMemento:
    def __init__(self, board, turn):
        self._board = [row.copy() for row in board]  # deep copy of 2D list
        self._turn = turn

    def get_state(self):
        return [row.copy() for row in self._board], self._turn


# Originator - Chess game whose state we want to save/restore
class ChessGame:
    def __init__(self, n):
        self.n = n
        # Initialize empty board
        self._board = [["-" for _ in range(n)] for _ in range(n)]
        self._turn = "White"

    def make_move(self, row, col, piece):
        if 0 <= row < self.n and 0 <= col < self.n:
            self._board[row][col] = piece
            # Switch turn
            self._turn = "Black" if self._turn == "White" else "White"
            print(f"{piece} moved to ({row}, {col}). Turn: {self._turn}")
        else:
            print("Invalid move!")

    def show_board(self):
        print("Current Board:")
        for row in self._board:
            print(" ".join(row))
        print()

    def save(self):
        return ChessMemento(self._board, self._turn)

    def restore(self, memento):
        self._board, self._turn = memento.get_state()
        print("Restored board state. Turn:", self._turn)


# Caretaker - manages history of mementos
class History:
    def __init__(self):
        self._mementos = []

    def add(self, memento):
        self._mementos.append(memento)

    def undo(self):
        if self._mementos:
            return self._mementos.pop()
        return None


# ======== Client Code ========
if __name__ == "__main__":
    n = 5  # dynamic board size
    game = ChessGame(n)
    history = History()

    # Move 1
    game.make_move(0, 0, "WP")  # White Pawn
    history.add(game.save())
    game.show_board()

    # Move 2
    game.make_move(4, 4, "BP")  # Black Pawn
    history.add(game.save())
    game.show_board()

    # Move 3
    game.make_move(0, 1, "WR")  # White Rook
    history.add(game.save())
    game.show_board()

    # Undo last move
    memento = history.undo()
    if memento:
        game.restore(memento)
        game.show_board()

    # Undo again
    memento = history.undo()
    if memento:
        game.restore(memento)
        game.show_board()
