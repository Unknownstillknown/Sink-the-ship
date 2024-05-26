from ship import Ship

class Board:

    rows = 0
    colums = 0
    player1ships = []

    def __init__(self, rows, colums):
        self.rows = rows
        self.colums = colums

    def addship(self, start, end):
        ship = Ship(start, end)
        self.player1ships.append(ship)

    def displayboard(self):
        for i in range(1, self.rows):
            print(f"{'---'*self.colums}")
             

if __name__ == "__main__":
    board = Board(10,10)
    board.addship("A1", "A5")
    board.displayboard()