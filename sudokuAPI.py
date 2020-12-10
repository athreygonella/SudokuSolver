import json
from urllib.request import urlopen

size = 4
level = 2

linkAPI = (f'http://www.cs.utep.edu/cheon/ws/sudoku/new/?size={size}&level={level}')

print(linkAPI)

with urlopen(linkAPI) as response:
    source = response.read()

data = json.loads(source)

print()
print(data)

# Example of Output
# {'response': True, 'size': '4', 'squares': [{'x': 0, 'y': 3, 'value': 3}, {'x': 1, 'y': 0, 'value': 3}, {'x': 1, 'y': 2, 'value': 4}, {'x': 2, 'y': 2, 'value': 3}, {'x': 3, 'y': 0, 'value': 4}, {'x': 3, 'y': 1, 'value': 3}]}