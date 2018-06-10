def get_row(row_index):
    result = [1] * (row_index + 1)
    for i in range(row_index):
        for j in range(i, 0, -1):
            result[j] += result[j - 1]
    return result
