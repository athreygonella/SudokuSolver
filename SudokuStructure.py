import math

class SudokuGrid:
    def __init__(self, data, size):
        self.size = size
        self.square_size = math.sqrt(size)

        self.cells = {}
        for col in range(0, self.size):
            for row in range(0, self.size):
                # create cells without values
                cell = SudokuCell(col, row, None, self.square_size)

                # add cell to dict with tuple key being the coordinates
                self.cells[(col, row)] = cell

        # Populates cells with data received from API
        for cellData in data['squares']:
            x_coord = cellData['x']
            y_coord = cellData['y']
            cell_value = cellData['value']
            self.cells[(x_coord, y_coord)].setValue(cell_value)

    def display(self):
        if self.size == 4:
            print('====================')
        elif self.size == 9:
            print('=========================================')

        for row in range(0, self.size):
            print('||', end = ' ')
            for col in range(0, self.size):
                cell = self.cells[(col, row)]

                if cell.isFilled:
                    print(cell.values[0], end = ' |')
                else:
                    print(' ', end = ' |')

                if (col + 1) % self.square_size == 0:
                    print('', end = '| ')
                else:
                    print('', end = ' ')

            print()
            if self.size == 4:
                if (row + 1) % self.square_size == 0:
                    print('====================')
                else:
                    print('--------------------')
            elif self.size == 9:
                if (row + 1) % self.square_size == 0:
                    print('=========================================')
                else:
                    print('-----------------------------------------')


    # Returns True if all cells in grid are filled
    def isGridFilled(self):
        for key, cell in self.cells.items():
            if cell.isFilled == False:
                return False
        return True

    # Returns list of possible values for a cell
    def findPossibleValuesRowCol(self, cell):
        # Initialize possible values
        possibles = []
        for x in range(1, self.size + 1):
            possibles.append(x)

        # Look across row (WORKING)
        for col in range(0, self.size):
            currentCell = self.cells[(col, cell.y)]
            if currentCell is not cell and currentCell.isFilled:
                if currentCell.values[0] in possibles:
                    possibles.remove(currentCell.values[0])

        # Look across column (WORKING)
        for row in range(0, self.size):
            currentCell = self.cells[(cell.x, row)]
            if currentCell is not cell and currentCell.isFilled:
                if currentCell.values[0] in possibles:
                    possibles.remove(currentCell.values[0])

        return possibles

    def findPossibleValuesSquare(self, cell, possibles):
        # Look within square (TODO: NOT WORKING)
        for key, currentCell in self.cells.items():
            if currentCell.square_location == cell.square_location:
                if currentCell is not cell and currentCell.isFilled:
                    if currentCell.values[0] in possibles:
                        # print('Removing ' + str(currentCell.values[0]) + ', which is at position ' + str(currentCell.x) + ',' + str(currentCell.y) + ' and square location ' + str(currentCell.square_location))

                        possibles.remove(currentCell.values[0])

        return possibles


    def solve(self):
        # while there are unfilled squares
            # for each square
                # if unfilled
                    # find possible values and update square's values list with
                    # if only one possible value, setValue()

        while not self.isGridFilled():
            for key, cell in self.cells.items():
                if not cell.isFilled:
                    possible_values = self.findPossibleValuesRowCol(cell)
                    # print(str(cell.x) + ',' + str(cell.y) + ': ' + str(possible_values) + '----->' + str(self.findPossibleValuesSquare(cell, possible_values)))

                    if len(possible_values) == 1:
                        cell.setValue(possible_values[0])
                        break
                    else:
                        cell.updatePossibleValues(possible_values)

            self.display()
            print()
            print()



class SudokuCell:
    def __init__(self, x, y, value, square_size):
        self.x = x
        self.y = y

        self.values = []

        if value != None:
            self.isFilled = True
            self.values.append(value)
        else:
            self.isFilled = False

        self.identifySquareLocation(square_size)

    def identifySquareLocation(self, square_size):
        square_column = math.floor(self.x / square_size)
        square_row = math.floor(self.y / square_size)
        self.square_location = (square_column, square_row)

    def setValue(self, value):
        if self.isFilled == False:
            self.values = []
            self.values.append(value)
            self.isFilled = True

    def updatePossibleValues(self, values):
        for value in values:
            self.values.append(value)
