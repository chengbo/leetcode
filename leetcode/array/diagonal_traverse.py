def find_diagonal_order(matrix):
    if len(matrix) == 0:
        return []
    result = []
    i = j = 0
    up_right = True
    count = len(matrix) * len(matrix[0])
    for _ in range(count):
        result += [matrix[i][j]]
        if up_right:
            i -= 1
            j += 1
        else:
            i += 1
            j -= 1

        if i == len(matrix):
            i -= 1
            j += 2
            up_right = not up_right
        elif j == len(matrix[i]):
            j -= 1
            i += 2
            up_right = not up_right
        elif i < 0:
            i = 0
            up_right = not up_right
        elif j < 0:
            j = 0
            up_right = not up_right

    return result
