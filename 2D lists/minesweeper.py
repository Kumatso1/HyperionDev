def calculate_mine_counts(grid):
    
    """ Calculates the number of adjacent mines for each cell in a minesweeper grid.

    Ar:
        grid: A list of lists representing the minesweeper grid, where "#" represents a mine 
        and "-" represents a safe spot.

    Returns:
        A new list of lists with the same dimensions as the input grid, where each dash (-) is replaced by a digit
        indicating the number of adjacent mines.
    """

    rows, cols = len(grid), len(grid[0])
    new_grid = []
    for row in range(rows):
        new_row = []
        for col in range(cols):
            if grid[row][col] == "#":
                new_row.append("#")  # Mine stays the same
            else:
                mine_count = 0
                # Check all adjacent cells (including diagonals)
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == "#":
                            mine_count += 1
                new_row.append(str(mine_count))  # Convert count to string
        new_grid.append(new_row)
    return new_grid


def main():
    """
    Example usage of the calculate_mine_counts function.
    """
    grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
    ]

    calculated_grid = calculate_mine_counts(grid)
    for row in calculated_grid:
        print(row)


if __name__ == "__main__":
  main()
