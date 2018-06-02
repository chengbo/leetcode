def spiral_order(matrix):
    if len(matrix) == 0:
        return []

    result = []
    i = j = 0
    i_begin, i_end = 1, len(matrix)
    j_begin, j_end = 0, len(matrix[0])
    to_right, to_down, to_left, to_up = 0, 1, 2, 3
    direction = to_right
    count = i_end * j_end
    for _ in range(count):
        result.append(matrix[i][j])
        if direction == to_right:
            j += 1
            if j == j_end:
                direction = to_down
                i += 1
                j -= 1
                j_end -= 1
        elif direction == to_down:
            i += 1
            if i == i_end:
                direction = to_left
                j -= 1
                i -= 1
                i_end -= 1
        elif direction == to_left:
            j -= 1
            if j < j_begin:
                direction = to_up
                j = j_begin
                i -= 1
                j_begin += 1
        elif direction == to_up:
            i -= 1
            if i < i_begin:
                direction = to_right
                i = i_begin
                j += 1
                i_begin += 1

    return result
