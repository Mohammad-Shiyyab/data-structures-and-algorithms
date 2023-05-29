def row_sum(matrix):
    row_sums = []
    for row in matrix:
        row_sums.append(sum(row))
    return row_sums