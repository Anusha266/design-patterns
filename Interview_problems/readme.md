🧩 Tic-Tac-Toe (LLD) — README
📌 Overview

This project implements a fully object-oriented Tic-Tac-Toe game using clean LLD practices.
It follows a modular, extensible architecture suitable for interview-level LLD.

The system supports:

Human and AI players

Configurable board size (≥ 3)

Strategy Pattern for move decisions

Pluggable winning strategies

CLI-based gameplay

🏗️ High-Level Architecture


Main Components
Component	Responsibility
Board	Stores game state, validates moves, prints board
Player & Strategy	Player info + decision making via Strategy Pattern
Winning Strategies	Independent win-checking logics (Row, Col, Diagonals)
WinningStrategyManager	Runs all strategies for last move
PlayerFactory + Builder	Clean construction of Player objects
TicTacToeGame	Game controller (turns, status, gameplay loop)
🎯 Design Principles Followed (SOLID + OOP)
1. Single Responsibility Principle (SRP)

Each class handles only one reason to change:

Board → grid and move validation

Player → player information

PlayerStrategy → move decision

WinningStrategy → win detection

TicTacToeGame → game flow

2. Open/Closed Principle (OCP)

The game is open for extension, closed for modification:

Add a new AI strategy without touching game logic

Add a new winning strategy simply by adding a new class

Add more players without modifying core logic

Board size is configurable

3. Liskov Substitution Principle (LSP)

Every strategy follows the same interface:

PlayerStrategy subclasses can replace each other

WinningStrategy subclasses can be added/removed safely

4. Interface Segregation Principle (ISP)

Interfaces are lean:

PlayerStrategy → make_move()

WinningStrategy → check_win()

No unnecessary methods.

5. Dependency Inversion Principle (DIP)

Game depends on abstractions, not concrete classes:

Player depends on PlayerStrategy interface

TicTacToeGame depends on WinningStrategy interface

🧪 Design Patterns Used
1. Strategy Pattern

Used in two places:

a) Player move decision

Human → read input

AI → choose random cell

Easily extensible to:

Minimax AI

Heuristic AI

Network-based remote player

b) Winning conditions

Each winning logic is encapsulated in:

RowWinningStrategy

ColWinningStrategy

MainDiagWinningStrategy

AntiDiagWinningStrategy

WinningStrategyManager applies them all.

2. Factory Pattern

PlayerFactory creates players in a clean, abstracted way.

Useful for:

changing how players are created

avoiding messy constructor logic

3. Builder Pattern

PlayerBuilder gradually constructs a Player with:

name

symbol

role

This prevents telescoping constructors.

4. Manager Pattern

WinningStrategyManager centralizes all winning strategies and coordinates them.

5. Controller Pattern

TicTacToeGame acts as the game controller, managing:

Turn switching

Checking game status

Notifying players

Ending the game

🎮 Game Flow Summary

Player creation through factory

Board initialization

Game loop begins

Current player’s strategy produces a move

Board validates and applies the move

Winning strategies run

Game announces WIN / DRAW / CONTINUE

Turn switches