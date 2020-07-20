# Game of Life Kata

## Milestone 1: Game of life implementation


from copy import deepcopy


def get_ASCII_file(path):
    """
    INPUT
    path: path to the file
    OUTPUT
    gird_board: the values of the input as a nested list
    """
    f = open(path, 'r')
    print("$ cat {}\n!Name: Toad\n".format(path)+f.read())
    try:
        with open(path) as f:
            rows = f.readlines()
            grid_board = [list(columns[:-1]) for columns in rows][1:-1]
    except:
        print("unvalid file")
    valid_state = valid_file(grid_board)
    if valid_state == True:
        return grid_board



def valid_file(grid):
    validation = True
    for row in grid:
        for cell in row:
            if cell not in ['.','O']:
                validation = False
                print("unvalid file, no valid value")
                break
    return validation

def get_adjacents(grid, cell_row, cell_column):
    """
    INPUT
    grid: 2d array/ nested list with the "." | "O" values
    celd_row: index of the the lists elements
    celd_column: index of the nested list elements
    OUTPUT
    count_adjacents_cells: the sum of the adjacents cells alives
    """
    count_adj_cells = 0
    height = len(grid)
    weight = len(grid[cell_row])

    for y in range(-1, 2):
        for x in range(-1, 2):
            valid_neighbor = True
            neighbor_row = cell_row + y
            neighbor_column = cell_column + x
            if neighbor_row < 0 or neighbor_row >= height:
                valid_neighbor = False
            if neighbor_column < 0 or neighbor_column >= weight:
                valid_neighbor = False
            if y == 0 and x == 0:
                valid_neighbor = False
            if valid_neighbor:
                if grid[neighbor_row][neighbor_column] == 'O':
                    count_adj_cells += 1
    return count_adj_cells



def count_adjacents(grid):
    """
    INPUT
    grid:2d array/ nested list with the "." | "O" values
    OUTPUT
    new_grid: 2d array/ nested list with the "." | "O" values modified by the convoys game conditions
    """
    new_grid = deepcopy(grid)
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            life_neighbors = get_adjacents(grid, row, cell)
            if grid[row][cell] == "." and life_neighbors == 3:
                new_grid[row][cell] = "O"
            if grid[row][cell] == "O" and life_neighbors in [2, 3]:
                new_grid[row][cell] = "O"
            if grid[row][cell] == "O" and life_neighbors not in [2, 3]:
                new_grid[row][cell] = "."
    return new_grid


def render_path(grid):
    """
    INPUT
    grid: 2d array/ nested list with the "." | "O" values
    OUTPUT
    text_file: ascii format data ready to be load
    """
    text_file = ""
    for i in grid:
        text_file += ','.join(i)+"\n"
    text_file = text_file.replace(",","")
    print(text_file)
    return text_file


def run_game(path):
    """
    INPUT
    path: path to the file
    OUTPUT
    text_grid: last instance of the grid ready to be load as a ASCII file
    """
    grid = get_ASCII_file(path)
    ticket_grid = "cat {}".format(path)
    new_grid = count_adjacents(grid)
    text_grid = render_path(new_grid)

    while True:
        ticket_grid += " | gameoflife"
        print(ticket_grid)
        next_grid = count_adjacents(new_grid)
        if new_grid == next_grid:
            text_grid = render_path(next_grid)
            break
        text_grid = render_path(new_grid)
        new_grid = deepcopy(next_grid)
    return text_grid


pattern = "game_state_1.txt"
game_life = run_game(pattern)











