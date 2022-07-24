from collections import defaultdict
a = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]

def isValidSudoku1(A):
    """Approach is we check for every row, every column, every 3*3 block.
       We take 3 dictionaries with keys as rowNo/colNo/blockNo
       and values as sets that stores numbers present in that row/col/block.
       We iterate through every element in 9*9 matrix and add them to respective dictionary values,
       if they are already present we return False"""
    rows = defaultdict(set)
    cols = defaultdict(set)
    blocks = defaultdict(set)
    for r in range(9):
        for c in range(9):
            if A[r][c] == '.':
                continue
            elif A[r][c] in rows[r] or A[r][c] in cols[c] or A[r][c] in blocks[(r // 3, c // 3)]:
                return 0  #
            else:
                rows[r].add(A[r][c])
                cols[c].add(A[r][c])
                blocks[(r // 3, c // 3)].add(A[r][c])
    return 1

def isValidSudoku2(A):
    """Approach is like previous one, but here instead of 3 dictionaries we take a single hashset and
       add strings into the set. The string is designed as value_row/col/block_rowNo/colNo/blockNo
       i.e. (e.g: 1row2, 3col1, 6block1-1...)"""
    ms = set()
    for r in range(9):
        for c in range(9):
            cur = A[r][c]
            if cur == '.':
                continue
            elif cur+'row'+str(r) in ms or cur+'col'+str(c) in ms or cur+'block'+str(r//3)+'-'+str(c//3) in ms:
                return 0
            else:
                ms.add(cur+'rows'+str(r))
                ms.add(cur+'cols'+str(c))
                ms.add(cur+'block'+str(r//3)+'-'+str(c//3))
    return 1

print(isValidSudoku1(a))
print(isValidSudoku2(a))

# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
