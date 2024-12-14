import itertools

directions = itertools.cycle([[-1,0],[0,1],[1,0],[0,-1]])
facing: list[int] = next(directions)

cur_row = 0
cur_col = 0

with open("06/input.txt", encoding="utf-8") as f:
    grid_strings = f.read().splitlines()
    for row_num in range(len(grid_strings)):
        # huh, I hardcoded starting facing north. /shrug.
        col_num = grid_strings[row_num].find("^")
        if col_num != -1:
            # found where we are.
            cur_row = row_num
            cur_col = col_num
            break
    grid: list[list[str]]= []
    for row in grid_strings:
        grid.append(list(row))
    grid[cur_row][cur_col] = 'X'
    next_row: int = cur_row + facing[0]
    next_col: int = cur_col + facing[1]
    while(next_row < len(grid[0]) and next_row >= 0 and next_col < len(grid) and next_col >= 0):
        # leave footsteps
        # print(cur_row, cur_col)
        if grid[next_row][next_col] == '#':
            # turn right
            facing = next(directions)
        else:
            # step forward
            cur_row = next_row
            cur_col = next_col
            # leave footsteps
            grid[cur_row][cur_col] = 'X'
        next_row = cur_row + facing[0]
        next_col = cur_col + facing[1]
    # we left the grid, count it
    footsteps = 0
    for row in grid:
        for col in row:
            if col == 'X':
                footsteps += 1
    print(footsteps)