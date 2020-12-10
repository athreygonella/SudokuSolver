
class SudokuGrid:
    def __init__(self, data):
        self.size = 4
        self.squares = {}
        for col in range(0, self.size):
            for row in range(0, self.size):
                # create squares without values
                square = SudokuSquare(col, row, None)

                # add square to dict with tuple key for coordinates
                self.squares[(col, row)] = square

        # Populates squares with data received from API
        for squareData in data['squares']:
            x_coord = squareData['x']
            y_coord = squareData['y']
            square_value = squareData['value']
            self.squares[(x_coord, y_coord)].setValue(square_value)

    def display(self):
        print('-------------')
        for row in range(0, self.size):
            print('|', end = '')
            for col in range(0, self.size):
                values = self.squares[(col, row)].values
                if len(values) != 0:
                    print(values[0], end =' |')
                else:
                    print(' ', end = ' |')

            print()
            print('-------------')


class SudokuSquare:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y

        self.values = []

        if value != None:
            self.isFilled = True
            self.values.append(value)
        else:
            self.isFilled = False

    def setValue(self, value):
        if self.isFilled == False:
            self.values = []
            self.values.append(value)
            self.isFilled = True

    def addPossibleValue(value):
        self.values.append(value)
