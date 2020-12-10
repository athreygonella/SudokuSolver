import json
from urllib.request import urlopen
import time

import SudokuStructure


def getSudokuData(difficulty, size):
    requestURL = f'http://www.cs.utep.edu/cheon/ws/sudoku/new/?size={size}&level={difficulty}'

    with urlopen(requestURL) as response:
        source = response.read()

    data = json.loads(source)
    return data


# Example of Output
# {'response': True, 'size': '4', 'squares': [{'x': 0, 'y': 3, 'value': 3}, {'x': 1, 'y': 0, 'value': 3}, {'x': 1, 'y': 2, 'value': 4}, {'x': 2, 'y': 2, 'value': 3}, {'x': 3, 'y': 0, 'value': 4}, {'x': 3, 'y': 1, 'value': 3}]}

if __name__ == '__main__':
    print('Welcome to SudokuSolver!')
    difficultyString = input('Enter the desired difficulty of your sudoku puzzle (Easy, Medium, or Hard): ')

    difficulty = None
    while difficulty == None:
        # convert difficultyString to number
        if difficultyString == 'Easy':
            difficulty = 1
        elif difficultyString == 'Medium':
            difficulty = 2
        elif difficultyString == 'Hard':
            difficulty = 3
        else:
            difficultyString = input('Please enter a valid difficulty level (Easy, Medium, or Hard): ')

    size = 4    # Size of the sudoku

    data = getSudokuData(difficulty, size)
    if data['response'] == False:
        print('ERROR: Unable to receive Sudoku puzzle from API')
    else:
        grid = SudokuStructure.SudokuGrid(data, size)

    # Display initial Sudoku SudokuGrid
    print('Here is the unsolved Sudoku Grid!')
    grid.display()

    # Solve Sudoku and display finished Grid
    s = input('Press Enter to solve Sudoku')
    print('Solving...')
    start_time = time.time()
    grid.solve()

    print('Here is the solved Sudoku Grid!')
    grid.display()
    print('It took %s seconds to solve the Sudoku puzzle' % (time.time() - start_time))
