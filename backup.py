grid = list()

# Note: Fixed the "0" to "O" in key 4 for consistency
tokens = {1:"1", 2:"2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

cell_counter = 1

for row in range(1, 6):
    new_row = list()

    # Check if this is a horizontal divider row (row 2 and 4)
    if row % 2 == 0:
        new_row.append('-----------')
    else:
        for col in range(1, 12):
            # Render Vertical Dividers
            if col % 4 == 0:
                new_row.append('|')
            # Render the Token (X, O)
            elif (col == 2 or col == 6 or col == 10):
                # Use str(cell_counter) to see the numbers 1-9
                new_row.append(tokens[cell_counter])
                cell_counter += 1
            # Render Padding Spaces
            else:
                new_row.append(' ')

    grid.append(new_row)

for row in grid:
    print(''.join(row))