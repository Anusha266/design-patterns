import random
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Tuple, Optional


class State(Enum):
    WON = 'won'
    PROGRESS = 'progress'
    DRAW = 'draw'


class Role(Enum):
    HUMAN = 'human'
    AI = 'ai'


# -------------------------
# Board
# -------------------------
class Board:
    def __init__(self, n: int):
        self.n = n
        # 0 means empty; otherwise store symbol (like 'X'/'O')
        self.grid = [[0 for _ in range(n)] for __ in range(n)]

    def print_board(self):
        # print indices header
        header = "   " + " ".join(f"{i}" for i in range(self.n))
        print(header)
        for r in range(self.n):
            row_str = f"{r}  " + " ".join(str(self.grid[r][c]) if self.grid[r][c] != 0 else "." for c in range(self.n))
            print(row_str)
        print()

    def is_valid_move(self, row: int, col: int) -> bool:
        return 0 <= row < self.n and 0 <= col < self.n and self.is_cell_empty(row, col)

    def is_cell_empty(self, row: int, col: int) -> bool:
        return self.grid[row][col] == 0

    def make_move(self, row: int, col: int, symbol: str) -> bool:
        if not self.is_valid_move(row, col):
            return False
        self.grid[row][col] = symbol
        return True

    def clear_board(self):
        self.grid = [[0 for _ in range(self.n)] for __ in range(self.n)]

    def get_empty_cells(self) -> List[Tuple[int, int]]:
        empties = []
        for r in range(self.n):
            for c in range(self.n):
                if self.grid[r][c] == 0:
                    empties.append((r, c))
        return empties


# -------------------------
# Winning Strategy
# -------------------------
class WinningStrategy(ABC):
    @abstractmethod
    def check_win(self, board: Board, last_move: Tuple[int, int], player_symbol: str) -> bool:
        """Return True if player_symbol has won given the last move."""
        pass


class RowWinningStrategy(WinningStrategy):
    def check_win(self, board: Board, last_move: Tuple[int, int], player_symbol: str) -> bool:
        row, _ = last_move
        for c in range(board.n):
            if board.grid[row][c] != player_symbol:
                return False
        return True


class ColWinningStrategy(WinningStrategy):
    def check_win(self, board: Board, last_move: Tuple[int, int], player_symbol: str) -> bool:
        _, col = last_move
        for r in range(board.n):
            if board.grid[r][col] != player_symbol:
                return False
        return True


class MainDiagWinningStrategy(WinningStrategy):
    def check_win(self, board: Board, last_move: Tuple[int, int], player_symbol: str) -> bool:
        row, col = last_move
        # only relevant if move was on main diagonal
        if row != col:
            return False
        for i in range(board.n):
            if board.grid[i][i] != player_symbol:
                return False
        return True


class AntiDiagWinningStrategy(WinningStrategy):
    def check_win(self, board: Board, last_move: Tuple[int, int], player_symbol: str) -> bool:
        row, col = last_move
        # only relevant if move was on anti-diagonal (row + col == n - 1)
        if row + col != board.n - 1:
            return False
        for i in range(board.n):
            if board.grid[i][board.n - 1 - i] != player_symbol:
                return False
        return True


class WinningStrategyManager:
    def __init__(self):
        self.strategies: List[WinningStrategy] = [
            RowWinningStrategy(),
            ColWinningStrategy(),
            MainDiagWinningStrategy(),
            AntiDiagWinningStrategy()
        ]

    def is_winner(self, board: Board, last_move: Tuple[int, int], player_symbol: str) -> bool:
        # Check all strategies (they internally verify relevancy)
        for strat in self.strategies:
            if strat.check_win(board, last_move, player_symbol):
                return True
        return False


# -------------------------
# Player Strategy (move decision)
# -------------------------
class PlayerStrategy(ABC):
    @abstractmethod
    def make_move(self, board: Board, player: "Player") -> Tuple[int, int]:
        """Should perform or return the move (row, col) that the player wants to make."""
        pass


class HumanStrategy(PlayerStrategy):
    def make_move(self, board: Board, player: "Player") -> Tuple[int, int]:
        board.print_board()
        while True:
            try:
                raw = input(f"{player.name} ({player.symbol}) - enter row and column (space separated): ")
                r_str, c_str = raw.strip().split()
                r, c = int(r_str), int(c_str)
                if board.is_valid_move(r, c):
                    return r, c
                else:
                    print("Invalid or occupied cell. Try again.")
            except ValueError:
                print("Invalid input format. Enter two integers separated by space.")


class RandomAIStrategy(PlayerStrategy):
    def make_move(self, board: Board, player: "Player") -> Tuple[int, int]:
        empties = board.get_empty_cells()
        if not empties:
            raise Exception("No moves left for AI")
        return random.choice(empties)


# Strategy registry maps Role to the strategy class
PLAYER_STRATEGY_REGISTRY = {
    Role.HUMAN: HumanStrategy,
    Role.AI: RandomAIStrategy
}


