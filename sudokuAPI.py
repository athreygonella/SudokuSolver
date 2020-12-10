import json
from urllib.request import urlopen

def getSudokuData(difficulty):
    size = 9    # Size of the sudoku

    requestURL = f'http://www.cs.utep.edu/cheon/ws/sudoku/new/?size={size}&level={difficulty}'

    with urlopen(requestURL) as response:
        source = response.read()

    data = json.loads(source)
    print(data)

# Example of Output
# {'response': True, 'size': '4', 'squares': [{'x': 0, 'y': 3, 'value': 3}, {'x': 1, 'y': 0, 'value': 3}, {'x': 1, 'y': 2, 'value': 4}, {'x': 2, 'y': 2, 'value': 3}, {'x': 3, 'y': 0, 'value': 4}, {'x': 3, 'y': 1, 'value': 3}]}

if __name__ == '__main__':
    print('Welcome to SudokuSolver!')
    difficultyString = input('Enter the desired difficulty of your sudoku puzzle (Easy, Medium, or Hard): ')

    # convert difficultyString to number
    if difficultyString == 'Easy':
        difficulty = 1
    elif difficultyString == 'Medium':
        difficulty = 2
    else:
        difficulty = 3

    getSudokuData(difficulty)
