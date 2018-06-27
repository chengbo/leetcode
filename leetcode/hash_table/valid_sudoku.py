def is_valid_sudoku(board):
    def is_valid(array):
        s = set()
        for i in range(9):
            if array[i] == '.':
                continue
            try:
                v = int(array[i])
                if v > 9 or v < 1:
                    return False
                if v in s:
                    return False
                s.add(v)
            except ValueError:
                return False
        return True

    for i in range(9):
        a = []
        for j in range(9):
            a.append(board[i][j])
        if not is_valid(a):
            return False

    for j in range(9):
        a = []
        for i in range(9):
            a.append(board[i][j])
        if not is_valid(a):
            return False

    def get_box(x, y):
        a = []
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                a.append(board[i][j])
        return a

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid(get_box(i, j)):
                return False

    return True
