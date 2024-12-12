# Somebody's Part 2 answer in 9 lines:
# From Reddit https://www.reddit.com/r/adventofcode/comments/1ha27bo/2024_day_9_solutions/
# I added comments and logging statements.
#   list structure not that intuitive but unambiguous, and allows code to extract meaningful data
#

import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

FNAME = "Day09atest.txt"
FNAME = "Day09a.txt"

# initialize each var.
#   F is the list of file blocks
#   S is the list of space blocks
#   p
F, S, p = [], [], 0

for i, c in enumerate(open(FNAME).read().strip()):
    # wow what is [a,b][c] += .. ??
    # [F, S] is a list of two lists, F and S   and c alternates between 0 and 1
    # The expression [a,b][c] is a list of two elements, a and b. If c is 0, it returns a; if c is 1, it returns b.
    #    we alternately append another list to F or S
    #    in either case, the list is a list of integers from p to p+c
    #    := is the walrus operator, it assigns the value to the variable and returns it
    [F, S][i % 2] += [[*range(p, p := p + int(c))]]
logging.debug(f"imported data. \nF {F} \nS {S}")

#   F is the list of file blocks [[0, 1], [5, 6, 7], [11], [15, 16, 17], [19, 20], ....
#       position in list is the file ID number
#   S is the list of space blocks  [[2, 3, 4], [8, 9, 10], [12, 13, 14], [18], [21], [26], [31], [35], []]

# x, y are simple indexes by length of lists.
for y in reversed(range(len(F))):  # 3000, 2999, 2998, 2997, ...
    for x in range(len(S)):  # 0, 1, 2, 3, 4, 5, 6, 7, 8
        # test is next space at least as big as end-list file   and,
        # test file's first block further along than space's first block
        # !opportunity to break? at 2nd test to save time
        if len(S[x]) >= len(F[y]) and F[y][0] > S[x][0]:
            # "move" the file by updating it's first block to the space's first block
            F[y] = S[x][: len(F[y])]
            S[x] = S[x][len(F[y]) :]
#   the Space list does not need to be correct in areas where file blocks moved out!

logging.debug(f"rearranged data. \nF {F} \nS {S}")
#   F is the list of file blocks [[0, 1], [5, 6, 7], [4], [15, 16, 17],...
#       position in list is the file ID number
#   S is the list of space blocks  [[], [], [14], [18], [21], [26], [31], [35], []]

print(sum((i * j) for i, f in enumerate(F) for j in f))
#     ... the first for loop (i, eg 1 and [5,6,7]) is the file ID number
#     ... the second for loop (j e.g. 5,6,7) is the block number in each file

# for my file produces a smaller number 6363913128533 which is good.
