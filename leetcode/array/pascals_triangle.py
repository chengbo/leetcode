def generate(num_rows):
    if num_rows == 0:
        return []
    result = [[1]]
    for i in range(1, num_rows):
        row = [1, 1]
        for j in range(1, i):
            prev_row = result[i - 1]
            row.insert(j, prev_row[j - 1] + prev_row[j])
        result.append(row)
    return result