# -------------------------
# Player Builder / Factory / Player
# -------------------------
class Player:
    def __init__(self, name: str, symbol: str, role: Role):
        self.name = name
        self.symbol = symbol
        self.role = role
        self._strategy: Optional[PlayerStrategy] = None

    def get_strategy(self) -> PlayerStrategy:
        # Lazily instantiate the strategy for this player
        if self._strategy is None:
            strategy_cls = PLAYER_STRATEGY_REGISTRY.get(self.role)
            if not strategy_cls:
                raise ValueError(f"No strategy registered for role {self.role}")
            self._strategy = strategy_cls()
        return self._strategy

    def notify(self, message: str):
        print(f"[{self.name}] {message}")


class PlayerBuilder:
    def __init__(self):
        self._name: Optional[str] = None
        self._symbol: Optional[str] = None
        self._role: Optional[Role] = None

    def set_name(self, name: str) -> "PlayerBuilder":
        self._name = name
        return self

    def set_symbol(self, symbol: str) -> "PlayerBuilder":
        self._symbol = symbol
        return self

    def set_role(self, role: Role) -> "PlayerBuilder":
        self._role = role
        return self

    def build(self) -> Player:
        if not self._name or not self._symbol or not self._role:
            raise ValueError("Player requires name, symbol, and role")
        return Player(self._name, self._symbol, self._role)


class PlayerFactory:
    @staticmethod
    def create_player(name: str, symbol: str, role: Role) -> Player:
        return PlayerBuilder().set_name(name).set_symbol(symbol).set_role(role).build()


# -------------------------
# TicTacToe Game Controller
# -------------------------
class TicTacToeGame:
    def __init__(self, size: int, players: List[Player]):
        if size < 3:
            raise ValueError("Board size should be at least 3")
        if len(players) < 2:
            raise ValueError("At least two players required")
        if len(players) > size * size:
            raise ValueError("Too many players for the board")

        self.n = size
        self.board = Board(size)
        self.players = players
        self.state = State.PROGRESS
        self.winner: Optional[Player] = None
        self.moves = 0
        self.total_moves = size * size
        self.winning_manager = WinningStrategyManager()
        self.current_player_index = 0
        self._validate_unique_symbols()

    def _validate_unique_symbols(self):
        symbols = [p.symbol for p in self.players]
        if len(symbols) != len(set(symbols)):
            raise ValueError("Player symbols must be unique")

    def switch_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def notify_all(self, msg: str):
        for p in self.players:
            p.notify(msg)

    def play(self):
        # Play until win or draw
        while self.state == State.PROGRESS and self.moves < self.total_moves:
            player = self.players[self.current_player_index]
            strategy = player.get_strategy()
            try:
                row, col = strategy.make_move(self.board, player)
            except Exception as e:
                print("Error making move:", e)
                return

            successful = self.board.make_move(row, col, player.symbol)
            if not successful:
                # If strategy gave invalid move (shouldn't happen for our strategies), ask again
                print("The move was invalid. Asking player to retry.")
                continue

            self.moves += 1
            # Check for win using last move position
            if self.winning_manager.is_winner(self.board, (row, col), player.symbol):
                self.state = State.WON
                self.winner = player
                self.notify_all(f"{player.name} ({player.symbol}) has won the game!")
                self.board.print_board()
                return
            elif self.moves == self.total_moves:
                self.state = State.DRAW
                self.notify_all("Game is a draw!")
                self.board.print_board()
                return
            else:
                # Continue game
                self.switch_turn()

        # If loop ends unexpectedly
        if self.state == State.PROGRESS:
            self.state = State.DRAW
            self.notify_all("Game ended — draw by exhaustion.")
            self.board.print_board()


# -------------------------
# Example CLI main
# -------------------------
def main():
    print("Welcome to Tic-Tac-Toe (CLI)")
    # Simple flow to create 2 players (can be extended)
    size = 3
    while True:
        try:
            inp = input("Enter board size (press Enter for default 3): ").strip()
            if inp == "":
                break
            val = int(inp)
            if val < 3:
                print("Minimum board size is 3.")
                continue
            size = val
            break
        except ValueError:
            print("Please enter a valid integer.")

    players: List[Player] = []
    used_symbols = set()

    # Let's create two players
    for i in range(2):
        while True:
            raw = input(f"Enter player {i+1} as: name symbol role(human/ai) (e.g. Alice X human): ").strip().split()
            if len(raw) != 3:
                print("Invalid input. Provide exactly three tokens.")
                continue
            name, symbol, role_str = raw
            symbol = symbol.strip()
            if len(symbol) != 1 or not symbol.isprintable():
                print("Symbol must be a single printable character.")
                continue
            if symbol in used_symbols:
                print("Symbol already used. Pick another.")
                continue
            try:
                role = Role(role_str.lower())
            except ValueError:
                print("Role must be 'human' or 'ai'.")
                continue

            player = PlayerFactory.create_player(name, symbol, role)
            players.append(player)
            used_symbols.add(symbol)
            break

    game = TicTacToeGame(size=size, players=players)
    game.play()


if __name__ == "__main__":
    main()
