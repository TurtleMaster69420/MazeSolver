from copy import deepcopy
board = [[".", "x", "x", ".", "."],
         [".", ".", "x", ".", "."],
         [".", "x", ".", ".", "."],
         [".", ".", ".", "x", "."],
         ["x", "x", "x", "x", "."]]
def isFine(x1, y1, x2, y2):
    if (x2, y2) not in children and x2 >= 0 and x2 < len(board[0]) and y2 >= 0 and y2 < len(board) and board[y2][x2] != "x":
        if board[y2][x2] == ".":
            return True
        elif int(board[y2][x2]) > int(board[y1][x1]) + 1:
            return True
    else:
        return False
children = {(0, 0): 0}
found = False
while not found:
    childrenFake = deepcopy(children)
    for child in childrenFake:
        x = child[0]
        y = child[1]
        
        # Can go right
        if isFine(x, y, x + 1, y):
            children[(x + 1, y)] = children[(x, y)] + 1 
        # Can go left
        if isFine(x, y, x - 1, y):
            children[(x - 1, y)] = children[(x, y)] + 1
        # Can go up
        if isFine(x, y, x, y - 1):
            children[(x, y - 1)] = children[(x, y)] + 1
        # Can go down
        if isFine(x, y, x, y + 1):
            children[(x, y + 1)] = children[(x, y)] + 1
        if (len(board[0]) - 1, len(board) - 1) in children:
            found = True
            break
coords = (len(board[0]) - 1, len(board) - 1)
paths = []
while coords != (0, 0):
    value = children[coords]
    x = coords[0]
    y = coords[1]
    if (x - 1, y) in children and children[(x - 1, y)] == value - 1:
        coords = (x - 1, y)
    if (x + 1, y) in children and children[(x + 1, y)] == value - 1:
        coords = (x + 1, y)
    if (x, y + 1) in children and children[(x, y + 1)] == value - 1:
        coords = (x, y + 1)
    if (x, y - 1) in children and children[(x, y - 1)] == value - 1:
        coords = (x, y - 1)
    paths.append(coords)
paths = paths[::-1]
