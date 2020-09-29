"""
Task:

https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.

Before the game begins, players set up the board and place the ships accordingly to the following rules:

- There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
- Each ship must be a straight line, except for submarines, which are just single cell.
- The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

This is all you need to solve this kata. If you're interested in more information about the game, visit this link.
"""

# Solution:


def construct_ship(ship, points, p):
    x, y = p
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]:
        if (x + dx, y + dy) in points:
            ship.append((x + dx, y + dy))
            points -= {(x + dx, y + dy)}
            construct_ship(ship, points, (x + dx, y + dy))


def validate_battlefield(field):
    points = {(x, y) for x in range(len(field)) for y in range(len(field[0])) if field[x][y]}
    ships = []


    while points:
        p = next(iter(points))
        ship = [p]
        points -= {p}
        ships.append(ship)
        construct_ship(ship, points, p)

    if sorted([len(s) for s in ships]) != [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]:
        return False
    for s in ships:
        x_line = [1 for p in s if p[0] == s[0][0]]
        y_line = [1 for p in s if p[1] == s[0][1]]
        if len(x_line) != len(s) and len(y_line) != len(s):
            return False

    return True
