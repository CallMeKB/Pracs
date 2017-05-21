def calculate_blocks(rows):
    n=rows
    for i in range(rows):
        n += i
    print(n)

#calculate_blocks(6)


def calc_blocks_recursive(rows):
    if rows <= 0:
        return 0
    return rows + calc_blocks_recursive(rows - 1)

print(calc_blocks_recursive(6))