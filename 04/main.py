xmas = "XMAS"

xmas_count = 0

def rotate_text(lines:list[str]):
    row_count = len(lines)
    col_count = len(lines[0])
    if row_count != col_count:
        raise Exception("we assumed a square.")
    ## force it back into string form too
    return list(map("".join, zip(*lines[::-1])))

with open("04/input.txt", encoding="utf-8") as f:
    lines:list[str] = f.read().splitlines()
    row_count = len(lines)
    col_count = len(lines[0])
    if row_count != col_count:
        raise Exception("we assumed a square.")
    for _ in range(4):
        for line in lines:
            current_horizontal_count = line.count(xmas)
            xmas_count += current_horizontal_count
            print( "row: " + str(current_horizontal_count) + " " + line)
        ## diagonals starting along the left
        ## exclude center
        for starting_row in range(1,col_count):
            diag_string = ""
            col = 0
            row = starting_row
            while row < row_count:
                diag_string += lines[row][col]
                col += 1
                row += 1
            current_diagonal_count = diag_string.count(xmas)
            xmas_count += current_diagonal_count
            print(str(current_diagonal_count) + " for diagonal " + diag_string)
        ## diagonals starting up top
        ## include center
        for starting_col in range(col_count):
            diag_string = ""
            col = starting_col
            row = 0
            while col < col_count:
                diag_string += lines[row][col]
                col += 1
                row += 1
            current_diagonal_count = diag_string.count(xmas)
            xmas_count += current_diagonal_count
            print(str(current_diagonal_count) + " for diagonal " + diag_string)
        # rotate
        lines = rotate_text(lines)

## done w part 1, saved to xmas_count

## part 2 time.

x_mas_count = 0
a_count = 0

with open("04/input.txt", encoding="utf-8") as f:
    lines:list[str] = f.read().splitlines()
    for line in lines:
        print(line)
    row_count = len(lines)
    col_count = len(lines[0])
    for row in range(1, row_count - 1):
        for col in range(1, col_count - 1):
            if lines[row][col] != "A":
                continue # we only care about A
            corners = lines[row-1][col-1] + lines[row+1][col+1] + lines[row-1][col+1] + lines[row+1][col-1]
            print(str(row) + "," + str(col) + ": " + corners)
            ## hardcode the 4 corner permutations that work.
            if corners in ["MSMS", "MSSM", "SMSM", "SMMS"]:
                x_mas_count += 1

## done w part 2, saved to x_mas_count
                
print("part 1:")
print(xmas_count)

print("part 2:")
print(x_mas_count)